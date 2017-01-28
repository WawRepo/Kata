#from __future__ import absolute_import
from unittest import TestCase

from game import Game

class TestGame(TestCase):
    def testCreateGame(self):
        game = Game()
        self.assertEquals(1,2)
