class Game:
    def __init__(self):
        self.rolls = []

    def Roll(self, pins):
        if pins >= 0 and pins <= 10:
            self.rolls.append(pins)
            return pins

    def SplitIntoFrames(self):
        frames = []
        frame = []
        for roll in self.rolls:
            if roll == 10:
                frame.append(roll)
                frames.append(frame)
                frame = []
            else:
                frame.append(roll)
                if len(frame) == 2:
                    frames.append(frame)
                    frame =[]

        if len(frame) > 0:
            frames.append(frame)
        return frames

    def Score(self):
        score = 0
        for roll in self.rolls:
            score += roll
        return score
