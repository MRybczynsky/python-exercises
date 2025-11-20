# %%import os

while True:
    filename = input('Enter path to result file:')

    if os.path.isfile(filename):
        break
    else:
        print('File name is not correct, try again')

print('The result file is %s' % (filename))
# %%
