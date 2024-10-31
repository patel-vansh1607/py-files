print("------------------------------")
print("WELCOMEE TO THE CALCULATOR APP")
print ("---------------------------- ")

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
operator = input("Enter your operator (Hint: '/', '*','-','+' ) ")

if operator == '+':
    result = first_number + second_number
    print("---------------------------")
    print(result)
    print("---------------------------")
elif operator == '-':
    result = first_number - second_number
    print("---------------------------")
    print(result)
    print("---------------------------")
elif operator == '*':
    result = first_number * second_number
    print("---------------------------")
    print(result)
    print("---------------------------")
elif operator == '/':
        result = first_number / second_number
        print("---------------------------")
        print(result)
        print("---------------------------")
else:
    print("---------------------------")
    print("Invalid operator! Please enter one of '/', '*', '-', '+'.")
    print("---------------------------")