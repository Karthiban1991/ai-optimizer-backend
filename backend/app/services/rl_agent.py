import random

class RLAgent:

    def decide(self):
        return random.choice(["scale_up", "scale_down", "none"])
