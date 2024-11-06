import unittest
import math
from gadit.intersections import Ray, Line, LineSegment, Circle
from gadit.intersections import ray_intersects_line, line_segment_intersects_circle, ray_intersects_circle, line_segment_intersects_line

class TestIntersections(unittest.TestCase):
    def test_ray_intersects_line(self):
        ray = Ray((0, 0), (1, 1))
        line = Line((1, 0), (1, 1))
        self.assertEqual(ray_intersects_line(ray, line), (1, 1))

    def test_line_segment_intersects_circle(self):
        segment = LineSegment((0, 0), (2, 2))
        circle = Circle((1, 1), 1)
        self.assertTrue(line_segment_intersects_circle(segment, circle))

    def test_ray_intersects_circle(self):
        ray = Ray((0, 0), (1, 1))
        circle = Circle((3, 3), 1)
        self.assertEqual(ray_intersects_circle(ray, circle), (3 - math.sqrt(2)/2, 3 - math.sqrt(2)/2))

    def test_line_segment_intersects_line(self):
        segment = LineSegment((0, 0), (2, 2))
        line = Line((0, 2), (2, 0))
        self.assertEqual(line_segment_intersects_line(segment, line), (1, 1))

if __name__ == '__main__':
    unittest.main()
