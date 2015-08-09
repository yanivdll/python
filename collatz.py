def collatz(number):
    if number % 2 ==0:
        return number // 2
    else:
        return (number * 3 + 1)

print("Please enter a number: ")

while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('Bad input. Please enter only numeric value. Try again:')

while number != 1:
    number = collatz(number)
    print(number)
