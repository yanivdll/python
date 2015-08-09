message = 'It was a wamr day, actually a hellish day here in Israel. I hope wether will be better back at NY.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print(count)
