import numpy as np
from typing import TypeVar, Generic

MAIN = __name__ == "__main__"
bingus = TypeVar("bingus")
T = TypeVar("T")

class Binguses(Generic[T]):
    def __init__(self, elements) -> None:
        self.elements = elements

    def __repr__(self,) -> str:
        return repr(self.elements)

if MAIN:
    l: bingus = [1, 2, 3]
    b = Binguses(l)
    print(b)
