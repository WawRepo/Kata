from unittest import TestCase
from input_output import *


class TestInputOutput(TestCase):

    def test_stack_output_char(self):
        code = 'tnss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ""
        output = []

        expected_stack = []
        expected_output = ["a"]
        stack_output_char(code_rdr, stack, heap, inp, output)
        self.assertEquals(output, expected_output)
        self.assertEquals(stack, expected_stack)

        #from empty stack error
        self.assertRaises(IndexError, lambda: stack_output_char(code_rdr, stack, heap, inp, output))

    def test_stack_output_int(self):
        code = 'tnss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ""
        output = []

        expected_stack = []
        expected_output = [97]
        stack_output_int(code_rdr, stack, heap, inp, output)
        self.assertEquals(output, expected_output)
        self.assertEquals(stack, expected_stack)

        #from empty stack error
        self.assertRaises(IndexError, lambda: stack_output_int(code_rdr, stack, heap, inp, output))


    def test_input_char_heap(self):
        code = 'tnss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ['ab']
        output = []

        expected_stack = []
        expected_inp = ['b']
        expected_heap = {97: 97}
        input_char_heap(code_rdr, stack, heap, inp, output)
        self.assertEquals(heap, expected_heap)
        self.assertEquals(stack, expected_stack)
        self.assertEquals(inp, expected_inp)

        #from empty stack error
        self.assertRaises(IndexError, lambda: input_char_heap(code_rdr, stack, heap, inp, output))


    def test_input_int_heap(self):
        code = 'tnss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = "97".split("\n")
        output = []

        expected_stack = []
        expected_heap = {97: 97}
        input_int_heap(code_rdr, stack, heap, inp, output)
        self.assertEquals(heap, expected_heap)
        self.assertEquals(stack, expected_stack)

       # from empty stack error
        self.assertRaises(IndexError, lambda: input_int_heap(code_rdr, stack, heap, inp, output))

    def test_input_output_flow(self):
        #char output
        code = 'ssnss'
        code_rdr = code_reader(code)

        stack = [97]
        heap = {}
        inp = ""
        output = []
        expected_stack = []
        expected_output = ["a"]
        input_output_flow(code_rdr, stack, heap, inp, output)
        self.assertEquals(output, expected_output)
        self.assertEquals(stack, expected_stack)

        #int output
        code = 'stss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ""
        output = []

        expected_stack = []
        expected_output = [97]
        input_output_flow(code_rdr, stack, heap, inp, output)
        self.assertEquals(output, expected_output)
        self.assertEquals(stack, expected_stack)

        #input to char heap
        code = 'tsss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ['ab']
        output = []

        expected_stack = []
        expected_heap = {97: 97}
        input_output_flow(code_rdr, stack, heap, inp, output)
        self.assertEquals(heap, expected_heap)
        self.assertEquals(stack, expected_stack)


        #input to char heap
        code = 'ttss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = "97".split("\n")
        output = []

        expected_stack = []
        expected_heap = {97: 97}
        input_output_flow(code_rdr, stack, heap, inp, output)
        self.assertEquals(heap, expected_heap)
        self.assertEquals(stack, expected_stack)