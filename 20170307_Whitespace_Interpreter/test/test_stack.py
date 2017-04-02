from unittest import TestCase
from stack import *

class TestStack(TestCase):
    def test_stack_manipulation_push(self):
        code = 'st'
        stack = []
        expected_stack = [1]
        stack_manipulation_push(code, stack)
        self.assertEquals(stack, expected_stack)

    def test_stack_manipulation_duplicate_nth(self):
        stack = [1, 2, 3, 4]
        code = 'ssn'  # 0
        code_rdr = code_reader(code)
        stack_manipulation_duplicate_nth(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 3, 4, 4])

        stack = [1, 2, 3, 4]
        code = 'stn'  # 1
        code_rdr = code_reader(code)
        stack_manipulation_duplicate_nth(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 3, 4, 3])

        stack = [1, 2, 3, 4]
        code = 'sttn'  # 3
        code_rdr = code_reader(code)
        stack_manipulation_duplicate_nth(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 3, 4, 1])

        #IndexError exeption
        stack = [1, 2, 3, 4]
        code = 'ttn'  # -1
        code_rdr = code_reader(code)
        self.assertRaises(IndexError, lambda: stack_manipulation_duplicate_nth(code_rdr, stack))

        #IndexError exeption
        code = 'stsssn'  # 8
        code_rdr = code_reader(code)
        self.assertRaises(IndexError, lambda: stack_manipulation_duplicate_nth(code_rdr, stack))


    def test_stack_manipulation_discard_n(self):
        stack = [1, 2, 3, 4]
        code = 'ssn'  # 0
        code_rdr = code_reader(code)
        stack_manipulation_discard_n(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 3, 4])

        stack = [1, 2, 3, 4]
        code = 'stn'  #1
        code_rdr = code_reader(code)
        stack_manipulation_discard_n(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 4])

        stack = [3, 2, 1, 4, 6, 7, 5]
        code = 'sttn'  #3
        code_rdr = code_reader(code)
        stack_manipulation_discard_n(code_rdr, stack)
        self.assertEqual(stack, [3, 2, 1, 5])

        stack = [1, 2, 3, 4]
        code = 'ttn'  #-1
        code_rdr = code_reader(code)
        stack_manipulation_discard_n(code_rdr, stack)
        self.assertEqual(stack, [4])

        stack = [1, 2, 3, 4]
        code = 'stsssn'  # 8
        code_rdr = code_reader(code)
        stack_manipulation_discard_n(code_rdr, stack)
        self.assertEqual(stack, [4])

    def test_stack_manipulation_duplicate_top(self):
        stack = [1, 2, 3, 4]
        code = 'stsssn'  # 8
        code_rdr = code_reader(code)
        stack_manipulation_duplicate_top(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 3, 4, 4])


    def test_stack_manipulation_swap(self):
        stack = [1, 2, 3, 4]
        code = 'stsssn'  # 8
        code_rdr = code_reader(code)
        stack_manipulation_swap(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 4, 3])

        stack = [4]
        code = 'stsssn'  # 8
        code_rdr = code_reader(code)
        stack_manipulation_swap(code_rdr, stack)
        self.assertEqual(stack, [4])


    def test_stack_manipulation_discard_top(self):
        stack = [1, 2, 3, 4]
        code = 'stsssn'  # 8
        code_rdr = code_reader(code)
        stack_manipulation_discard_top(code_rdr, stack)
        self.assertEqual(stack, [1, 2, 3])

        stack = []
        code = 'stsssn'  # 8
        code_rdr = code_reader(code)
        self.assertRaises(ValueError, lambda: stack_manipulation_discard_top(code_rdr, stack))
        self.assertEqual(stack, [])

    def test_stack_flow(self):
        code = 'sstnss'
        code_rdr = code_reader(code)
        stack = []
        expected_stack = [1]
        stack_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        code = 'tssttn'
        code_rdr = code_reader(code)
        stack = [1, 2, 3, 4]
        expected_stack = [1, 2, 3, 4, 1]
        stack_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        code = 'tnstn'
        code_rdr = code_reader(code)
        stack = [1, 2, 3, 4]
        expected_stack = [1, 2, 4]
        stack_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        code = 'nsstn'
        code_rdr = code_reader(code)
        stack = [1, 2, 3, 4]
        expected_stack = [1, 2, 3, 4, 4]
        stack_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

        code = 'nnstn'
        code_rdr = code_reader(code)
        stack = [1, 2, 3, 4]
        expected_stack = [1, 2, 3]
        stack_flow(code_rdr, stack)
        self.assertEquals(stack, expected_stack)