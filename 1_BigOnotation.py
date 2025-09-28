def get_squared_numbers(numbers):
    squared_numbers=[]
    for number in numbers:
        squared_numbers.append(number*number)
    return squared_numbers

input_numbers=[3,4,5,6,7,8,9]
solution=get_squared_numbers(input_numbers)
print(solution)