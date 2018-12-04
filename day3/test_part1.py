from part1 import Solver

test_cases = [
    {
        "case": [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
            "#4 @ 3,2: 5x4",
            "#5 @ 1,6: 2x2"
        ],
        "expected": 18 # Answer is sq inches
    }
]

if __name__ == "__main__":

    for test in test_cases:
        solver = Solver(12)
        solver.solve(test['case'])

        solver.print_grid()

        assert solver.make_output_part1() == test['expected'], "Expected: {} - Got: {}".format(test['expected'], solver.make_output_part1())