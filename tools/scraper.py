import requests
from bs4 import BeautifulSoup
from rich.repr import rich_repr


@rich_repr
class Server(object):
    id: str
    latitude: str
    longditude: str
    location: str
    provider: str
    country_code: str

    def __init__(
        self,
        id: str,
        latitude: str,
        longditude: str,
        location: str,
        provider: str,
        country_code: str,
    ):
        self.id = id
        self.latitude = latitude
        self.longditude = longditude
        self.location = location
        self.provider = provider
        self.country_code = country_code


def run():

    url = "https://www.whatsmydns.net/#A/github.com"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    SERVERS = []

    for i in soup.find_all(
        class_="border-b py-1 px-2 text-xs leading-none flex items-center cursor-pointer"
    ):

        SERVERS.append(
            Server(
                id=i["data-id"],
                latitude=i["data-latitude"],
                longditude=i["data-longitude"],
                location=i["data-location"],
                provider=i["data-provider"],
                country_code=i["data-country-code"],
            )
        )

    print(SERVERS)


if __name__ == "__main__":
    run()
