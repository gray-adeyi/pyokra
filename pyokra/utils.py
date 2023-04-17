from dataclasses import dataclass
from enum import Enum
from io import BytesIO
from typing import Optional


@dataclass
class APIResponse:
    status_code: int
    status: Optional[str]
    message: Optional[str]
    data: Optional[dict]
    file: Optional[BytesIO]


@dataclass
class SandboxCustomer:
    account_no: int
    name: str
    bank: str
    username: str
    password: str
    type: str
    volume: str
    identity: int
    internet_speed: int

    def to_dict(self):
        return {
            "noOfAccount": self.account_no,
            "name": self.name,
            "bank": self.bank,
            "username": self.username,
            "password": self.password,
            "type": self.type,
            "volume": self.volume,
            "identity": self.identity,
            "internetSpeed": self.internet_speed,
        }


class ResponseType(str, Enum):
    JSON = "JSON"
    HTML = "HTML"
    FILE = "FILE"


class FileType(str, Enum):
    CSV = "csv"


class WeekDay(str, Enum):
    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"


class Currency(str, Enum):
    NGN = "NGN"


class Country(str, Enum):
    NG = "NG"


class APIVersion(str, Enum):
    V1 = "1"
    V2 = "2"


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class Mode(str, Enum):
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"
