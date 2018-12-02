class Solver:
    
    def __init__(self):

        self.two_letter_boxes = 0
        self.three_letter_boxes = 0

    def solve(self, input_file):
        """
        Execute steps to solve the puzzle
        
        :param input_file: List of lines from the input file
        :type input_file: list
        """
        
        for i in input_file:
            num_of_letters = self.count_letters(i)

            self.validate_box(num_of_letters)

    def count_letters(self, string):
        """
        Count the number of letters in a string

        :param string: Input string
        :type string: str
        """
        
        letter_count = {}

        for s in string:
            letter_count[s] = letter_count.get(s) + 1 if letter_count.get(s) else 1

        return letter_count

    def validate_box(self, letters):
        """
        Check if this box contains exactly two of any letter 
        or exactly three of any letter

        :param letters: Dict of letter occurances
        :type letters: dict
        """
        
        if 2 in letters.values():
            self.two_letter_boxes += 1

        if 3 in letters.values():
            self.three_letter_boxes += 1

    def get_checksum(self):
        """
        Return the checksum from the list of box IDs
        """

        return self.two_letter_boxes * self.three_letter_boxes

if __name__ == "__main__":

    with open("input.txt") as f:
        input_file = f.readlines()

    solver = Solver()
    solver.solve(input_file)

    print("Resulting Checksum: {}".format(solver.get_checksum()))