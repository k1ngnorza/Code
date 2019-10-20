#this program says hello and asks for my name and age and my age in 5 years time

#intro
print('Hello Dude!')

#asks my name
print('What is your name?')
myName = input()
print('Nice to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))

#asks my age
print('what is your age?')
myAge = input()
print('you are '+ myAge + '!')
print('you will be ' + (str(int(myAge) + 5)) + ' in 5 years.')