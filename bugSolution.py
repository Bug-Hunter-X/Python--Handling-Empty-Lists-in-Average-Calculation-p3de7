def calculate_average(numbers):
    if not numbers:
        return None #or raise an exception
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")
#If the list is empty, it returns None, rather than throwing an error.