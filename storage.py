import json
from datetime import datetime
from expense import Expense

class Storage:
  def __init__(self, filename="expense.json"):
    self.filename = filename
    
  def save_expenses(self, expenses):
    # Convert expenses to a format that can be serialized to JSON
    expenses_data = []
    for expense in expenses:
      expenses_data.append({
        'amount': expense.amount,
        'category': expense.category,
        'description': expense.description,
        'date': expense.date.strftime('%Y-%m-%d %H:%M:%S')
      })
    
    # Write to file
    with open(self.filename, 'w') as file:
      json.dump(expenses_data, file, indent=4)
      
  def load_expenses(self):
      try:
          with open(self.filename, 'r') as file:
            expenses_data = json.load(file)
            
          # Convert JSON data back to Expense objects
          expenses = []
          for expenses_data in expenses_data:
              expense = Expense(
                amount=expenses_data['amount'],
                category=expenses_data['category'],
                description=expenses_data['description'],
                date=datetime.strptime(expenses_data['date'], '%Y-%m-%d %H:%M:%S')
              )
              expenses.append(expense)
          return expenses
      except (FileNotFoundError, json.JSONDecodeError):
        
        return[]
              
      