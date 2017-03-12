from unittest import TestCase
from heap import *

class TestAritmetic(TestCase):
    def test_stack_to_heap(self):
        stack_to_heap()

    # def test_heap_to_stack(self):
    #     heap_to_stack()

    def test_aritmetic(self):
        #sum
        code = 'ssnss'
        code_rdr = code_reader(code)
        stack = [1, 2]
        expected_stack = [3]
        arithmetic(code_rdr, stack)
        self.assertEquals(stack, expected_stack)

