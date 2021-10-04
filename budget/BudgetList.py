from . import Expense
import matplotlib.pyplot as plt
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


    #Create an Interactor method
    def __iter__(self):
        self.iter_e  = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    #Method Next
    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()



#Main function    
def main():
     
    myBudgetList = BudgetList(1200)
    
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    # Test len()
    print('The count of all expenses: ' + str(len(myBudgetList)))
    
    #Test the Iterable
    for entry in myBudgetList:
        print (entry)
    
    #Create Figure and Axes
    fig, ax = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green','red','blue'])
    ax.set_title('Your total expenses v.s total budget')
    plt.show()




if __name__ == "__main__":
    main()