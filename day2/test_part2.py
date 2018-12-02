from part2 import Solver

def test():
    test_cases = [
        {
            "case": [
                "abcde",
                "fghij",
                "klmno",
                "pqrst",
                "fguij",
                "axcye",
                "wvxyz",
                "fgahj",
                "fgujj"
            ],
            "expected": "fgij"
        }
    ]

    for test in test_cases:
        solver = Solver()
        solver.solve(test['case'])

        assert solver.make_output() == test['expected'], "Expected: {} - Got: {}".format(test['expected'], solver.make_output())

if __name__ == "__main__":
    test()