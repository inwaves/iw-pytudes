import numpy as np
from typing import TypeVar, Generic, TypeVarTuple, NewType

MAIN = __name__ == "__main__"
DType = TypeVar("DType")
Shape = TypeVarTuple("Shape")
Height, Width = NewType("Height", float), NewType("Width", float)

class VariadicArray(Generic[DType, *Shape]):
    pass

if MAIN:
    a: VariadicArray[float, Height, Width] = VariadicArray()
    print(a)
