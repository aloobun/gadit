from typing import Tuple
import math

def dot(v1: Tuple[float, float], v2: Tuple[float, float]) -> float:
    return v1[0] * v2[0] + v1[1] * v2[1]

def subtract(v1: Tuple[float, float], v2: Tuple[float, float]) -> Tuple[float, float]:
    return (v1[0] - v2[0], v1[1] - v2[1])

def magnitude(v: Tuple[float, float]) -> float:
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

def normalize(v: Tuple[float, float]) -> Tuple[float, float]:
    mag = magnitude(v)
    return (v[0] / mag, v[1] / mag) if mag != 0 else (0, 0)
