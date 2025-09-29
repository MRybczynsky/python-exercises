message1 = 'Processing file %s'
print(message1 % ('file_1.txt'))

message2 = 'File %s has size %d KB'
print(message2 % ('file_1.txt',100))

message3 = 'File %20s has size %10d KB'
print(message3 % ('file_1.txt',100))

message4 = 'Processing file {0:s}'
print(message4.format('file1.txt'))

helloMessage = '\nHello %s!'
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))

helloMessage = '\nHello {0:s}!'
print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))

helloMessage = "\n%s has %d %s"
print(helloMessage %('Kate', 1, 'animal'))
print(helloMessage %('Chris', 100000, '$'))

helloMessage = "\n{0:s} has {1:d} {2:s}"
print(helloMessage.format('Kate', 1, 'animal'))
print(helloMessage.format('Chris', 100000, '$'))

line = '\n%20s costs %6d $'
print(line % ('Ice cream',3))
print(line % ('Trip to Venice',1500))
print(line % ('Pizza',10))
