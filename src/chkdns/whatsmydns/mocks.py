from typing import Any


RESPONSES: list[dict[str, Any]] = [
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 25076,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 5690 IN A 198.185.159.144",
                    "test.co.uk. 5690 IN A 198.185.159.145",
                    "test.co.uk. 5690 IN A 198.49.23.144",
                    "test.co.uk. 5690 IN A 198.49.23.145",
                ],
                "authority": [
                    "test.co.uk. 164090 IN NS dns1.p02.nsone.net.",
                    "test.co.uk. 164090 IN NS dns2.p02.nsone.net.",
                    "test.co.uk. 164090 IN NS dns3.p02.nsone.net.",
                    "test.co.uk. 164090 IN NS dns4.p02.nsone.net.",
                    "test.co.uk. 164090 IN NS ns01.squarespacedns.com.",
                    "test.co.uk. 164090 IN NS ns02.squarespacedns.com.",
                    "test.co.uk. 164090 IN NS ns03.squarespacedns.com.",
                    "test.co.uk. 164090 IN NS ns04.squarespacedns.com.",
                ],
                "additional": [
                    "ns01.squarespacedns.com. 152645 IN A 45.54.22.1",
                    "ns02.squarespacedns.com. 152645 IN A 45.54.22.65",
                    "ns03.squarespacedns.com. 152645 IN A 45.54.22.129",
                    "ns04.squarespacedns.com. 152645 IN A 45.54.22.193",
                ],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 49645,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 5464,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 5602 IN A 198.185.159.144",
                    "test.co.uk. 5602 IN A 198.185.159.145",
                    "test.co.uk. 5602 IN A 198.49.23.144",
                    "test.co.uk. 5602 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {"data": [{"query": "test.co.uk", "type": "A", "response": "DNS query timed out"}]},
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 20668,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 14400 IN A 198.185.159.144",
                    "test.co.uk. 14400 IN A 198.185.159.145",
                    "test.co.uk. 14400 IN A 198.49.23.144",
                    "test.co.uk. 14400 IN A 198.49.23.145",
                ],
                "authority": [
                    "test.co.uk. 137545 IN NS dns1.p02.nsone.net.",
                    "test.co.uk. 137545 IN NS dns2.p02.nsone.net.",
                    "test.co.uk. 137545 IN NS dns3.p02.nsone.net.",
                    "test.co.uk. 137545 IN NS dns4.p02.nsone.net.",
                    "test.co.uk. 137545 IN NS ns01.squarespacedns.com.",
                    "test.co.uk. 137545 IN NS ns02.squarespacedns.com.",
                    "test.co.uk. 137545 IN NS ns03.squarespacedns.com.",
                    "test.co.uk. 137545 IN NS ns04.squarespacedns.com.",
                ],
                "additional": [
                    "dns1.p02.nsone.net. 118483 IN AAAA 2620:4d:4000:6259:7:2:0:1",
                    "dns1.p02.nsone.net. 63315 IN A 198.51.44.2",
                    "dns2.p02.nsone.net. 118483 IN AAAA 2a00:edc0:6259:7:2::2",
                    "dns2.p02.nsone.net. 33633 IN A 198.51.45.2",
                    "dns3.p02.nsone.net. 118483 IN AAAA 2620: 4d: 4000: 6259: 7: 2: 0: 3",
                    "dns3.p02.nsone.net. 32190 IN A 198.51.44.66",
                    "dns4.p02.nsone.net. 32554 IN A 198.51.45.66",
                    "ns01.squarespacedns.com. 171476 IN A 45.54.22.1",
                    "ns02.squarespacedns.com. 163753 IN A 45.54.22.65",
                    "ns03.squarespacedns.com.168742 IN A 45.54.22.129",
                    "ns04.squarespacedns.com. 132630 IN A 45.54.22.193",
                ],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 41661,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 30 IN A 198.185.159.144",
                    "test.co.uk. 30 IN A 198.185.159.145",
                    "test.co.uk. 30 IN A 198.49.23.144",
                    "test.co.uk. 30 IN A 198.49.23.145",
                ],
                "authority": [
                    "test.co.uk. 1738 IN NS dns1.p02.nsone.net.",
                    "test.co.uk. 1738 IN NS dns2.p02.nsone.net.",
                    "test.co.uk. 1738 IN NS dns3.p02.nsone.net.",
                    "test.co.uk. 1738 IN NS dns4.p02.nsone.net.",
                    "test.co.uk. 1738 IN NS ns01.squarespacedns.com.",
                    "test.co.uk. 1738 IN NS ns02.squarespacedns.com.",
                    "test.co.uk. 1738 IN NS ns03.squarespacedns.com.",
                    "test.co.uk. 1738 IN NS ns04.squarespacedns.com.",
                ],
                "additional": [
                    "dns2.p02.nsone.net. 10485 IN AAAA 2a00:edc0:6259:7:2::2",
                    "dns2.p02.nsone.net. 17457 IN A 198.51.45.2",
                    "dns3.p02.nsone.net. 10086 IN AAAA 2620: 4d: 4000: 6259: 7: 2: 0: 3",
                    "dns3.p02.nsone.net. 8608 IN A 198.51.44.66",
                    "dns4.p02.nsone.net. 17020 IN A 198.51.45.66",
                    "dns4.p02.nsone.net. 17095 IN AAAA 2a00:edc0:6259:7:2::4",
                    "ns01.squarespacedns.com. 118 IN A 45.54.22.1",
                    "ns02.squarespacedns.com.1071 IN A 45.54.22.65",
                    "ns03.squarespacedns.com. 3381 IN A 45.54.22.129",
                    "ns04.squarespacedns.com. 1349 IN A 45.54.22.193",
                ],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 44765,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 5696 IN A 198.185.159.144",
                    "test.co.uk. 5696 IN A 198.185.159.145",
                    "test.co.uk. 5696 IN A 198.49.23.144",
                    "test.co.uk. 5696 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {"data": [{"query": "test.co.uk", "type": "A", "response": "DNS query timed out"}]},
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 9127,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 14400 IN A 198.185.159.144",
                    "test.co.uk. 14400 IN A 198.185.159.145",
                    "test.co.uk. 14400 IN A 198.49.23.144",
                    "test.co.uk. 14400 IN A 198.49.23.145",
                ],
                "authority": [
                    "test.co.uk. 172800 IN NS dns1.p02.nsone.net.",
                    "test.co.uk. 172800 IN NS dns2.p02.nsone.net.",
                    "test.co.uk. 172800 IN NS dns3.p02.nsone.net.",
                    "test.co.uk. 172800 IN NS dns4.p02.nsone.net.",
                    "test.co.uk. 172800 IN NS ns01.squarespacedns.com.",
                    "test.co.uk. 172800 IN NS ns02.squarespacedns.com.",
                    "test.co.uk. 172800 IN NS ns03.squarespacedns.com.",
                    "test.co.uk. 172800 IN NS ns04.squarespacedns.com.",
                ],
                "additional": [
                    "dns1.p02.nsone.net. 10255 IN A 198.51.44.2",
                    "dns2.p02.nsone.net. 136489 IN AAAA 2a00:edc0:6259:7:2::2",
                    "dns2.p02.nsone.net. 43189 IN A 198.51.45.2",
                    "dns3.p02.nsone.net. 10255 IN A 198.51.44.66",
                    "dns3.p02.nsone.net. 51297 IN AAAA 2620: 4d: 4000: 6259: 7: 2: 0: 3",
                    "dns4.p02.nsone.net. 13080 IN A 198.51.45.66",
                    "dns4.p02.nsone.net. 92309 IN AAAA 2a00:edc0: 6259: 7: 2: : 4",
                    "ns01.squarespacedns.com. 159122 IN A 45.54.22.1",
                    "ns02.squarespacedns.com. 154975 IN A 45.54.22.65",
                    "ns03.squarespacedns.com.159181 IN A 45.54.22.129",
                    "ns04.squarespacedns.com. 154494 IN A 45.54.22.193",
                ],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {"data": [{"query": "test.co.uk", "type": "A", "response": "DNS query timed out"}]},
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 29995,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 5703 IN A 198.185.159.144",
                    "test.co.uk. 5703 IN A 198.185.159.145",
                    "test.co.uk. 5703 IN A 198.49.23.144",
                    "test.co.uk. 5703 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 58479,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 5709 IN A 198.185.159.144",
                    "test.co.uk. 5709 IN A 198.185.159.145",
                    "test.co.uk. 5709 IN A 198.49.23.144",
                    "test.co.uk. 5709 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 41218,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 30 IN A 198.185.159.144",
                    "test.co.uk. 30 IN A 198.185.159.145",
                    "test.co.uk. 30 IN A 198.49.23.144",
                    "test.co.uk. 30 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 18827,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 33699,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 0 IN A 198.185.159.144",
                    "test.co.uk. 0 IN A 198.185.159.145",
                    "test.co.uk. 0 IN A 198.49.23.144",
                    "test.co.uk. 0 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 5434,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 5706 IN A 198.185.159.144",
                    "test.co.uk. 5706 IN A 198.185.159.145",
                    "test.co.uk. 5706 IN A 198.49.23.144",
                    "test.co.uk. 5706 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 63102,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 5727 IN A 198.185.159.144",
                    "test.co.uk. 5727 IN A 198.185.159.145",
                    "test.co.uk. 5727 IN A 198.49.23.144",
                    "test.co.uk. 5727 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {"data": [{"query": "test.co.uk", "type": "A", "response": "DNS query timed out"}]},
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 61609,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {"data": [{"query": "test.co.uk", "type": "A", "response": "DNS query timed out"}]},
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 60452,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 32530,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {"data": [{"query": "test.co.uk", "type": "A", "response": "DNS query timed out"}]},
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 63572,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 13732 IN A 198.185.159.144",
                    "test.co.uk. 13732 IN A 198.185.159.145",
                    "test.co.uk. 13732 IN A 198.49.23.144",
                    "test.co.uk. 13732 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {"data": [{"query": "test.co.uk", "type": "A", "response": "DNS query timed out"}]},
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 16004,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 13731 IN A 198.185.159.144",
                    "test.co.uk. 13731 IN A 198.185.159.145",
                    "test.co.uk. 13731 IN A 198.49.23.144",
                    "test.co.uk. 13731 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 48708,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 10774,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 4143,
                "opcode": "QUERY",
                "rcode": "SERVFAIL",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [],
                "authority": [],
                "additional": [],
                "response": [],
            }
        ]
    },
    {
        "data": [
            {
                "query": "test.co.uk",
                "type": "A",
                "id": 19644,
                "opcode": "QUERY",
                "rcode": "NOERROR",
                "flags": {"qr": True, "rd": True, "ra": True},
                "questions": ["test.co.uk. IN A"],
                "answers": [
                    "test.co.uk. 14400 IN A 198.185.159.144",
                    "test.co.uk. 14400 IN A 198.185.159.145",
                    "test.co.uk. 14400 IN A 198.49.23.144",
                    "test.co.uk. 14400 IN A 198.49.23.145",
                ],
                "authority": [],
                "additional": [],
                "response": [
                    "198.185.159.144",
                    "198.185.159.145",
                    "198.49.23.144",
                    "198.49.23.145",
                ],
            }
        ]
    },
]
