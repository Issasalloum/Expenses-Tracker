expenses = []

print('-----------------------------------')
print('Expense Tracker')
print('-----------------------------------')


def add_expense():
    expense_name = input('Enter expense name: ')
    amount = float(input('Enter amount: '))
    category = input('Enter category: ')
    date = input('Enter date (YYYY/MM/DD): ')

    new_expense = {
        'name': expense_name,
        'amount': amount,
        'category': category,
        'date': date
    }

    expenses.append(new_expense)
    print('Expense added successfully!')
def show_expense():
    if not expenses:
        print('No expenses yet!')
    else:
        for expense in expenses:
            print('--------------------')
            print(f"Name: {expense['name']}")
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Date: {expense['date']}")
            print('--------------------')
            
def search_expenses():
    if not expenses:
        print('no expenses to search!')
    else:
        search = input('enter expense name to search: ')
        found = False
        for expense in expenses:
            if search == expense['name']:
                print('--------------------')
                print(f"Name: {expense['name']}")
                print(f"Amount: {expense['amount']}")
                print(f"Category: {expense['category']}")
                print(f"Date: {expense['date']}")
                print('--------------------')
                found = True
        if not found:
            print('no expense found!')
    				
def delete_expense():
	if not expenses:
		print('no expenses to delete')
	else:
		delete=input('enter expense name to delete: ')
		found=False
		for expense in expenses:
			if delete==expense['name']:
				found=True
				expenses.remove(expense)
				print('expense deleted successfully! ')
				break
		if not found:
				print('no expense found! ')			
def filter_by_category():
    if not expenses:
        print('no expenses yet!')
    else:
        filter = input('enter category to filter: ')
        found = False

        for expense in expenses:
            if filter == expense['category']:
                print('--------------------')
                print(f"Name: {expense['name']}")
                print(f"Amount: {expense['amount']}")
                print(f"Category: {expense['category']}")
                print(f"Date: {expense['date']}")
                print('--------------------')
                found = True

        if not found:
            print('category not found!')
def total_spending():
	if not expenses:
		print('you do not spend anything! ')
	else:
		total=0
		for expense in expenses:
			total+=expense['amount']	
		print('total spending: ',total)
def category_statistics():
	if not expenses:
		print('no expenses yet! ')	
	else:
		categories=set()
		for expense in expenses:
			categories.add(expense['category'])	
		for category in categories:
			count=0
			total=0
			for expense in expenses:
				if category==expense['category']:
					count+=1
					total+=expense['amount']			
			print('category: ',category)
			print('count: ',count)
			print('total: ',total)			
def highest_expense():
	if not expenses:
		print('no expenses yet! ')
	else:		
		highest = 0
		highest_expense=None
		for expense in expenses:
		    if expense['amount'] > highest:
		        highest = expense['amount']	
		        highest_expense=expense
		print('highest expense: ',highest_expense['name'])
		print('highest amount: ',highest)		
def monthly_summary():
	if not expenses:
		print('no expenses yet! ')
	else:
		month=input('enter month(YYYY/MM): ')
		count=0
		total=0
		for expense in expenses:			
			if expense['date'][:7] == month:
				count+=1
				total+=expense['amount']
		print('month ',month)
		print('number of expenses: ',count)
		print('total spending: ',total)									
while True:
    print('-----------------------------------')
    print('1: Add Expense')
    print('2: Show All Expenses')
    print('3: Search')
    print('4: Delete Expense')
    print('5: Filter by Category')
    print('6: Total Spending')
    print('7: Category Statistics')
    print('8: Highest Expense')
    print('9: Monthly Summary')
    print('10: Exit')
    print('-----------------------------------')

    choice = input('Enter your choice (1-10): ')

    if choice == '1':
        add_expense()
    elif choice=='2':
        show_expense()    
    elif choice=='3':
    	search_expenses()
    elif choice=='4':
    	delete_expense()
    elif choice=='5':
    	filter_by_category()	
    elif choice=='6':
    	total_spending()	
    elif choice=='7':
    	category_statistics()		
    elif choice=='8':
    	highest_expense()	
    elif choice=='9':
    	monthly_summary()
    elif choice=='10':
    	print('Welcom! ')
    	break		
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')    	