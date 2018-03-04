class TransitionClock:

    def __init__(self):
        self.clock = 0

    def tick(self):
        self.clock += 1

    def transition(self, frame_duration):
        return self.clock % frame_duration == 0
