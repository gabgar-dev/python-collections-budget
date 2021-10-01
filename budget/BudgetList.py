from . import Expense

# Class
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    def __len__(self):
        return (len(self.expenses) + len(self.overages))

    # Append
    def append(self, item):
        
        if (self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
       
        else:
            self.overages.append(item)
            self.sum_overages+=item


#Main function    
def main():
     
    myBudgetList = BudgetList(1200)
    
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    # Test len()
    print('The count of all expenses: ' + str(len(myBudgetList)))
    

if __name__ == "__main__":
    main()