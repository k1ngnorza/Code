# strings in python are used to communicate with the users by telling the user information/instructions via on-screen text
    any symbols "!@#$%^&*()_+-" can be written on the string, as long as ther are within the quotation marks

TIPS:
    # Try to use double quotation marks as a standard, single quatation marks are fine but if you can use double quotation
    # marks, you can avoid problems like these that require more typing to fix.
        print('he's') # will result in an error

USES:
# combined with 'input()' and using limitations such as 'If, Else Statements' you can build
# a very engaging program, simple or not:
    print("what is your name?")
    userName = input()
    if userName == 'Norielle':
        print("Welcome back, Norielle!")
    else:
        print("You are not welcome here!")