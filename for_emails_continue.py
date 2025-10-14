# %%persons = ['Elizabeth', 'Steven@sales.mycomapny.com', 'Sebastian', 'Margaret', 'Svetlana@mycompany.eu', 'Raphael']

domain = 'mycompany.com'

emails = []

'''for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email = person + '@' + domain
        emails.append(email)

for email in emails:
    print(email)'''

for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)


menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
-----------------------
To stop this script select 0
'''



while True:
    print(menu)
    letter = input("Enter your choice ")
    if letter == '1':
        print("Function COFFEE not implemented")
        input("Please, press ENTER")
        continue
    if letter == '2':
        print("Function TEA not implemented")
        input("Please, press ENTER")
        continue
    if letter == '3':
        print(":)")
        input("Please, press ENTER")
        continue
    if letter = '0':
        break
    input("You need to make a valid choice. Press ENTER and try again!")

# %%
