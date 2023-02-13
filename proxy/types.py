from typing import NamedTuple

from requests.structures import CaseInsensitiveDict


class ProxyResponse(NamedTuple):
    content: bytes = None
    status_code: int = None
    errors: bool = True
    headers: CaseInsensitiveDict = {}
