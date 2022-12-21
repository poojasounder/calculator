from art import logo
print(logo)

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def divide(num1,num2):
    return num1/num2

def multiply(num1,num2):
    return num1 * num2

operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
}

def calculator():
    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        choice_operation = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        function = operations[choice_operation]
        first_ans = function(num1, num2)
        print(f"{num1} {choice_operation} {num2} = {first_ans}")
        response = input(f"Type 'y' to continue calculating with {first_ans}, or type 'n' to start a new calculation: ")
        if response == 'y':
            num1 = first_ans
        else:
            should_continue = False
            calculator()

calculator()