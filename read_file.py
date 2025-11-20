# %%file = open('/Users/maciej/Documents/result.rtf','r')

content = file.read()
print(content)

file.close()

with open('/Users/maciej/Documents/result.rtf','r') as file:
    content = file.read()
    print(content)

with open('/Users/maciej/Documents/result.rtf','r') as file:
    for line in file:
        print(line)

file = open('/Users/maciej/Documents/result.rtf','r')
fragment = file.read(10)
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)

file.close()



# %%
