catsName = []
while True:
    print('Enter the name of cat number ' + str(len(catsName) + 1) + ' . Otherwise type nothing to exit:')
    name = input()
    if name == '':
        break

    catsName = catsName + [name]
print('Here are the names of your cats:')
for i in catsName:
    print(i)
