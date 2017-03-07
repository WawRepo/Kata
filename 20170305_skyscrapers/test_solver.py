#from __future__ import absolute_import
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

        self.validation = (
            (1, 0, 0, 2),
            (0, 0, 0, 3),
            (0, 0, 0, 0),
            (0, 1, 3, 4)
        )

        self.board = [[1, 2, 4, 3], [2, 1, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.available_values_len_tab = [[[set([]), 0], [set([]), 0], [set([]), 0], [set([]), 0]]
            , [[set([4]), 1], [set([4]), 1], [set([]), 0], [set([4]), 1]]
            , [[set([3, 4]), 2], [set([3, 4]), 2], [set([1, 2]), 2], [set([1, 2, 4]), 3]]
            , [[set([3, 4]), 2], [set([3, 4]), 2], [set([1, 2]), 2], [set([1, 2, 4]), 3]]]

        self.unsolvable_board = [[2, 1, 4, 3], [3, 4, 1, 2], [4, 2, 3, 1], [1, 3, 0, 4]]


    def test_solve_scrapers(self):
        self.assertEqual(solve_puzzle(self.clues[0]), self.outcomes[0])
        self.assertEqual(solve_puzzle(self.clues[1]), self.outcomes[1])


    def test_visible_count(self):
        self.assertEqual(visible_count((1, 3, 4, 2)), 3)
        self.assertEqual(visible_count((2, 4, 3, 1)), 2)

    # (1, 3, 4, 2),
    # (4, 2, 1, 3),
    # (3, 4, 2, 1),
    # (2, 1, 3, 4)
    def test_view_for_hint(self):
        self.assertEqual(view_for_hint(0, self.outcomes[0]), [1, 4, 3, 2])
        self.assertEqual(view_for_hint(4, self.outcomes[0]), [2, 4, 3, 1])
        self.assertEqual(view_for_hint(8, self.outcomes[0]), [4, 1, 3, 2])
        self.assertEqual(view_for_hint(15, self.outcomes[0]), [1, 3, 4, 2])

    def test_validate_view_by_hint(self):
        self.assertTrue(validate_view_by_hint([1, 3, 4, 2], 3))

    def test_get_horizontal_values(self):
        self.assertEqual(get_horizontal_values(0, self.validation), {1, 2})
        self.assertEqual(get_horizontal_values(1, self.validation), {3})
        self.assertEqual(get_horizontal_values(3, self.validation), {1, 3, 4})

    def test_get_vertical_values(self):
        self.assertEqual(get_vertical_values(0, self.validation), {1})
        self.assertEqual(get_vertical_values(1, self.validation), {1})
        self.assertEqual(get_vertical_values(3, self.validation), {2, 3, 4})

    def test_available_values(self):
        self.assertEqual(available_values(0, 0, self.validation), {3, 4})
        self.assertEqual(available_values(1, 1, self.validation), {2, 4})
        self.assertFalse(len(available_values(3, 3, self.validation)))

    def test_get_avaialble_values(self):
        self.assertEqual(get_avaialble_values(self.board), self.available_values_len_tab)

    def test_get_next_position_with_minimal_len(self):
        self.assertEqual(get_next_position_with_minimal_len(self.board, self.available_values_len_tab), (1,3))

        #for solved game
        self.assertEqual(get_next_position_with_minimal_len(self.outcomes[0]
                                                            , get_avaialble_values(self.outcomes[0]))
                         , (None, None))

