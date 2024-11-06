import unittest
from gadit.curves import *

class TestCurves(unittest.TestCase):
    def test_bezier_quadratic(self):
        p0 = (0, 0)
        p1 = (1, 1)
        p2 = (2, 0)
        t = 0.5
        expected = (1.0, 0.5)
        actual = bezier_quadratic(p0, p1, p2, t)
        self.assertEqual(actual, expected)

    def test_bezier_cubic(self):
        p0 = (0, 0)
        p1 = (1, 1)
        p2 = (2, -1)
        p3 = (3, 0)
        t = 0.5
        expected = (1.5, 0.0)
        actual = bezier_cubic(p0, p1, p2, p3, t)
        self.assertEqual(actual, expected)

    def test_bezier_generalized(self):
        control_points = [(0, 0), (1, 1), (2, 0)]
        t = 0.5
        expected = (1.0, 0.5)
        actual = bezier_generalized(control_points, t)
        self.assertEqual(actual, expected)

    def test_hermite_curve(self):
        p0 = (0, 0)
        p1 = (1, 0)
        m0 = (1, 1)
        m1 = (1, -1)
        t = 0.5
        expected = (0.5, 0.25)
        actual = hermite_curve(p0, p1, m0, m1, t)
        self.assertEqual(actual, expected)

    def test_catmull_rom_spline(self):
        p0 = (0, 0)
        p1 = (1, 1)
        p2 = (2, 0)
        p3 = (3, 1)
        t = 0.5
        expected_x = 1.5
        expected_y = 0.5
        actual_x, actual_y = catmull_rom_spline(p0, p1, p2, p3, t)
        self.assertAlmostEqual(actual_x, expected_x)
        self.assertAlmostEqual(actual_y, expected_y)
