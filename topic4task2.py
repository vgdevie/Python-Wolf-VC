import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    else:
        result = random.sample(range(min, max+1), quantity)
        result.sort()
        return result

min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))
quantity = int(input("Enter the quantity of numbers: "))

print("Your lottery numbers are: ", get_numbers_ticket(min, max, quantity))