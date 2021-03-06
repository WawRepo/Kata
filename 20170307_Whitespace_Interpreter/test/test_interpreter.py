from unittest import TestCase
from interpreter import *


class TestInterpreter(TestCase):
    def test_output_0_3(self):
        """ Testing push, output of numbers 0 through 3 """
        output1 = "   \t\n\t\n \t\n\n\n"
        output2 = "   \t \n\t\n \t\n\n\n"
        output3 = "   \t\t\n\t\n \t\n\n\n"
        output0 = "    \n\t\n \t\n\n\n"
        self.assertEquals(whitespace(output1), "1")
        self.assertEquals(whitespace(output2), "2")
        self.assertEquals(whitespace(output3), "3")
        self.assertEquals(whitespace(output0), "0")


    def test_output_negative_1_3(self):
        """ Testing ouput of numbers -1 through -3 """
        outputNegative1 = "  \t\t\n\t\n \t\n\n\n"
        outputNegative2 = "  \t\t \n\t\n \t\n\n\n"
        outputNegative3 = "  \t\t\t\n\t\n \t\n\n\n"
        self.assertEquals(whitespace(outputNegative1), "-1")
        self.assertEquals(whitespace(outputNegative2), "-2")
        self.assertEquals(whitespace(outputNegative3), "-3")

    def test_error_for_empty_code(self):
        """Testing simple flow control edge case"""
        self.assertRaises(Exception, lambda: whitespace(''))

    def test_letter_output_A_C(self):
        """Testing output of letters A through C"""
        outputA = "   \t     \t\n\t\n  \n\n\n"
        outputB = "   \t    \t \n\t\n  \n\n\n"
        outputC = "   \t    \t\t\n\t\n  \n\n\n"
        self.assertEquals(whitespace(outputA), "A")
        self.assertEquals(whitespace(outputB), "B")
        self.assertEquals(whitespace(outputC), "C")


    def test_comment_remover(self):
        code = ' alas\tt\nn\t \n'
        comment_removed = ' \t\n\t \n'
        self.assertEqual(comment_removed, comment_remover(code))


    def test_from_CW_empty_stack_exeption(self):
        code =" \n\n"
        self.assertRaises(Exception, lambda: whitespace(code))


    def test_from_CW_out_of_bound_index_during_nth_duplication(self):
        code = "   \t\n   \t \n   \t\t\n \t  \t\t\n\t\n \t\n\n\n"
        self.assertRaises(IndexError, lambda: whitespace(code))


    def test_get_labels(self):
        code = 'nsstttnssstntnstnsssssnnnn'
        expected_labels = {'ttt':7, 'sss': 23}
        self.assertDictEqual(expected_labels, get_labels(code))

    def _test_from_CW_no_label_to_jump_fail(self):
        code = "   \t\n   \t \n   \t\t\n\t\n \t\n \n  \t\n\t\n \t\t\n \t\n  \n \n\t"
        self.assertRaises(IndexError, lambda: whitespace(code))

    def _test_from_CW_exception_from_unknown_label(self):
        code = "   \t\n\t\n \t\n \n \n   \t\n\t\n \t\n\n\n"
        self.assertRaises(KeyError, lambda: whitespace(code))

    def _test_from_CW_exception_subroutine_not_exit(self):
        code = "   \t\n\t\n \t\n \t\n\n  \n   \t \n\t\n \t"
        self.assertRaises(KeyError, lambda: whitespace(code))