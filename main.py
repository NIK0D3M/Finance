from tracker import FinanceTracker
from storage import Storage
from datetime import datetime

def print_menu():
  print("\n===== Personal Finance Tracker =====")
  print("1. Add Expense")
  print("2. View All Expenses")
  print("3. View Expenses by Category")
  print("4. View Spending Summary")
  print("5. Exit")
  print("===================================")
  
def get_valid_amount():
  while True:
      try:
        amount = float(input("Amount: $"))
        if amount <= 0:
          print ("Amount must be positive.")
          continue
        return amount 
      except ValueError:
        print("Please enter a valid number.")
        
def main():
  storage = Storage()
  tracker = FinanceTracker()
  
  expenses = storage.load_expenses()
  for expense in expenses:
    tracker.add_expense(
      expense.amount,
      expense.category,
      expense.description,
      expense.date
    )
    
  while True:
    print_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
      # Add Expense
      print("\n--- Add New Expense ---")
      amount = get_valid_amount()
      category = input("Category: ")
      description = input("Description (optional): ")
      
      date_input = input("Date (YYYY-MM-DD) or leave blank for today: ")
      date = None
      if date_input:
        try:
          date = datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
          print("Invalid date format. Using today's date.")
          
      tracker.add_expense(amount,category,description,date)
      storage.save_expenses(tracker.get_expenses())
      print("Expenses added successfully!")
      
    elif choice == '2':
      # View all Expenses
      print("\n--- All Expenses ---")
      expenses = tracker.get_expenses()
      if not expenses:
        print("No expenses recorded yet.")
      else: 
        for i, expense in enumerate(expenses, 1):
          print(f"{i}. {expense}")
        print(f"\nTotal: ${tracker.get_total_expenses():.2f}")
        
    elif choice ==  '3':
      
      categories = tracker.get_all_categories()
      if not categories:
        print("\nNo expenses recorded yet.")
        continue
      
      print("\n--- Categories ---")
      for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
        
      try:
        cat_idx = int(input("\nSelect category number: ")) - 1
        if 0 <= cat_idx < len(categories):
          selected_category = categories[cat_idx]
          print(f"\n--- Expenses in {selected_category} ---")
          cat_expenses = tracker.get_expenses_by_category(selected_category)
          for i, expense in enumerate(cat_expenses, 1):
            print(f"\nTotal for {selected_category}: ${tracker.get_total_by_category(selected_category):.2f}")
        else:
          print("Invalid selection.")
      except ValueError:
        print("Please enter a valid number.")
        
    elif choice == '4':
      
      print("\n--- Spending Summary ---")
      categories = tracker.get_all_categories()
      if not categories:
        print("No expenses recorded yet.")
        continue
      
      total = tracker.get_total_expenses()
      print(f"Total Spending: ${total:.2f}\n")
      
      print("Breakdown by Category:")
      for category in categories:
        cat_total = tracker.get_total_by_category(category)
        percentage = (cat_total / total) * 100 if total > 0 else 0
        print(f"{category}: ${cat_total:.2f} ({percentage:.1f}%)")
        
    elif choice == '5':
      print("\nThank you for using Personal Finance Tracker!")
      break
    
    else:
      print("Invalid choice. Please try again.")
      
if __name__ == "__main__":
  main()