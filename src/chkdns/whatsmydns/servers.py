FLAGS = {
    "US": "🇺🇸",
    "CA": "🇨🇦",
    "AU": "🇦🇺",
    "NZ": "🇳🇿",
    "GB": "🇬🇧",
    "IE": "🇮🇪",
    "DE": "🇩🇪",
    "FR": "🇫🇷",
    "NL": "🇳🇱",
    "BE": "🇧🇪",
    "ES": "🇪🇸",
    "IT": "🇮🇹",
    "DK": "🇩🇰",
    "SE": "🇸🇪",
    "NO": "🇳🇴",
    "FI": "🇫🇮",
    "PT": "🇵🇹",
    "AT": "🇦🇹",
    "CH": "🇨🇭",
    "CZ": "🇨🇿",
    "PL": "🇵🇱",
    "SK": "🇸🇰",
    "HU": "🇭🇺",
    "RO": "🇷🇴",
    "RU": "🇷🇺",
    "UA": "🇺🇦",
    "GR": "🇬🇷",
    "TR": "🇹🇷",
    "CN": "🇨🇳",
    "JP": "🇯🇵",
    "KR": "🇰🇷",
    "IN": "🇮🇳",
    "TW": "🇹🇼",
    "HK": "🇭🇰",
    "SG": "🇸🇬",
    "MY": "🇲🇾",
    "PH": "🇵🇭",
    "TH": "🇹🇭",
    "ID": "🇮🇩",
    "VN": "🇻🇳",
    "IL": "🇮🇱",
    "SA": "🇸🇦",
    "AE": "🇦🇪",
    "JO": "🇯🇴",
    "IQ": "🇮🇶",
    "IR": "🇮🇷",
    "KW": "🇰🇼",
    "OM": "🇴🇲",
    "QA": "🇶🇦",
    "LB": "🇱🇧",
    "SY": "🇸🇾",
    "PS": "🇵🇸",
    "KZ": "🇰🇿",
    "SA": "🇸🇦",
    "YE": "🇾🇪",
    "VN": "🇻🇳",
    "ZW": "🇿🇲",
    "PK": "🇵🇰",
    "ZA": "🇿🇦",
    "MX": "🇲🇽",
    "BR": "🇧🇷",
}


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

    @property
    def flag(self) -> str:
        return FLAGS.get(self.country_code.upper(), "✈️")


SERVERS: list[Server] = [
    Server('oajdnppj', 31, -85, 'Dothan AL, United States', 'Comodo', 'us'), 
    Server('vdjvwabp', 33.75, -84.38, 'Atlanta GA, United States', 'Speakeasy', 'us'), 
    Server('oajdyabp', 38.95, -77.34, 'Reston VA, United States', 'Sprint', 'us'), 
    Server('gxbreqjo', 41.82, -71.42, 'Providence RI, United States', 'Verizon', 'us'), 
    Server('zgjgwyjn', 42.35, -71.05, 'Boston MA, United States', 'Speakeasy', 'us'), 
    Server('gobwzdjm', 45.44, -73.87, 'Beaconsfield QC, Canada', 'PubNIX', 'ca'), 
    Server('qrjnpdgj', 25, -107, 'Culiacan, Mexico', 'Megacable', 'mx'), 
    Server('dxbznoyb', -30, -52, 'Santa Cruz do Sul, Brazil', 'Claro', 'br'), 
    Server('pqboeokb', 37, -6, 'Paterna de Rivera, Spain', 'ServiHosting', 'es'), 
    Server('zejyoqrj', 53, -2, 'Manchester, United Kingdom', 'Ancar B', 'gb'), 
    Server('vxjlnzlj', 51, 3, 'Lille, France', 'Completel SAS', 'fr'), 
    Server('dzbxgkvj', 51, 6, 'Weert, Netherlands', 'Pyton', 'nl'), 
    Server('zgbgdkjn', 51.52, 7.45, 'Dortmund, Germany', 'Verizon', 'de'), 
    Server('qrjnpnnj', 47, 10, 'Zizers, Switzerland', 'Oskar Emmenegger', 'ch'), 
    Server('dabkezmb', 44.54, 10.78, 'Sassuolo, Italy', 'Telecom Italia', 'it'), 
    Server('ywjqnwqb', -26, 29, 'Cullinan, South Africa', 'Liquid', 'za'), 
    Server('qrbnpxgb', 37, 31, 'Antalya, Turkey', 'Teknet Yazlim', 'tr'), 
    Server('qrbnvwbx', 59.89, 30.26, 'Saint Petersburg, Russia', 'Prometey', 'ru'), 
    Server('plbpgeoj', 33.6, 73.07, 'Rawalpindi, Pakistan', 'CMPak', 'pk'), 
    Server('vxblnmlb', 11, 79, 'Ariyalur, India', 'Railwire', 'in'), 
    Server('dzjxgrwb', 3, 102, 'Shah Alam, Malaysia', 'TT Dotcom', 'my'), 
    Server('gxbrvdob', 1, 104, 'Singapore, Singapore', 'Tefincom', 'sg'), 
    Server('zgbgxkjn', 39.91, 116.4, 'Beijing, China', 'CNNIC', 'cn'), 
    Server('oajdnalj', 38, 127, 'Seoul, South Korea', 'KT', 'kr'), 
    Server('dabkemab', 36, 140, 'Chiyoda, Japan', 'Kddi', 'jp'), 
    Server('dajkerqj', -35, 139, 'Adelaide SA, Australia', 'Telstra', 'au'), 
    Server('zebykgbq', -37.8, 144.98, 'Melbourne VIC, Australia', 'Pacific Internet', 'au'), 
]
