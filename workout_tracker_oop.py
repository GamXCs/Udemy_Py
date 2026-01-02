raw_workouts = [
    {"exercise": " bench press ", "muscle": "chest", "sets": "4"},
    {"exercise": "Squat", "muscle": "Legs", "sets": 5},
    {"exercise": "deadlift", "muscle": "legs", "sets": "3"},
    {"exercise": "Pull Up", "muscle": "Back", "sets": "4"},
    {"exercise": "Bicep Curl", "sets": 3},
    {"exercise": "Row", "muscle": "back", "sets": "4"},
]


class Workout:
    def __init__(self, exercise, muscle, sets):
        self.exercise = str(exercise).strip().title()
        self.muscle = str(muscle).strip().title() if muscle else "Other"
        self.sets = int(sets)


class WorkoutLog:
    def __init__(self, raw_workouts):
        self.workouts = []

        for workout in raw_workouts:
            muscle = workout.get("muscle", "Other")

            workout = Workout(
                exercise=workout.get("exercise", ""),
                muscle=muscle,
                sets=workout.get("sets", 0),
            )
            self.workouts.append(workout)

    def total_workouts(self):
        return len(self.workouts)

    def average_sets(self):
        return sum(s.sets for s in self.workouts) / self.total_workouts()

    def min_sets(self):
        return min(s.sets for s in self.workouts)

    def max_sets(self):
        return max(s.sets for s in self.workouts)

    def group_by_muscle(self):
        groups = {}

        for w in self.workouts:
            label = w.muscle

            if label not in groups:
                groups[label] = []
            groups[label].append(w)
        return groups

    def summary_by_muscle(self):
        groups = self.group_by_muscle()

        for muscle, workouts in groups.items():
            count = len(workouts)
            avg = sum(w.sets for w in workouts) / count
            print(f"{muscle} - Count:{count}, Avg Set:{avg}")


log = WorkoutLog(raw_workouts)
log.summary_by_muscle()
