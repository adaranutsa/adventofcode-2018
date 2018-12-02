from difflib import SequenceMatcher

class Solver:

    """
    Puzzle: There are 2 box IDs (using input.txt) that differ by only
    1 letter in the same position. Find those 2 box IDs and return
    the common letters between them (removing the different letter).
    """
    
    def __init__(self):

        self.correct_boxes = []
        self.similarity_ratio = 0

    def solve(self, input_file):
        """
        Loop through the list of box IDs and compare each one.

        Looping is done using a pointer approach.

        pointer1 refers to the first item in the list to compare
        pointer2 moves down the list comparing each item to the first
        
        :param input_file: List of lines from the input file
        :type input_file: list
        """
        
        pointer1 = 0
        pointer2 = 1

        while pointer1 < len(input_file) - 2:

            if pointer2 >= len(input_file) - 1:
                pointer1 += 1
                pointer2 = pointer1 + 1

            results = self.similar(input_file[pointer1].strip(), input_file[pointer2].strip())

            if results > self.similarity_ratio:
                self.similarity_ratio = results
                self.correct_boxes = [input_file[pointer1].strip(), input_file[pointer2].strip()]

            pointer2 += 1

    def similar(self, string1, string2):
        """
        Get the similarity ratio between two strings

        :param string1: Input string 1
        :type string1: str
        :param string2: Input string 2
        :type string2: str
        """

        return SequenceMatcher(None, string1, string2).ratio()

    def make_output(self):
        """
        Generate the output by checking which letters are similar
        between the two correct boxes and returning them.
        """

        string1 = self.correct_boxes[0]
        string2 = self.correct_boxes[1]

        similar_letters = ""

        index = 0

        while index < len(string1):

            if string1[index] == string2[index]:
                similar_letters += string1[index]

            index += 1

        return similar_letters

if __name__ == "__main__":

    with open("input.txt") as f:
        input_file = f.readlines()

    solver = Solver()
    solver.solve(input_file)

    print("Similar Letters: {}".format(solver.make_output()))