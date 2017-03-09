from unittest import TestCase
from interpreter import *

class TestSolve(TestCase):

    def test_code_reader(self):
        code = '123'
        reader = code_reader(code)
        self.assertEquals(reader.next(), '1')
        self.assertEquals(reader.next(), '2')
        self.assertEquals(reader.next(), '3')
        self.assertRaises(StopIteration, lambda: reader.next())


    def test_read_until_terminal(self):
        code = '123nzcxn'
        reader = code_reader(code)
        self.assertEquals(read_until_terminal(reader), '123')
        self.assertEquals(read_until_terminal(reader), 'zcx')

    def test_parse_number(self):
        """Testing parsing mechanic"""
        number_wi = 'st'
        self.assertEquals(parse_number(number_wi), 1)
        number_wi = 'tt'
        self.assertEquals(parse_number(number_wi), -1)
        number_wi = 'ttss'
        self.assertEquals(parse_number(number_wi), -4)
        number_wi = ''
        self.assertRaises(Exception,lambda: parse_number(number_wi))


    def test_stack_manipulation_push(self):
        code = 'st'
        stack = []
        expected_stack = [1]
        stack_manipulation_push(code, stack)
        self.assertEquals(stack, expected_stack)

    def test_stack_manipulation_duplicate_nth(self):
        stack = [1, 2, 3, 4]
        code = 'stsn'#2
        code_rdr = code_reader(code)
        stack_manipulation_duplicate_nth(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 3, 3, 4])

    def test_stack_manipulation_discard_n(self):

    def test_stack_manipulation(self):
        code = 'sstnss'
        code_rdr = code_reader(code)
        stack = []
        expected_stack = [1]
        stack_manipulation(code_rdr, stack)
        self.assertEquals(stack, expected_stack)


    # def test_output_0_3(self):
    #     """ Testing push, output of numbers 0 through 3 """
    #     output1 = "   \t\n\t\n \t\n\n\n"
    #     output2 = "   \t \n\t\n \t\n\n\n"
    #     output3 = "   \t\t\n\t\n \t\n\n\n"
    #     output0 = "    \n\t\n \t\n\n\n"
    #     self.assertEquals(whitespace(output1), "1")
    #     self.assertEquals(whitespace(output2), "2")
    #     self.assertEquals(whitespace(output3), "3")
    #     self.assertEquals(whitespace(output0), "0")
    #
    #
    # def test_output_negative_1_3(self):
    #     """ Testing ouput of numbers -1 through -3 """
    #     outputNegative1 = "  \t\t\n\t\n \t\n\n\n"
    #     outputNegative2 = "  \t\t \n\t\n \t\n\n\n"
    #     outputNegative3 = "  \t\t\t\n\t\n \t\n\n\n"
    #     self.assertEquals(whitespace(outputNegative1), "-1")
    #     self.assertEquals(whitespace(outputNegative2), "-2")
    #     self.assertEquals(whitespace(outputNegative3), "-3")

    def test_error_for_empty_code(self):
        """Testing simple flow control edge case"""
        self.assertRaises(Exception, lambda: whitespace(''))

    # def test_letter_output_A_C(self):
    #     """Testing output of letters A through C"""
    #     outputA = "   \t     \t\n\t\n  \n\n\n"
    #     outputB = "   \t    \t \n\t\n  \n\n\n"
    #     outputC = "   \t    \t\t\n\t\n  \n\n\n"
    #     self.assertEquals(whitespace(outputA), "A")
    #     self.assertEquals(whitespace(outputB), "B")
    #     self.assertEquals(whitespace(outputC), "C")