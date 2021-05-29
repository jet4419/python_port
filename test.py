# f = open('text.txt', 'r')
# print(f.read())

# Proper opening of file
with open('text.txt', 'a') as f:
    f.write('\nAdded text 2')
