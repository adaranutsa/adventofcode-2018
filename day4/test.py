from main import Solver

test_cases = [
    {
        "case": ["[1518-11-01 00:00] Guard #10 begins shift",
            "[1518-11-01 00:05] falls asleep",
            "[1518-11-01 00:25] wakes up",
            "[1518-11-01 00:30] falls asleep",
            "[1518-11-01 00:55] wakes up",
            "[1518-11-01 23:58] Guard #99 begins shift",
            "[1518-11-02 00:40] falls asleep",
            "[1518-11-02 00:50] wakes up",
            "[1518-11-03 00:05] Guard #10 begins shift",
            "[1518-11-03 00:24] falls asleep",
            "[1518-11-03 00:29] wakes up",
            "[1518-11-04 00:02] Guard #99 begins shift",
            "[1518-11-04 00:36] falls asleep",
            "[1518-11-04 00:46] wakes up",
            "[1518-11-05 00:03] Guard #99 begins shift",
            "[1518-11-05 00:45] falls asleep",
            "[1518-11-05 00:55] wakes up"
        ],
        "expected_part1": 240,
        "expected_part2": 4455
    }
]

if __name__ == "__main__":

    for test in test_cases:
        solver = Solver()
        solver.solve(test['case'])

        assert solver.make_output_part1() == test['expected_part1'], "Expected: {} - Got: {}".format(test['expected_part1'], solver.make_output_part1())
        assert solver.make_output_part2() == test['expected_part2'], "Expected: {} - Got: {}".format(test['expected_part2'], solver.make_output_part2())