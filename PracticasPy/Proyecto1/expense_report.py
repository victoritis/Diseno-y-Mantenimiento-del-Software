import locale
from enum import Enum, unique, auto
from datetime import datetime
from typing import List


@unique
class ExpenseType(Enum):
    DINNER = auto()
    BREAKFAST = auto()
    CAR_RENTAL = auto()


class Expense:
    type: ExpenseType
    amount: int


class ExpenseReport:
    def print_report(self, expenses: List[Expense]):
        report_str = ''

        total = 0
        meals = 0
        # TODO: reemplazar con datetime.now

        report_str += f"Expense Report {datetime(2023, 10, 3)}\n"

        for expense in expenses:
            if expense.type == ExpenseType.DINNER or expense.type == ExpenseType.BREAKFAST:
                meals += expense.amount

            name = ""
            if expense.type == ExpenseType.DINNER:
                name = "Dinner"
            elif expense.type == ExpenseType.BREAKFAST:
                name = "Breakfast"
            elif expense.type == ExpenseType.CAR_RENTAL:
                name = "Car Rental"

            meal_over_expenses_marker = "X" if expense.type == ExpenseType.DINNER and expense.amount > 5000 or expense.type == ExpenseType.BREAKFAST and expense.amount > 1000 else " "
            report_str += f"{name} \t {expense.amount} \t {meal_over_expenses_marker}\n"
            total += expense.amount

        report_str += f"Meals: {meals}\n"
        report_str += f"total: {total}\n"


