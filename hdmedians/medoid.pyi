import numpy as np
from numpy.typing import NDArray
from typing import TypeVar

_T = TypeVar("_T", bound=np.number)

def medoid(a: NDArray[_T], axis: int = 1, indexonly: bool = False) -> NDArray[_T]: ...
def nanmedoid(a: NDArray[_T], axis: int = 1, indexonly: bool = False) -> NDArray[_T]: ...
