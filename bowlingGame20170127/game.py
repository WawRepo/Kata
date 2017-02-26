class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if self.rollValidateVsFrameStatus(pins):
            self.rolls.append(pins)
            return pins

    def splitIntoFrames(self):
        frames = []
        frame = []
        for roll in self.rolls:
            if len(frames) == 9:
                if len(frame) < 2:
                    frame.append(roll)
                elif len(frame) == 2 and (sum(frame) == 10 or frame[1]==10):
                    frame.append(roll)
                    frames.append(frame)
                elif len(frame) == 2 and not(sum(frame) == 10 or frame[1] == 10):
                    frames.append(frame)
            elif len(frames) < 9:
                if roll == 10:
                    frame.append(roll)
                    frames.append(frame)
                    frame = []
                else:
                    frame.append(roll)
                    if len(frame) == 2:
                        frames.append(frame)
                        frame =[]

        if len(frame) == 1:
            frames.append(frame)
        return frames

    def rollValidateVsFrameStatus(self,pins):
        frames = self.splitIntoFrames()
        if len(frames) < 10:
            if pins >= 0 and pins <= 10:
                if len(frames[-1]) == 2:
                    return True
                elif len(frames[-1]) == 1 and frames[-1][0] + pins <= 10:
                    return True
                else:
                    return False
            else:
                return False



    def Score(self):
        score = 0
        for roll in self.rolls:
            score += roll
        return score
