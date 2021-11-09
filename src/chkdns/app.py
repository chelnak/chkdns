import click
import sys
import asyncio

from functools import wraps
from typing import DefaultDict

from rich import box
from rich.console import Console
from rich.repr import T
from rich.style import Style
from rich.table import Column, Table
from rich.live import Live

from .whatsmydns import Client, QueryTimeoutException
from . import __version__

CLI_HELP = """
Validate a domain against a list of global DNS servers.

chkdns is powered by whatsmydns.net!
"""

TYPE_CHOICES = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT", "CAA"]

RESULT_EMOJIS = {"succeeded": "✅", "failed": "❌", "timeout": "⌛", "unknown": "❓"}


class Stats(object):
    """A utility object used to store statistics."""

    def __init__(self, server_count: int):
        """A utility object used to store statistics.

        Args:
            server_count (int): The number of servers. Used to calculate percentages.
        """
        self.server_count = server_count
        self.stats: dict[str, int] = DefaultDict(int)

    def get_types(self) -> list[str]:
        """Returns a list of all types."""
        return list(self.stats.keys())

    def add(self, type) -> None:
        """Increment the count of the given type. If the type does not exist, it is added to the data structure."""
        self.stats[type] += 1

    def percentage_of(self, type) -> str:
        """Returns the percentage of the given type as a string."""
        return f"{self.stats[type] / self.server_count * 100:.2f}%"


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
    stats = Stats(server_count=len(servers))

    with Live(console=console) as live:

        table = Table(box=box.SIMPLE, expand=True, caption_justify="left")
        table.add_column("", no_wrap=True)
        table.add_column("location", no_wrap=True)
        table.add_column("provider", no_wrap=True)
        table.add_column("result", justify="center", no_wrap=True)
        table.add_column("response", no_wrap=True)

        for server in sorted(servers, key=lambda server: server["provider"]):

            try:
                response = await dns.query(server["id"], type, host)
                data = response["data"][0]

                if data["rcode"] == "NOERROR":
                    result = "succeeded"
                elif data["rcode"] == "SERVFAIL":
                    result = "failed"
                else:
                    result = "unknown"

                stats.add(type=result)
                answer = ", ".join(answer.split()[-1] for answer in data["answers"])

            except QueryTimeoutException:
                result = "timeout"
                answer = "DNS query timed out."
                stats.add(type="timeout")

            except Exception:
                console.print_exception()
                sys.exit(1)

            table.add_row(
                server["flag"],
                server["location"],
                server["provider"],
                RESULT_EMOJIS[result],
                answer,
            )

            caption = Table(
                *[Column(no_wrap=True) for _ in range(4)],
                box=box.SIMPLE,
                show_header=False,
                style=Style(dim=True),
            )

            for stat in stats.get_types():
                caption.add_row(RESULT_EMOJIS[stat], stat, stats.percentage_of(stat))

            table.caption = caption
            live.update(table)
