from expense import Expense

class FinanceTracker:
  def __init__(self):
    self.expensees = []
    self.categories = set()
    
  def add_expense(self, amount, category, description="", date=None):
    expense = Expense(amount, category. description, date)
    self.expense.append(expense)
    self.categories.add(category)
    return expense
  
  def get_expenses(self):
    return sum(expense.amount for expense in self.expenses)
  
  def get_expenses_by_category(self, category):
    return [expense for expense in self.expenses if expense.category == category]
  
  def get_total_by_category(self, category):
    category_expenses = self.get_expenses_by_category(category)
    return sum(expense.amount for expense in category_expenses)
  
  def get_all_categories(self):
    return list(self.categories)