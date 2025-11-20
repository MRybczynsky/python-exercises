# %%# filename = input("Enter filename:")
# print("The file name is: %s" % (filename))

while True:
    filesize = input("Enter file size (MB) :")
    #print("The file size is: %s" % (filesize))
    #print("The file size in KB is: %s" % (filesize*1024))
    if filesize.isdecimal():
        filesizeINT = int(filesize)
        break
        
print("The file size is: %s" % (filesizeINT))
print("The file size in KB is: %s" % (filesizeINT*1024))

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

import math

while True:
    a = input("Enter a:")
    b = input("Enter b:") 
    c = input("Enter c:") 
    if check_int(a) and check_int(b) and check_int(c):
        a = int(a)
        b = int(b)
        c = int(c)
        if a==0:
            print("This is not a quadratic equation")
        else:
            delta = pow(b,2)-4*a*c
            if delta<0:
                print("No solutions")
            elif delta==0:
                x1=(-b)/(2*a)
                print("x1 =", x1)
            else:
                x1=(-b-delta**0.5)/(2*a)
                x2=(-b+delta**0.5)/(2*a)
                print("x1 =",x1)
                print("x2 =",x2)
    else:
        print("Wrong value!")




# %%
