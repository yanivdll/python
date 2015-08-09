# this program says hello and ask for my name

print('Hello world!')
print('What\'s your name?')
myName = input()
print('It\'s good to meet you, ' + myName)
print('The length of your name is: ' + str(len(myName)))
print('What\'s your age?')
myAge = input() #need to run an if on the input to make sure it's a number

print('You\'ll be ' + str(myAge + 1) + ' in one year')
    
