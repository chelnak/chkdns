from typing import DefaultDict
import click
import sys
import asyncio
from functools import wraps

from rich import box
from rich.console import Console
from rich.progress import track
from rich.table import Table

from .whatsmydns import Client, QueryTimeoutException
from . import __version__

CLI_HELP = """
Validate a domain against a list of global DNS servers.

chkdns is powered by whatsmydns.net!
"""

TYPE_CHOICES = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT", "CAA"]


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command(help=CLI_HELP, no_args_is_help=True)
@click.option(
    "--type",
    default="A",
    show_default=True,
    type=click.Choice(TYPE_CHOICES),
    help="The type of record to query for.",
)
@click.option("--host", required=True, help="A valid hostname.")
@click.version_option(__version__)
@coro
async def cli(type, host):

    console = Console()

    dns = Client(use_mock=False)
    servers = dns.get_servers()

    table = Table(box=box.SIMPLE, leading=1, expand=True)
    table.add_column("", no_wrap=True)
    table.add_column("location", no_wrap=True)
    table.add_column("provider", no_wrap=True)
    table.add_column("result", justify="center", no_wrap=True)
    table.add_column("response", no_wrap=True)

    stats = DefaultDict(int)
    servers_count = len(servers)

    for server in track(
        sorted(servers, key=lambda server: server["provider"]),
        description=f"Checking DNS propagation for {host}",
        transient=True,
    ):

        try:
            response = await dns.query(server["id"], type, host)
            data = response["data"][0]

            if data["rcode"] == "NOERROR":
                stats["success"] += 1
                result = "✅"
            elif data["rcode"] == "SERVFAIL":
                result = "❌"
                stats["fail"] += 1
            else:
                result = "❓"
                stats["unknown"] += 1

            answer = ", ".join(answer.split()[-1] for answer in data["answers"])
        except QueryTimeoutException:

            result = "⏳"
            answer = "DNS query timed out."
            stats["timeout"] += 1

        except Exception:
            console.print_exception()
            sys.exit(1)

        table.add_row(
            server["flag"], server["location"], server["provider"], result, answer
        )

    score = stats["success"] / servers_count * 100
    table.caption = f"{score:.2f}% of servers responded successfully for {host}."

    console.print(table)
