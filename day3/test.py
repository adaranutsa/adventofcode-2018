from main import Solver

test_cases = [
    {
        "case": [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2"
        ],
        "expected_part1": 4,  # Answer is sq inches
        "expected_part2": 3
    }
]

if __name__ == "__main__":

    for test in test_cases:
        solver = Solver(12)
        solver.solve(test['case'])

        solver.print_grid()

        assert solver.make_output_part1() == test['expected_part1'], "Expected Part 1: {} - Got: {}".format(test['expected_part1'], solver.make_output_part1())
        assert solver.make_output_part2() == test['expected_part2'], "Expected Part 2: {} - Got: {}".format(test['expected_part2'], solver.make_output_part2())