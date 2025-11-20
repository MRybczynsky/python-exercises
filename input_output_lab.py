# %%import os
webaddresses = []

line = input("Please enter a web address:")

while len(line)>0:
    webaddresses.append(line)
    line = input("Please enter a web address:")

print(webaddresses)

dirname = os.getcwd()

print(dirname)

filename = input("Please enter a file name:")
filepath = os.path.join(dirname, filename)
print(filepath)

file = open(filename, 'w+')

for address in webaddresses:
    file.write(address +'\n')
    
file.close()


fileToCheck = input("Enter path to file:")

while not os.path.isfile(fileToCheck):
    fileToCheck = input("Please enter correct path to file:")

webaddresses2 = []

with open(fileToCheck,'r') as file:
    for line in file:
        webaddresses2.append(line.replace("\n",""))

dirname = os.path.dirname(fileToCheck)
webPathPL = os.path.join(dirname, 'webs_pl.txt')
webPathOther = os.path.join(dirname, 'webs_other.txt')
filePL = open(webPathPL, "w")
fileOther = open(webPathOther, "w")


for address in webaddresses2:
    if address.endswith(".pl"):
        print(address, " is a polish web page")
        filePL.write(address + "\n")
    else:
        print(address, "is not a polish web page")
        fileOther.write(address + "\n")

filePL.close()
fileOther.close()

# %%
