from part2 import Solver

def test():
    test_cases = [
        {
            "case": ["+1","-1"],
            "expected": 0
        },
        {
            "case": ["+3", "+3", "+4", "-2", "-4"],
            "expected": 10
        },
        {
            "case": ["-6", "+3", "+8", "+5", "-6"],
            "expected": 5
        },
        {
            "case": ["+7", "+7", "-2", "-7", "-4"],
            "expected": 14
        }
    ]

    for test in test_cases:
        solver = Solver()
        solver.solve(test['case'])

        assert solver.frequency == test['expected'], "Expected: {} - Got: {}".format(test['expected'], solver.frequency)

if __name__ == "__main__":
    test()