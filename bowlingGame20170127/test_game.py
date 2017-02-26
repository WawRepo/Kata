from unittest import TestCase

from game import Game

class TestGame(TestCase):

    def testRoll(self):
        game = Game()
        game.roll(1)

    def testRollSize(self):
        game = Game()
        self.assertEquals(game.roll(1), 1)

        self.assertIsNone(game.roll(-1))
        self.assertIsNone(game.roll(11))

    def testScore(self):
        game = Game()
        self.assertEquals(0,game.Score())
        game.roll(1)
        self.assertEquals(1,game.Score())

    def roolMany(self,game,pins,n):
        for i in range(0,n,1):
            game.roll(pins)

    def testRollMultipleSamePinsNo(self ):
        sameRoll = [0,1,2,3,4]
        for pins in sameRoll:
            game = Game()
            self.roolMany(game,pins,20)
            self.assertEquals(20*pins, game.Score())

    def testSplitIntoFrames(self):
        game = Game()
        game.roll(1)
        self.assertListEqual([[1]], game.splitIntoFrames())
        game.roll(3)
        self.assertListEqual([[1,3]], game.splitIntoFrames())
        game.roll(10)
        self.assertListEqual([[1, 3],[10]], game.splitIntoFrames())
        game.roll(1)
        self.assertListEqual([[1, 3], [10],[1]], game.splitIntoFrames())

    def testSplitIntoFrames10thFrame(self):
        game = Game()
        self.roolMany(game, 1, 18)

        nineFrames = []
        for i in range(0, 9, 1 ):
            nineFrames.append([1,1])

        self.assertListEqual(nineFrames, game.splitIntoFrames())

        game.roll(10)
        game.roll(10)
        game.roll(10)

        tenFrames = list(nineFrames)
        tenFrames.append([10,10,10])

        self.assertListEqual(tenFrames, game.splitIntoFrames())


        # def testStrike(self):
    #     game = Game()
    #     game.Roll(5)
    #     game.Roll(5)
    #     game.Roll(3)
    #     self.assertEquals(16, game.Score())
    #
    def testImproperThrows(self):
        game = Game()
        game.roll(5)
        self.assertIsNone(game.roll(6))

