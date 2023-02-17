from enum import Enum
from typing import Union


class ExitReason(Enum):
    ok = 0
    timeout = 1
    error = 2


def check_reason(response: Union[str, ExitReason]= "") -> str:
    if response is ExitReason.timeout:
        return "TIMEOUT"
    elif response is ExitReason.error:
        return "ERROR"
    else:
        return f"string {response}"


if __name__ == "__main__":
    print(check_reason(ExitReason(2)))
    print(check_reason("keyboard interrupt"))
