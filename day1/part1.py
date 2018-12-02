class Solver:

    def __init__(self):
        self.frequency = 0

    def solve(self, input_file):
        for i in input_file:
            self.frequency += int(i)

if __name__ == "__main__":

    with open("input.txt") as f:
        input_file = f.readlines()

    solver = Solver()
    solver.solve(input_file)

    print("Resulting Frequency: {}".format(solver.frequency))