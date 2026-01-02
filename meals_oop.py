from pprint import pprint

raw_meals = [
    {"name": " chicken burrito ", "meal_type": "lunch", "calories": "650"},
    {"name": "Oatmeal", "meal_type": "Breakfast", "calories": 350},
    {"name": "Salmon Bowl", "meal_type": "Dinner", "calories": "720"},
    {"name": "Protein Shake", "calories": "420"},
    {"name": " greek yogurt ", "meal_type": "breakfast", "calories": 180},
    {"name": "Steak", "meal_type": "Dinner", "calories": "800"},
]


class Meal:
    def __init__(self, name, meal_type, calories):
        self.name = str(name).strip().title()
        self.meal_type = str(meal_type).strip().title() if meal_type else "Other"
        self.calories = int(calories)


# Manager/Container class
class MealLog:
    def __init__(self, raw_meals):
        self.meals = []

        for each_meal in raw_meals:
            # Meal_type is missing so fetch that directly
            meal_type = each_meal.get("meal_type", "Other")

            meal = Meal(
                name=each_meal.get("name", ""),
                meal_type=meal_type,
                calories=each_meal.get("calories", 0),
            )
            self.meals.append(meal)

    def total_meals(self):
        return len(self.meals)

    def average_calories(self):
        return sum(meal.calories for meal in self.meals) / self.total_meals()

    def min_calories(self):
        return min(meal.calories for meal in self.meals)

    def max_calories(self):
        return max(meal.calories for meal in self.meals)

    def group_by_meal_type(self):
        groups = {}

        for m in self.meals:
            label = m.meal_type

            if label not in groups:
                groups[label] = []
            groups[label].append(m)
        return groups

    def summary_by_meal_type(self):
        groups = self.group_by_meal_type()

        for meal_type, meals in groups.items():
            count = len(meals)
            avg = sum(m.calories for m in meals) / count
            print(f"{meal_type}- Count:{count}, Avg Calories: {avg}")


log = MealLog(raw_meals)
for m in log.meals:
    print(m.name, "-", m.meal_type, "-", m.calories)

log = MealLog(raw_meals)
print("Total meals:", log.total_meals())
print("Average calories:", log.average_calories())

log = MealLog(raw_meals)
print("Total meals:", log.total_meals())
print("Average calories:", log.average_calories())
print("Min calories:", log.min_calories())
print("Max calories:", log.max_calories())
print()
log.summary_by_meal_type()
