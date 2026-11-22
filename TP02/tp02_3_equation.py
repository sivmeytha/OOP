class EquationCalculator:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def calculate_x(self):
        return self.z - self.y