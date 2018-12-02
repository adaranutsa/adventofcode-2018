from part1 import Solver

def test():
    test_cases = [
        {
            "case": [
                "abcdef",
                "bababc",
                "abbcde",
                "abcccd",
                "aabcdd",
                "abcdee",
                "ababab"
            ],
            "expected": 12
        }
    ]

    for test in test_cases:
        solver = Solver()
        solver.solve(test['case'])

        assert solver.get_checksum() == test['expected'], "Expected: {} - Got: {}".format(test['expected'], solver.get_checksum())

if __name__ == "__main__":
    test()