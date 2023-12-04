from string import ascii_letters

def processString(input):
    output = ''
    for letter in input:
        if letter in ascii_letters:
            continue
        else:
            output += letter
    num = int(output[0] + output[-1])
    return num

with open('input.txt') as fh:
    text = fh.read()
    text = text.split('\n')

total = 0

for line in text:
    total += processString(line)

print(total)