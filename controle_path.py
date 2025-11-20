# %%import os
from datetime import date

data_input_catalog = '/Users/maciej/Documents/data_input'
data_output_catalog = '/Users/maciej/Documents/data_output'
today = str(date.today())

#print(os.path.join(data_output_catalog, today.strftime("%Y-%m-%d")))
today_output_catalog = os.path.join(data_output_catalog, today)

is_input_catalog_ok = os.path.isdir(data_input_catalog)
is_output_catalog_ok = os.path.isdir(data_output_catalog)
is_today_output_catalog_ok = os.path.isdir(today_output_catalog) and os.path.isfile(today_output_catalog) 


if(is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok==False):
    print('Conditions met! We can continue!')
elif (is_input_catalog_ok == False):
    print("Bad conditions. Input catalog doesn't exist")
elif (is_output_catalog_ok == False):
    print("Bad conditions. Output catalog doesn't exist")
elif (is_today_output_catalog_ok == True):
    print('Bad conditions. File exists')



# %%
