from __future__ import absolute_import
from unittest import TestCase
from solver import *

class TestSolve(TestCase):

    def setUp(self):
        self.clues = (
            (2, 2, 1, 3,
             2, 2, 3, 1,
             1, 2, 2, 3,
             3, 2, 1, 3),
            (0, 0, 1, 2,
             0, 2, 0, 0,
             0, 3, 0, 0,
             0, 1, 0, 0)
        )
        self.outcomes = (
            ((1, 3, 4, 2),
             (4, 2, 1, 3),
             (3, 4, 2, 1),
             (2, 1, 3, 4)),
            ((2, 1, 4, 3),
             (3, 4, 1, 2),
             (4, 2, 3, 1),
             (1, 3, 2, 4))
        )

    def test_solve_scrapers(self):
        self.assertEqual(solve_scrapers(self.clues[0]), self.outcomes[0])
        self.assertEqual(solve_scrapers(self.clues[1]), self.outcomes[1])


    def test_visible_count(self):
        self.assertEqual(visible_count((1, 3, 4, 2)), 3)