import re

class Solver:
    def __init__(self):

        """
        self.sleeping_habits data structure

        {"guard_id": {
            "total_minutes_asleep": 0,
            "minutes_asleep": {
                    "minute": "times slept this minute"
                }
            }
        }
        """

        self.sleeping_habits = {}

    def solve(self, input_file):

        # Guard ID regex
        re_guard_id = re.compile(r"#\d*")

        # Hour:Minute regex
        re_hour_minute = re.compile(r"\d\d:\d\d")

        guard_on_duty = 0

        fell_asleep_minute = 0

        for i in sorted(input_file):

            # Get guard on duty
            guard_id = re_guard_id.search(i)
            if guard_id:
                guard_on_duty = guard_id.group(0).strip("#")

            # Get hour:minute
            minute = int(re_hour_minute.search(i).group(0).split(":")[-1])

            if "falls asleep" in i:
                fell_asleep_minute = minute

            if "wakes up" in i:
                minutes_asleep = minute - fell_asleep_minute

                if not guard_on_duty in self.sleeping_habits:
                    self.sleeping_habits[guard_on_duty] = {}
                    self.sleeping_habits[guard_on_duty]['total_minutes_asleep'] = minutes_asleep
                    time_asleep = {}
                else:
                    self.sleeping_habits[guard_on_duty]['total_minutes_asleep'] += minutes_asleep
                    time_asleep = self.sleeping_habits[guard_on_duty]['minutes_asleep']

                for i in range(fell_asleep_minute, minute):

                    if not i in time_asleep:
                        time_asleep[i] = 1
                    else:
                        time_asleep[i] += 1

                self.sleeping_habits[guard_on_duty]['minutes_asleep'] = time_asleep

    def make_output_part1(self):
    
        guard_id = 0
        total_minutes_asleep = 0
        
        for guard, value in self.sleeping_habits.items():
            if value['total_minutes_asleep'] > total_minutes_asleep:
                guard_id = guard
                total_minutes_asleep = value['total_minutes_asleep']
                
        # Get minute slept the most
        minutes_slept_most = self.sleeping_habits[guard_id]['minutes_asleep']
        
        minute_slept_most = 0
        total_times_slept = 0
        
        for minute, times in minutes_slept_most.items():
            if times > total_times_slept:
                minute_slept_most = minute
                total_times_slept = times

        return int(guard_id) * int(minute_slept_most)

    def make_output_part2(self):

        guard_id = 0
        minute_asleep = 0
        total_times_slept = 0

        for guard, value in self.sleeping_habits.items():

            for minute, times in value['minutes_asleep'].items():

                if times > total_times_slept:
                    total_times_slept = times
                    minute_asleep = minute
                    guard_id = guard

        return int(guard_id) * int(minute_asleep)

if __name__ == "__main__":

    with open("input.txt") as f:
        input_file = f.readlines()

    solver = Solver()
    solver.solve(input_file)

    print("Result: {}".format(solver.make_output_part1()))
    print("Most minute asleep: {}".format(solver.make_output_part2()))