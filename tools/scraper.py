import requests
import time
from rich.repr import rich_repr
import json

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
    url = 'https://www.whatsmydns.net/api/servers'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    result = requests.get(url,headers=headers).json()
    SERVERS = []

    for server in result:
            SERVERS.append(Server(
                id=server['id'],
                latitude=server['latitude'],
                longditude=server['longitude'],
                location=server['location'],
                provider=server['provider'],
                country_code=server['country'],
            )
       
         )

    with open("servers.txt", "a") as servers:
        for server in SERVERS:
            servers.write(str(server) + ', \n')

if __name__ == "__main__":
    run()
