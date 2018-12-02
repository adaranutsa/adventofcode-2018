from part1 import Solver

def test():
    test_cases = [
        {
            "case": ["+1","+1","+1"],
            "expected": 3
        },
        {
            "case": ["+1","+1","-2"],
            "expected": 0
        },
        {
            "case": ["-1","-2","-3"],
            "expected": -6
        }
    ]

    for test in test_cases:
        solver = Solver()
        solver.solve(test['case'])

        assert solver.frequency == test['expected'], "Expected: {} - Got: {}".format(test['expected'], solver.frequency)

if __name__ == "__main__":
    test()