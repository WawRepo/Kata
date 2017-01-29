from unittest import TestCase

from game import Game

class TestGame(TestCase):

    def testRoll(self):
        game = Game()
        game.Roll(1)

    def testRollSize(self):
        game = Game()
        self.assertEquals(game.Roll(1) , 1)

        self.assertIsNone(game.Roll(-1))
        self.assertIsNone(game.Roll(11))

    def testScore(self):
        game = Game()
        self.assertEquals(0,game.Score())
        game.Roll(1)
        self.assertEquals(1,game.Score())

    def roolMany(self,game,pins,n):
        for i in range(0,n,1):
            game.Roll(pins)

    def testRollMultipleSamePinsNo(self ):
        sameRoll = [0,1,2,3,4]
        for pins in sameRoll:
            game = Game()
            self.roolMany(game,pins,20)
            self.assertEquals(20*pins, game.Score())

    def testSplitIntoFrames(self):
        game = Game()
        game.Roll(1)
        self.assertListEqual([[1]],game.SplitIntoFrames())
        game.Roll(3)
        self.assertListEqual([[1,3]], game.SplitIntoFrames())
        game.Roll(10)
        self.assertListEqual([[1, 3],[10]], game.SplitIntoFrames())
        game.Roll(1)
        self.assertListEqual([[1, 3], [10],[1]], game.SplitIntoFrames())


    # def testStrike(self):
    #     game = Game()
    #     game.Roll(5)
    #     game.Roll(5)
    #     game.Roll(3)
    #     self.assertEquals(16, game.Score())
    #
    # def testImproperThrows(self):
    #     game = Game()
    #     game.Roll(5)
    #     self.assertIsNone(game.Roll(6))

