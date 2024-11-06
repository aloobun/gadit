from typing import Optional, Tuple
import math

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def magnitude(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def normalize(v):
    mag = magnitude(v)
    return (v[0] / mag, v[1] / mag) if mag != 0 else (0, 0)

class Ray:
    def __init__(self, origin: Tuple[float, float], direction: Tuple[float, float]):
        self.origin = origin
        self.direction = normalize(direction)

class LineSegment:
    def __init__(self, start: Tuple[float, float], end: Tuple[float, float]):
        self.start = start
        self.end = end

class Line:
    def __init__(self, point1: Tuple[float, float], point2: Tuple[float, float]):
        self.point = point1
        self.direction = normalize(subtract(point2, point1))

class Circle:
    def __init__(self, center: Tuple[float, float], radius: float):
        self.center = center
        self.radius = radius

# Intersection functions b/w ray, line, circle
def ray_intersects_line(ray: Ray, line: Line) -> Optional[Tuple[float, float]]:
    p = ray.origin
    r = ray.direction
    q = line.point
    s = line.direction

    r_cross_s = r[0] * s[1] - r[1] * s[0]
    if r_cross_s == 0:
        return None  # Parallel or coincident

    t = ((q[0] - p[0]) * s[1] - (q[1] - p[1]) * s[0]) / r_cross_s
    return (p[0] + t * r[0], p[1] + t * r[1]) if t >= 0 else None

def line_segment_intersects_circle(segment: LineSegment, circle: Circle) -> bool:
    start, end = segment.start, segment.end
    cx, cy = circle.center
    radius = circle.radius

    start_to_center = subtract((cx, cy), start)
    end_to_start = subtract(end, start)
    projection_length = dot(start_to_center, end_to_start) / magnitude(end_to_start)
    closest_point = (start[0] + projection_length * end_to_start[0] / magnitude(end_to_start),
                     start[1] + projection_length * end_to_start[1] / magnitude(end_to_start))

    distance_to_center = magnitude(subtract(closest_point, (cx, cy)))
    return distance_to_center <= radius

def ray_intersects_circle(ray: Ray, circle: Circle) -> Optional[Tuple[float, float]]:
    p = ray.origin
    d = ray.direction
    c = circle.center
    r = circle.radius

    f = subtract(p, c)
    a = dot(d, d)
    b = 2 * dot(f, d)
    c = dot(f, f) - r**2
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None  # No intersection
    elif discriminant == 0:
        t = -b / (2 * a)
        return (p[0] + t * d[0], p[1] + t * d[1]) if t >= 0 else None
    else:
        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        if t1 >= 0:
            return (p[0] + t1 * d[0], p[1] + t1 * d[1])
        elif t2 >= 0:
            return (p[0] + t2 * d[0], p[1] + t2 * d[1])
        return None

def line_segment_intersects_line(segment: LineSegment, line: Line) -> Optional[Tuple[float, float]]:
    p1, p2 = segment.start, segment.end
    q, r = line.point, line.direction

    den = r[0] * (p2[1] - p1[1]) - r[1] * (p2[0] - p1[0])
    if den == 0:
        return None  # Parallel or coincident

    t = ((q[1] - p1[1]) * r[0] - (q[0] - p1[0]) * r[1]) / den
    u = ((q[1] - p1[1]) * (p2[0] - p1[0]) - (q[0] - p1[0]) * (p2[1] - p1[1])) / den

    if 0 <= t <= 1 and 0 <= u:
        return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))
    return None
