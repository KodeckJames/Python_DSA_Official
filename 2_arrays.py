# Example: Say you are storing Apple's stock prices for 5 days 
stock_prices=[297, 330, 559, 785, 906]
# Scenario 1: Looking for the stock price on day 3:
day_2_stock_price=stock_prices[2]
print(day_2_stock_price)
# The big O complexity of looking for an array element by index is O(1) meaning, it's a constant time operation.

# SCENARIO 2: ON WHAT DAY WAS PRICE 785?
# Here you're not looking by index, but by value
stock_prices=[297, 330, 559, 785, 906]
def get_stock_price(stock_price):
    stock_price_index=len(stock_prices)
    for i in range(stock_price_index):
        if stock_prices[i]==785:
            return i
        
answer=get_stock_price(785)
print(answer)

# SCENARIO 3: PRINT ALL PRICES
def print_all_stocks():
    for stock_price in stock_prices:
        print(stock_price)
print_all_stocks()

# SCENARIO 4: INSERTING NEW PRICE e.g. 284 AT INDEX 1
def insert_new_price():
    stock_prices.insert(1, 284)
    print(stock_prices)
insert_new_price()

# EXERCISE
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
# Question 1
# a)
monthly_expenses =  [2200, 2350, 2600, 2130, 2190]

def feb_extra_expenses():
    extra_expense=monthly_expenses[1]-monthly_expenses[0]
    return extra_expense
result=feb_extra_expenses()
print(result)

# b)
def expenses_in_first_three_months():
    total=0
    for i in range(3):
        total+=monthly_expenses[i]
    return total
total_expenses=expenses_in_first_three_months()
print(total_expenses)

# c)
def expenditure_of_2000():
    for expense in monthly_expenses:
        if expense==2000:
            return True
        return False
print(expenditure_of_2000())

# d)
def add_June_expenditure():
    monthly_expenses.append(1980)
    return monthly_expenses
print(add_June_expenditure())

# e)
def April_correction():
    new_April_expenditure=monthly_expenses[3]-200
    monthly_expenses[3]=new_April_expenditure
    return monthly_expenses
print(April_correction())

# Question 2
# a)
heroes=['spider man','thor','hulk','iron man','captain america']
print(len(heroes))

# b)
heroes.append('black panther')
print(heroes)

# c)
heroes.pop()
heroes.insert(3, 'black panther')
print(heroes)

# d)
heroes[1:3]=["doctor strange"]
print(heroes)

# e)
heroes.sort()
print(heroes)

# Question 3
def list_of_odd_numbers():
    user_input=int(input("Enter maximum number: "))
    odd_numbers=[]
    initial_odd_number=1
    while initial_odd_number < user_input:
        initial_odd_number+=1
        if initial_odd_number%2!=0:
            odd_numbers.append(initial_odd_number)   
    return odd_numbers

print(list_of_odd_numbers())