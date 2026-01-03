raw_expenses = [
    {"item": " groceries ", "category": "food", "amount": "82.45"},
    {"item": "Gas", "category": "transportation", "amount": 45.00},
    {"item": "Netflix", "category": "Entertainment", "amount": "15.99"},
    {"item": "Rent", "category": "housing", "amount": "1200"},
    {"item": "Coffee", "amount": "4.75"},
    {"item": "Gym", "category": "health", "amount": 35},
]


class Expense:
    def __init__(self, item, category, amount):
        self.item = str(item).strip().title()
        self.category = str(category).strip().title() if category else "Other"
        self.amount = float(amount)


class ExpenseReport:
    def __init__(self, raw_expenses):
        self.expenses = []

        for expense in raw_expenses:
            expense = Expense(
                item=expense.get("item", ""),
                category=expense.get("category", "Other"),
                amount=expense.get("amount", 0.0),
            )
            self.expenses.append(expense)

    def total_expenses(self):
        return len(self.expenses)

    def total_spent(self):
        return sum(e.amount for e in self.expenses)

    def average_amount(self):
        return sum(e.amount for e in self.expenses) / self.total_expenses()

    def groups_by_category(self):
        groups = {}

        for c in self.expenses:
            label = c.category

            if label not in groups:
                groups[label] = []
            groups[label].append(c)
        return groups

    def summary_by_category(self):
        groups = self.groups_by_category()

        for category, expenses in groups.items():
            count = len(expenses)
            category_total = sum(e.amount for e in expenses)
            avg = category_total / count
            print(
                f"{category}-Count:{count}, Avg per category:${avg:.2f},Category total: ${category_total:;2f}"
            )
        print(f"Total Spent:${self.total_spent():.2f}")
