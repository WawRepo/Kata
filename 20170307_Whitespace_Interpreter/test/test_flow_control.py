from unittest import TestCase
from flow_control import *


class TestFlowControl(TestCase):

    def test_flow_control_exit(self):
        code = 'tnss'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ""
        output = []
        labels = {}
        return_address = []
        flow_control_exit(code_rdr, stack, heap, inp, output, labels, return_address)
        self.assertRaises(StopIteration, lambda: code_rdr.next())


    def  test_empty_label_creation(self):
        code = 'n'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ""
        output = []
        labels = {}
        return_address = []
        flow_control_mark_label(code_rdr, stack, heap, inp, output, labels, return_address)

        expected_labels = {'': 1}

        self.assertDictEqual(expected_labels, labels)

    def test_non_label_creation(self):
        code = 'ststn'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ""
        output = []
        labels = {}
        return_address = []
        flow_control_mark_label(code_rdr, stack, heap, inp, output, labels, return_address)

        expected_labels = {'stst': 5}

        self.assertDictEqual(expected_labels, labels)

    def test_same_lanel_error(self):
        code = 'ststn'
        code_rdr = code_reader(code)
        stack = [97]
        heap = {}
        inp = ""
        output = []
        labels = {'stst': 5}
        return_address = []

        self.assertRaises(KeyError, lambda: flow_control_mark_label(code_rdr, stack, heap, inp, output, labels, return_address))


    def test_call_subroutine(self):
        code = 'ststnstst'
        code_rdr = code_reader(code)
        stack = []
        heap = {}
        inp = ""
        output = []
        labels = {'stst': 1}
        return_address = []

        expected_position = 1
        expected_return_address = [5]

        flow_control_call_subroutine(code_rdr, stack, heap, inp, output, labels, return_address)

        self.assertEquals(expected_position, code_rdr.position())
        self.assertListEqual(expected_return_address, return_address)

    def test_jump_unconditionally(self):

        code = 'ststnstst'
        code_rdr = code_reader(code)
        stack = []
        heap = {}
        inp = ""
        output = []
        labels = {'stst': 1}
        return_address = []

        expected_position = 1
        expected_return_address = []

        flow_control_jump_unconditionally(code_rdr, stack, heap, inp, output, labels, return_address)

        self.assertEquals(expected_position, code_rdr.position())
        self.assertListEqual(expected_return_address, return_address)

    def test_jump_if_zero_on_stack(self):
        code = 'ststnstst'
        code_rdr = code_reader(code)
        stack = [1]
        heap = {}
        inp = ""
        output = []
        labels = {'stst': 1}
        return_address = []
        expected_position = 5

        flow_control_jump_if_zero_stack(code_rdr, stack, heap, inp, output, labels, return_address)

        self.assertEquals(expected_position, code_rdr.position())

        code_rdr = code_reader(code)
        stack = [0]
        expected_position = 1

        flow_control_jump_if_zero_stack(code_rdr, stack, heap, inp, output, labels, return_address)

        self.assertEquals(expected_position, code_rdr.position())

    def test_jump_if_less_than_zero_on_stack(self):
        code = 'ststnstst'
        code_rdr = code_reader(code)
        stack = [1]
        heap = {}
        inp = ""
        output = []
        labels = {'stst': 1}
        return_address = []
        expected_position = 5

        flow_control_jump_if_less_zero_stack(code_rdr, stack, heap, inp, output, labels, return_address)

        self.assertEquals(expected_position, code_rdr.position())

        code_rdr = code_reader(code)
        stack = [-1]
        expected_position = 1

        flow_control_jump_if_less_zero_stack(code_rdr, stack, heap, inp, output, labels, return_address)

        self.assertEquals(expected_position, code_rdr.position())

    def test_ext_subroutine(self):
        code = 'ststnstst'
        code_rdr = code_reader(code)
        stack = [1]
        heap = {}
        inp = ""
        output = []
        labels = {'stst': 1}
        return_address = [1]

        expected_position = 1
        expected_return_address =[]

        flow_control_exit_subroutine(code_rdr, stack, heap, inp, output, labels, return_address)

        self.assertEquals(expected_position, code_rdr.position())
        self.assertListEqual(expected_return_address, return_address)