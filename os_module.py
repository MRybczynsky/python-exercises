# %%import os
import time

print('Current directory is:', os.getcwd())

currentDir = os.getcwd()
filename = 'result.txt'
fullpath = os.path.join(currentDir,filename)
print('\nThe contructected file path is:', fullpath)

relativePath = 'output.txt'
print('\nThe abcolute path is: ', os.path.abspath(relativePath))

filepath = r'/temp/result.txt'
print('\nThe file name part is: ', os.path.basename(filepath))
print('The directory part is: ', os.path.dirname(filepath))

print('\nIs file existing?', os.path.exists(filepath))

if os.path.exists(filepath):
    print('\nLast modify date is:', os.path.getmtime(filepath))
    print('\nLast modify date is:', time.localtime(os.path.getmtime(filepath)))

    print('\nFile size is:', os.path.getsize(filepath))

    print('\nIs it a file?', os.path.isfile(filepath))
    print('Is it a dir?', os.path.isdir(filepath))

    print('\nPath splitted:', os.path.split(filepath))
    print('Only file name part:', os.path.split(filepath)[1])

    print('\nPath splitted into drive:', os.path.splitdrive(filepath))
    print('Only drive:', os.path.splitdrive(filepath)[0])
    
    

# %%
