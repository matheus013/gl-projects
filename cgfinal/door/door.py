class Door:
    def __init__(self, height, width, base_left, base_right, alpha, run, state):
        self.height = height
        self.width = width
        self.base_right = base_right
        self.base_left = base_left
        self.alpha = alpha
        self.run = run
        self.state = state

    def print(self):
        return self.height, self.width, self.base_left, self.base_right, self.alpha_left

    def run_reverse(self):
        self.run = not self.run

    def state_reverse(self):
        self.state = not self.state
