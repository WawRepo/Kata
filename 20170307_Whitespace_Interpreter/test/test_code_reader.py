from unittest import TestCase
from code_reader import *


class TestCodeReader(TestCase):

    def test_code_read_next(self):
        code = 'tnss'
        code_rdr = code_reader(code)

        self.assertEquals('t', code_rdr.next())
        self.assertEquals('n', code_rdr.next())
        self.assertEquals('s', code_rdr.next())
        self.assertEquals('s', code_rdr.next())

        self.assertRaises(StopIteration, lambda: code_rdr.next())

    def test_code_read_position(self):
        code = 'tnss'
        code_rdr = code_reader(code)

        code_rdr.next()
        self.assertEquals(1, code_rdr.position())
        code_rdr.next()
        self.assertEquals(2, code_rdr.position())
        code_rdr.next()
        self.assertEquals(3, code_rdr.position())

    def test_code_read_move(self):
        code = 'tnss'
        code_rdr = code_reader(code)

        code_rdr.move(1)
        self.assertEquals(1, code_rdr.position())

        code_rdr.move(3)
        self.assertEquals(3, code_rdr.position())

        self.assertRaises(IndexError, lambda: code_rdr.move(-1))
        self.assertRaises(IndexError, lambda: code_rdr.move(99))
        self.assertRaises(IndexError, lambda: code_rdr.move(4))

    def test_iterator(self):
        code = 'tnss'
        code_rdr = code_reader(code)

        for c in code_rdr:
            print c