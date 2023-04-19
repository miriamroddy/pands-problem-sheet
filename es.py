import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    contents = f.read()

count = 0
for letter in contents:
    if letter == 'e':
        count += 1

print(count)