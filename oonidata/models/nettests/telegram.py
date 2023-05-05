from dataclasses import dataclass
from typing import List, Optional
from oonidata.compat import add_slots
from oonidata.models.dataformats import (
    BaseTestKeys,
    DNSQuery,
    Failure,
    HTTPTransaction,
    NetworkEvent,
    TCPConnect,
    TLSHandshake,
)
from oonidata.models.nettests.base_measurement import BaseMeasurement


@add_slots
@dataclass
class TelegramTestKeys(BaseTestKeys):
    failure: Failure = None
    failed_operation: Optional[str] = None

    network_events: Optional[List[NetworkEvent]] = None
    tls_handshakes: Optional[List[TLSHandshake]] = None
    queries: Optional[List[DNSQuery]] = None
    tcp_connect: Optional[List[TCPConnect]] = None
    requests: Optional[List[HTTPTransaction]] = None

    telegram_http_blocking: Optional[bool] = None
    telegram_tcp_blocking: Optional[bool] = None
    telegram_web_failure: Optional[str] = None
    telegram_web_status: Optional[str] = None


@add_slots
@dataclass
class Telegram(BaseMeasurement):
    __test_name__ = "telegram"

    test_keys: TelegramTestKeys
