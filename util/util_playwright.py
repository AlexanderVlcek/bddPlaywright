from enum import Enum


class WaitUntil(Enum):
    COMMIT = "commit"
    DOM_CONTENT_LOADED = "domcontentloaded"
    NETWORK_IDLE = "networkidle"

