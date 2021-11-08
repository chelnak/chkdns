import httpx
import socket
from urllib.parse import urlencode
from typing import Any, Optional
from random import choice
from .servers import SERVERS
from .mocks import RESPONSES


class QueryTimeoutException(Exception):
    """A query timeout exception."""

    pass


class QueryException(Exception):
    """A query exception."""

    pass


class Client:
    def __init__(
        self,
        use_mock: bool = False,
        timeout: Optional[float] = None,
    ) -> None:
        """A http client for whatsmydns.net

        Args:
            use_mock (bool, optional): Use a mocked set of responses. Defaults to False.
            timeout (Optional[float], optional): An optional timeout for requests. Defaults to None.
        """
        self.use_mock = use_mock
        self.base_url = "https://www.whatsmydns.net/api/"
        self.timeout = timeout if timeout else socket.getdefaulttimeout()

    async def request(self, endpoint: str, method: str = "GET") -> httpx.Response:
        """Make an async http request."""
        async with httpx.AsyncClient(
            timeout=self.timeout, base_url=self.base_url
        ) as client:
            response = await client.request(method=method, url=endpoint)
            return response

    def get_servers(self) -> list[dict[str, str]]:
        """Returns a list of queriable servers."""
        return SERVERS

    async def query(self, id: str, type: str, query: str) -> dict[str, Any]:
        """Query whatsmydns.net for a DNS record.

        Args:
            id (str): [description]
            type (str): [description]
            query (str): [description]

        Returns:
            httpx.Response: [description]

            {'data': [{'query': 'test.co.uk', 'type': 'A', 'id': 62728, 'opcode': 'QUERY', 'rcode': 'SERVFAIL', 'flags': {'qr': True, 'rd': True, 'ra': True}, 'questions': ['test.co.uk. IN A'], 'answers': [], 'authority': [], 'additional': [], 'response': []}]}
        """

        parameters = {"server": id, "type": type, "query": query}
        endpoint = f"details?{urlencode(parameters)}"

        if self.use_mock:
            response = choice(RESPONSES)

        else:
            raw_response = await self.request(endpoint=endpoint)

            if raw_response.is_error:
                raise QueryException(raw_response.json())

            response = raw_response.json()

        if response["data"][0]["response"] == "DNS query timed out":
            raise QueryTimeoutException(response["data"][0]["response"])

        return response
