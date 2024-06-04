from typing import Literal, TypeVar

import numpy as np
from numpy.typing import NDArray

Float32Or64 = TypeVar("Float32Or64", np.float32, np.float64)

def geomedian(
    X: NDArray[Float32Or64],
    axis: Literal[1, 2] = 1,
    eps: float = 1e-8,
    maxiters: int = 1000
) -> NDArray[Float32Or64]: ...

def nangeomedian(
    X: NDArray[Float32Or64],
    axis: Literal[1, 2] = 1,
    eps: float = 1e-7,
    maxiters: int = 500
) -> NDArray[Float32Or64]: ...
