class Solver:

    """
    Puzzle: Loop through all numbers in the input.txt file
    over and over again until you find the first number
    after each addition/subtraction that occurs twice.
    """

    def __init__(self):
        self.frequency = None

    def solve(self, input_file):

        # {"frequency":"occurred count"}
        # The first frequency is 0
        occurred_frequencies = {0:1}

        running_frequency = 0

        while self.frequency == None:

            for i in input_file:
                running_frequency += int(i)

                occurred_frequencies[running_frequency] = occurred_frequencies[running_frequency] + 1 if occurred_frequencies.get(running_frequency) else 1

                if occurred_frequencies.get(running_frequency) == 2:
                    self.frequency = running_frequency
                    break

if __name__ == "__main__":

    with open("input.txt") as f:
        input_file = f.readlines()

    solver = Solver()
    solver.solve(input_file)

    print("First frequency occurring twice: {}".format(solver.frequency))