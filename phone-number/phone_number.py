import re


PHONE_RE = re.compile(r"""
    ^
    1 ?
    \D *
    ( \d {3} )
    \D *
    ( \d {3} )
    \D *
    ( \d {4} )
    \D *
    $
""", re.VERBOSE)


class Phone:
    def __init__(self, phone_number: str) -> None:
        match = PHONE_RE.search(phone_number)
        self.number = (
            "".join(match.groups())
            if match
            else "0000000000"
        )

    def area_code(self) -> str:
        return self.number[:3]

    def __str__(self) -> str:
        return PHONE_RE.sub(r"(\1) \2-\3", self.number)

    pretty = __str__
