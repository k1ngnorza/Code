########## CALCULATOR ###########
print("######CALCULATOR######")

##operators = ['+', '-', '/', '*', '**', '%']


# Create a list of functions you want to use for your calculator
def add_(x,y):
    return(x+y)
def sub_(x,y):
    return(x-y)
def mult_(x,y):
    return(x*y)
def div_(x,y):
    return(x/y)
def pow_(x,y):
    return(x**y)
def flo_(x,y):
    return(x//y)

#We create a dictionary relating the operation to each function
# add_ points to where the function is that you can call later
# for example: If we type  Love = add_
# we can then do Love(3,4)
# which returns  7

operator_dic = {'+':add_, '-':sub_, '/':div_, '*':mult_, '**':pow_, '%':flo_}

while True:
    # inputs & invalids
    ##num1 = input("-number1: ")
    
    num1 = input("What's your operation!")
    try:
        num1 = num1.replace(" ","") #We remove all spaces in the string
                                    # Strings are immutible lists btw
        x = int(num1[0])            # we presume the form x + y  where the first string entry is a number
        operator = num1[1:-1]       # since the operator can be of any size either * or **,
                                    # we try to collect the entire operator
        y = int(num1[-1])           # we select for the last number in the list
        (operator in operator_dic) == True # always nice to test if the operator exists
        
        
    except:
        print("Invalid input! must be in the form of  (x * y)")
        continue
    
    
    #operator_dic[operator] returns the function
    #once we have the function, we apply the arguments that then return a values
    
    result = operator_dic[operator](x,y)
    
    #we return the printed result
    print("\nYour result is: \n", str( result), "\n")
    
        
        
        
'''    
        
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
'''