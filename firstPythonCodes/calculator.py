########## CALCULATOR ###########
print("######CALCULATOR######")

operators = ['+', '-', '/', '*', '**', '%']

while True:
    # inputs & invalids
    num1 = input("-number1: ")
    if num1 == 'q':
        break
    try:
        int(num1)
    except:
        print("Invalid Input, Try Again1")
        print("####################1")
        continue

    operator = input("operator: ")
    if operator == 'q':
        break
    if operator not in operators:
        print("Invalid Input, Try Again2")
        print("####################2")
        continue

    num2 = input("-number2: ")
    if num2 == 'q':
        break
    try:
        int(num2)
    except:
        print("Invalid Input, Try Again3")
        print("####################3")
        continue
    
    # operators
    if operator == '+':
        plus = float(num1) + float(num2)
        result = "Result: " + str(plus)

    elif operator == '-':
        subtract = float(num1) - float(num2)
        result = "Result: " - str(subtract)

    elif operator == '/':
        divide = float(num1) / float(num2)
        result = "Result: " + str(divide)

    elif operator == '*':
        times = float(num1) * float(num2)
        result = "Result: " + str(times)

    elif operator == '**':
        power = float(num1) ** float(num2)
        result = "Result: " + str(power)
    
    else:
        print("--" + result)
        print("####################")
        continue
    
    # results
    print("--" + result)
    print("####################")

# prints this out, when out of the while loop
print("################################")
print("# You have quit the Calculator #")
print("################################")