from typing import Literal, TypeVar

import numpy as np
from numpy.typing import NDArray

_T = TypeVar("_T", bound=np.number)

def medoid(
    a: NDArray[_T], axis: Literal[0, 1] = 1, indexonly: bool = False
) -> NDArray[_T]: ...
def nanmedoid(
    a: NDArray[_T], axis: Literal[0, 1] = 1, indexonly: bool = False
) -> NDArray[_T]: ...
