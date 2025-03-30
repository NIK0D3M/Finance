from datetime import datetime

class Expense:
  def __init__(self, amount, category, description="", date=None):
    self.amount = float(amount)
    self.category = category
    self.description = description
    self.date = date if date else datetime.now()
    
  def __str__(self):
    return f"{self.date.strftime('%Y-%m-%d')} | ${self.amount:.2f} | {self.category} | {self.description}"