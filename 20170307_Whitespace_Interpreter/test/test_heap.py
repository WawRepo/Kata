from unittest import TestCase
from heap import *


class TestHeap(TestCase):
    def test_stack_to_heap(self):
        stack = [1, 2]
        heap = {}
        expected_heap = {1: 2}
        expected_stack = []
        stack_to_heap("dummy code", stack, heap)
        self.assertEquals(heap, expected_heap)
        self.assertEquals(stack, expected_stack)
        # IndexError exeption
        self.assertRaises(IndexError, lambda: stack_to_heap("dummy code", stack, heap))

    def test_heap_to_stack(self):
        stack = [2]
        heap = {2: 1}
        expected_stack = [1]
        expected_heap = {2: 1}
        heap_to_stack("dummy code", stack, heap)
        self.assertEquals(heap, expected_heap)
        self.assertEquals(stack, expected_stack)
        # IndexError exeption
        self.assertRaises(KeyError, lambda: heap_to_stack("dummy code", stack, heap))

    def test_heap_flow(self):
        # stack to heap
        code = 'snss'
        code_rdr = code_reader(code)
        stack = [1, 2]
        heap = {}
        expected_heap = {1: 2}
        heap_flow(code_rdr, stack, heap)
        self.assertEquals(heap, expected_heap)

        # heap to stack
        code = 'tnss'
        code_rdr = code_reader(code)
        stack = [2]
        heap = {2: 1}
        expected_stack = [1]
        expected_heap = {2: 1}
        heap_flow(code_rdr, stack, heap)
        self.assertEquals(heap, expected_heap)
        self.assertEquals(stack, expected_stack)
