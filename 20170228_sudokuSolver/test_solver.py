from unittest import TestCase

from solver import *

class TestGame(TestCase):

    def setUp(self):
        self.problem = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]]

        self.problem1 = [
            [0, 9, 6, 5, 0, 4, 0, 7, 1],
            [0, 2, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 4, 0, 9, 0, 6, 2, 3],
            [0, 0, 3, 0, 6, 0, 0, 8, 0],
            [0, 0, 8, 0, 5, 0, 4, 0, 0],
            [9, 0, 0, 4, 0, 0, 0, 0, 5],
            [7, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 1, 0, 7, 5, 3, 4, 9],
            [2, 3, 0, 0, 4, 8, 1, 0, 7]]

    def test_get_square_values(self):
        self.assertEquals(get_square_values(7, 8, self.problem), {2, 7})
        self.assertEquals(get_square_values(4, 1, self.problem), {1,4,6,9})

    def test_get_horizontal_values(self):
        self.assertEquals(get_horizontal_values(4, 1, self.problem), {1, 4, 5, 6, 8})

    def test_get_vertical_values(self):
        self.assertEquals(get_vertical_values(4, 1, self.problem), {9, 6})

    def test_available_values(self):
        self.assertEquals(available_values(0, 0, self.problem), {2, 3, 6, 7})
        self.assertEquals(available_values(4, 1, self.problem), {2, 3, 7})

    def test_solve_1(self):
        solution = [[9, 2, 6, 5, 8, 3, 4, 7, 1], [7, 1, 3, 4, 2, 6, 9, 8, 5], [8, 4, 5, 9, 7, 1, 3, 6, 2], [3, 6, 2, 8, 5, 7, 1, 4, 9], [4, 7, 1, 2, 6, 9, 5, 3, 8], [5, 9, 8, 3, 1, 4, 7, 2, 6], [6, 5, 7, 1, 3, 8, 2, 9, 4], [2, 8, 4, 7, 9, 5, 6, 1, 3], [1, 3, 9, 6, 4, 2, 8, 5, 7]]
        self.assertEquals(solver(self.problem,[]), solution, "I felt a disturbance in the force")

    def test_solve_1(self):
        solution = [[3, 9, 6, 5, 2, 4, 8, 7, 1], [8, 2, 7, 1, 3, 6, 5, 9, 4], [5, 1, 4, 8, 9, 7, 6, 2, 3], [4, 5, 3, 7, 6, 1, 9, 8, 2], [1, 7, 8, 9, 5, 2, 4, 3, 6], [9, 6, 2, 4, 8, 3, 7, 1, 5], [7, 4, 5, 3, 1, 9, 2, 6, 8], [6, 8, 1, 2, 7, 5, 3, 4, 9], [2, 3, 9, 6, 4, 8, 1, 5, 7]]
        self.assertEquals(solver(self.problem1,[]), solution, "I felt a disturbance in the force")

    def test_validate_initial_board_char_false(self):
        self.problem[0][0] = 'a'
        self.assertFalse(validate_initial_board(self.problem))

    def test_validate_initial_board_not_admisive_value(self):
        self.problem[0][0] = 10
        self.assertFalse(validate_initial_board(self.problem))

    def test_validate_initial_board_not_reused_values(self):
        self.problem[0][1] = 9
        self.assertFalse(validate_initial_board(self.problem))

    def test_sudoku_solver(self):
        solution = [[9, 2, 6, 5, 8, 3, 4, 7, 1], [7, 1, 3, 4, 2, 6, 9, 8, 5], [8, 4, 5, 9, 7, 1, 3, 6, 2],
                    [3, 6, 2, 8, 5, 7, 1, 4, 9], [4, 7, 1, 2, 6, 9, 5, 3, 8], [5, 9, 8, 3, 1, 4, 7, 2, 6],
                    [6, 5, 7, 1, 3, 8, 2, 9, 4], [2, 8, 4, 7, 9, 5, 6, 1, 3], [1, 3, 9, 6, 4, 2, 8, 5, 7]]
        self.assertEquals(sudoku_solver(self.problem), solution, "I felt a disturbance in the force")

    def test_sudoku_solver1(self):
        solution = [[3, 9, 6, 5, 2, 4, 8, 7, 1], [8, 2, 7, 1, 3, 6, 5, 9, 4], [5, 1, 4, 8, 9, 7, 6, 2, 3],
                    [4, 5, 3, 7, 6, 1, 9, 8, 2], [1, 7, 8, 9, 5, 2, 4, 3, 6], [9, 6, 2, 4, 8, 3, 7, 1, 5],
                    [7, 4, 5, 3, 1, 9, 2, 6, 8], [6, 8, 1, 2, 7, 5, 3, 4, 9], [2, 3, 9, 6, 4, 8, 1, 5, 7]]
        self.assertEquals(sudoku_solver(self.problem1), solution, "I felt a disturbance in the force")
