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
    Server(
        "36", "34.05", "-118.24", "Los Angeles CA, United States", "Speakeasy", "us"
    ),
    Server("57", "32.78", "-96.79", "Dallas TX, United States", "Speakeasy", "us"),
    Server("325", "31", "-85", "Dothan AL, United States", "Comodo", "us"),
    Server("48", "33.75", "-84.38", "Atlanta GA, United States", "Bellsouth", "us"),
    Server(
        "241",
        "40.68",
        "-73.78",
        "Jamaica NY, United States",
        "Level 3 Communications",
        "us",
    ),
    Server("337", "49", "-123", "Burnaby, Canada", "Fortinet", "ca"),
    Server("412", "19", "-99", "Mexico City, Mexico", "Total Play", "mx"),
    Server("416", "-24", "-47", "Diadema, Brazil", "Trufer Comercio de Sucatas", "br"),
    Server("376", "37", "-2", "Almeria, Spain", "Vodafone Ono", "es"),
    Server("384", "53", "-2", "Manchester, United Kingdom", "Ancar B", "gb"),
    Server("371", "51", "3", "Lille, France", "Completel SAS", "fr"),
    Server("366", "52", "5", "Amsterdam, Netherlands", "Freedom Registry", "nl"),
    Server("398", "57", "10", "Aalborg, Denmark", "BMS", "dk"),
    Server("154", "51.65", "6.18", "Host, Germany", "Host Europe", "de"),
    Server("379", "47", "10", "Zizers, Switzerland", "Oskar Emmenegger", "ch"),
    Server("298", "43.72", "10.95", "Empoli, Italy", "Leonet", "it"),
    Server("364", "-26", "29", "Cullinan, South Africa", "Liquid", "za"),
    Server("428", "37", "31", "Antalya, Turkey", "Teknet Yazlim", "tr"),
    Server("361", "61", "77", "Nizhnevartovsk, Russia", "Rostelecom", "ru"),
    Server("304", "33.6", "73.07", "Rawalpindi, Pakistan", "CMPak", "pk"),
    Server("394", "29", "77", "Delhi, India", "OMNET", "in"),
    Server("209", "13.75", "100.5", "Bangkok, Thailand", "Loxley", "th"),
    Server("71", "3.11", "101.61", "Petaling Jaya, Malaysia", "Clear-Comm", "my"),
    Server("424", "1", "104", "Singapore, Singapore", "Linode", "sg"),
    Server("141", "32.06", "118.78", "Nanjing, China", "NanJing XinFeng IT", "cn"),
    Server("425", "38", "127", "Seoul, South Korea", "KT", "kr"),
    Server("429", "36", "140", "Chiyoda, Japan", "Kddi", "jp"),
    Server("346", "-35", "139", "Adelaide SA, Australia", "Telstra", "au"),
    Server("345", "-34", "151", "Melbourne VIC, Australia", "Pacific", "au"),
]
