# This function adds multiple numbers
def add(*args):
    return sum(args)

# This function multiplies multiple numbers
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# This function divides multiple numbers
def divide(*args):
    if len(args) < 2:
        print("Error: At least two numbers are required for division.")
        return None

    result = args[0]  # Initialize the result with the first number
    for num in args[1:]:
        try:
            result /= num
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None
    return result

# This function subtracts multiple numbers
def subtract(*args):
    if len(args) < 2:
        print("Error: At least two numbers are required for subtraction.")
        return None

    result = args[0]  # Initialize the result with the first number
    for num in args[1:]:
        result -= num
    return result

print("Select operation.")
print("1. Add")
print("2. Multiply")
print("3. Divide")
print("4. Subtract")  # Add subtraction option

running = True
while running:
    # take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num_count = int(input("Enter the number of integers: "))
            numbers = []
            for i in range(num_count):
                num = float(input(f"Enter integer {i+1}: "))
                numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Sum:", add(*numbers))
        elif choice == '2':
            print("Product:", multiply(*numbers))
        elif choice == '3':
            print("Result:", divide(*numbers))
        elif choice == '4':
            print("Result:", subtract(*numbers))

        # check if the user wants another calculation
        # break the while loop if the answer is no
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation == 'no':
            running = False
    else:
        print("Invalid Input")
