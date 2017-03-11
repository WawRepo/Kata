from unittest import TestCase
from arithmetic import *

class TestAritmetic(TestCase):
    def test_arithmetic_add(self):
        code = 'ss'
        stack = [1, 2]
        expected_stack = [3]
        arithmetic_add(code, stack)
        self.assertEquals(stack, expected_stack)

        code = 'ss'
        stack = [1]
        expected_stack = [1]
        arithmetic_add(code, stack)
        self.assertEquals(stack, expected_stack)


    def test_aritmetic(self):
        code = 'ssnss'
        code_rdr = code_reader(code)
        stack = [1, 2]
        expected_stack = [3]
        arithmetic(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        code = 'stnss'
        code_rdr = code_reader(code)
        stack = [1, 2]
        expected_stack = [-1]
        arithmetic(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        code = 'snnss'
        code_rdr = code_reader(code)
        stack = [2, 2]
        expected_stack = [4]
        arithmetic(code_rdr, stack)
        self.assertEquals(stack, expected_stack)