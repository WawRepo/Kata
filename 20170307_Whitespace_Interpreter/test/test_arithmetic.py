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
        self.assertRaises(IndexError, lambda: arithmetic_add(code, stack))


    def test_arithmetic_divide(self):
        code = 'ss'
        stack = [6, 3]
        expected_stack = [2]
        arithmetic_divide(code, stack)
        self.assertEquals(stack, expected_stack)

        stack = [6, 0]
        expected_stack = []
        self.assertRaises(ZeroDivisionError, lambda: arithmetic_divide(code, stack))
        self.assertEquals(stack, expected_stack)

        code = 'ss'
        stack = [1]
        self.assertRaises(IndexError, lambda: arithmetic_divide(code, stack))

    def test_arithmetic_modulo(self):
        code = 'ss'
        stack = [4, 3]
        expected_stack = [1]
        arithmetic_modulo(code, stack)
        self.assertEquals(stack, expected_stack)

        stack = [4, 0]
        expected_stack = []
        self.assertRaises(ZeroDivisionError, lambda: arithmetic_modulo(code, stack))
        self.assertEquals(stack, expected_stack)

        code = 'ss'
        stack = [1]
        self.assertRaises(IndexError, lambda: arithmetic_modulo(code, stack))

    def test_arithmetic_flow(self):
        #sum
        code = 'ssnss'
        code_rdr = code_reader(code)
        stack = [1, 2]
        expected_stack = [3]
        arithmetic_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        #difference
        code = 'stnss'
        code_rdr = code_reader(code)
        stack = [1, 2]
        expected_stack = [-1]
        arithmetic_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        #multiply
        code = 'snnss'
        code_rdr = code_reader(code)
        stack = [2, 3]
        expected_stack = [6]
        arithmetic_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        #divide
        code = 'tsnss'
        code_rdr = code_reader(code)
        stack = [6, 3]
        expected_stack = [2]
        arithmetic_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        #modulo
        code = 'ttnss'
        code_rdr = code_reader(code)
        stack = [6, 3]
        expected_stack = [0]
        arithmetic_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)