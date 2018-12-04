class Solver:

    """Puzzle: Given the size of the fabric and the input (claims to the fabric),
    find how many square inches of fabric has multiple claims to it.

    In other words, based on the input, how many of the inputs overlap the same
    area in the grid at least twice. Grab that number and return the sq inches.
    """

    def __init__(self, grid_size):

        # Create the grid
        self.grid = []
        self.make_grid(self.grid, grid_size)

        # List of processed IDs
        self.ids = []

    def make_grid(self, place, length):
        """
        Create the grid in a specific variable and
        with a specific size
        
        :param place: The variable to create the grid in
        :type place: list variable
        :param length: The size of the grid. It creates a square. If 10 is passed, it creates a 10x10 grid
        :type length: int
        """

        place[:] = [["."] * length for _ in range(length)]

    def print_grid(self):
        """
        Print the grid to the screen
        """

        for x in self.grid:
            for y in x:
                print("{}\t".format(y), end="")
            print("\n")

    def make_output_part1(self):
        """
        Create the output for part 1 of how many sq in are being overlapped at least twice.
        """

        # Starting position
        sx, sy = 0,0

        # Ending position
        ex, ey = (len(self.grid[0])-1, len(self.grid)-1)

        square_inches = 0

        while sy <= ey and sx <= ex:
            if len(self.grid[sy][sx]) > 1:
                square_inches += 1

            # Increment the x axis
            sx += 1

            # If x axis reaches the end,
            # step down 1 on the y axis
            if sx > ex:

                # Reset the starting position of the x axis
                sx = 0
                sy += 1

        return square_inches

    def make_output_part2(self):
        """
        Create output for part 2 of which ID doesn't overlap with any others.
        """

        # Starting position
        sx, sy = 0,0

        # Ending position
        ex, ey = (len(self.grid[0])-1, len(self.grid)-1)

        overlapping_ids = []

        while sy <= ey and sx <= ex:
        
            value = self.grid[sy][sx]
            
            if value == ".":
                sx += 1
            
                if sx > ex:
                    sx = 0
                    sy += 1
                continue

            # Only keep track of overlapping values
            if type(value) == list and len(value) >= 2:
                for v in value:
                    if int(v) not in overlapping_ids:
                        overlapping_ids.append(int(v))
            
            sx += 1
            
            if sx > ex:
                sx = 0
                sy += 1

        return list(set(sorted(self.ids)) - set(sorted(overlapping_ids)))[0]
    
    def solve(self, input_file):
        """
        Loop through the list of instructions, extract the details,
        and traverse the grid, laying claim to the fabric

        :param input_file: List of instructions from an input file
        :type input_file: list
        """
        
        for i in input_file:
            claim, start_pos, end_pos = self.extract_instr_details(i.strip())

            self.ids.append(int(claim))

            self.traverse_grid(claim, start_pos, end_pos)

    def perform_action(self, claim, current_value):
        """
        Perform an action on the grid based on the value
        of the grid item

        :param claim: The claim number for this instruction
        :type claim: str/int
        :param current_value: The current value of the grid item
        :type current_value: str
        """

        # No claim has been laid
        if current_value == ".":
            return current_value.append(claim)

        # Multiple claims exist, return X to mark claim overlap
        else:
            current_value.append(claim)

    def traverse_grid(self, claim, start_pos, end_pos):
        """
        Traverse the grid and lay claim to a piece of Santa's fabric

        :param claim: The claim number
        :type claim: int
        :param start_pos: Starting position on the grid
        :type start_pos: tuple
        :param end_pos: Ending position on the grid
        :type end_pos: tuple
        """

        # Starting position
        sx, sy = start_pos

        # Ending position
        ex, ey = end_pos

        while sy <= ey and sx <= ex:

            if self.grid[sy][sx] == ".":
                self.grid[sy][sx] = [claim]
            else:
                self.grid[sy][sx].append(claim)

            # Increment the x axis
            sx += 1

            # If x axis reaches the end,
            # step down 1 on the y axis
            if sx > ex:

                # Reset the starting position of the x axis
                sx = start_pos[0]
                sy += 1

    def get_claim(self, instr):
        """
        Extract and return the claim ID
        
        :param instr: Current instruction split into a list
        :type instr: list
        """
        
        return instr[0].split("#")[-1]
        
    def get_start_pos(self, instr):
        """
        Extract and return a tuple of the starting position
        
        :param instr: Current instruction split into a list
        :type instr: list
        """
        
        pos_list = instr[2].strip(":").split(",")
        
        return tuple(map(lambda x: int(x), pos_list))

    def get_end_pos(self, instr):
        """
        Extract and return a tuple of the area to cover
        
        :param instr: Current instruction split into a list
        :type instr: list
        """
        
        area_list = instr[-1].split("x")
        
        return tuple(map(lambda x: int(x), area_list))

    def extract_instr_details(self, instruction):
        """
        Extract the details of a single instruction (claim, start/end pos)
        
        :param instruction: A string containing the claim instructions
        :type instruction: str
        """
        
        to_list = instruction.split(" ")
        
        claim = self.get_claim(to_list)
        start_pos = self.get_start_pos(to_list)
        end_pos = tuple(s1 + (s2 - 1) for s1, s2 in zip(start_pos, self.get_end_pos(to_list)))

        return (claim, start_pos, end_pos)

if __name__ == "__main__":

    with open("input.txt") as f:
        input_file = f.readlines()

    solver = Solver(1000)
    solver.solve(input_file)

    print("Overlapping sq in: {}".format(solver.make_output_part1()))
    print("Non-overlapping ID: {}".format(solver.make_output_part2()))