s = 'A Python script'
print(s[0])
print(s[2])
print(s[2:7])
print(s[:8])
print(s[8:])
print(s[2:999])
print(s[222:999])

message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[message.find(':')+2:])

start = message[message.find('"')+1:]
print(start)

end = start[:start.find('"')]
print(end)

q = "THE EYES"
print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])

q = "a gentleman"
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])


#z napisu  "THE MORSE CODE" zrobić tekst "HERE COME DOTS"
m = "THE MORSE CODE"
#    01234567890123
print(m[1:3],m[6],m[2],m[3],m[10:12],m[4],m[2],m[3],m[12],m[11],m[0],m[7])

''' 'Program "Kropka nad i" nadamy o: 22:00'

'Program "Pytanie na śniadanie" nadamy o: 6:00'''

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(':')+2:]
print(time)
tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title, time)

line2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
time2 = line2[line2.find(':')+2:]
print(time2)
tmp2 = line2[line2.find('"')+1:]
print(tmp2)
title2 = tmp2[:tmp2.find('"')]
print(title2, time2)


