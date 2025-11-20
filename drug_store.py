# %%filepath = '/Users/maciej/Documents/result.txt'

with open(filepath,'r') as file:
    for line in file:
        line = line.replace("\n", " ")
        order = line.split(",")

        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' % (order[0],order[1],order[2]))
        else:
            print("Line %s malformed!!!" % line)
 
print("Processing finished")


# %%
