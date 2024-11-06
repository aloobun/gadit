from typing import List, Tuple
import math


def bezier_quadratic(
    p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float], t: float
) -> Tuple[float, float]:

    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
    return (x, y)


def bezier_cubic(
    p0: Tuple[float, float],
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    p3: Tuple[float, float],
    t: float,
) -> Tuple[float, float]:

    x = (
        (1 - t) ** 3 * p0[0]
        + 3 * (1 - t) ** 2 * t * p1[0]
        + 3 * (1 - t) * t**2 * p2[0]
        + t**3 * p3[0]
    )
    y = (
        (1 - t) ** 3 * p0[1]
        + 3 * (1 - t) ** 2 * t * p1[1]
        + 3 * (1 - t) * t**2 * p2[1]
        + t**3 * p3[1]
    )
    return (x, y)


def bezier_generalized(
    control_points: List[Tuple[float, float]], t: float
) -> Tuple[float, float]:

    n = len(control_points) - 1
    x = 0
    y = 0
    for i in range(n + 1):
        x += (
            math.comb(n, i)
            * (1 - t) ** (n - i)
            * t**i
            * control_points[i][0]
        )
        y += (
            math.comb(n, i)
            * (1 - t) ** (n - i)
            * t**i
            * control_points[i][1]
        )
    return (x, y)


def hermite_curve(
    p0: Tuple[float, float],
    p1: Tuple[float, float],
    m0: Tuple[float, float],
    m1: Tuple[float, float],
    t: float,
) -> Tuple[float, float]:

    h00 = 2 * t**3 - 3 * t**2 + 1
    h10 = t**3 - 2 * t**2 + t
    h01 = -2 * t**3 + 3 * t**2
    h11 = t**3 - t**2
    x = h00 * p0[0] + h10 * m0[0] + h01 * p1[0] + h11 * m1[0]
    y = h00 * p0[1] + h10 * m0[1] + h01 * p1[1] + h11 * m1[1]
    return (x, y)

