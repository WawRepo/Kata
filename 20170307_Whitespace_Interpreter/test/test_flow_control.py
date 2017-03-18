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

        flow_control_exit(code_rdr, stack, heap, inp, output)
        self.assertRaises(StopIteration, lambda: code_rdr.next())


