# %%def printHello():
    #this function just print hello
    print("Hello")
    return

def printAnimal(*animals):
    #this function just print animal
    cat = r'''
    |\---/|
    | o_o |
     \_^_/'''

    bear = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''

    bat = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/       '''
    
    for animal in animals:
        if(animal == 'cat'):
            print(cat)
            print(True)
        elif(animal == 'bear'):
            print(bear)
            print(True)
        elif(animal == 'bat'):
            print(bat)
            print(True)
        else:
            print(False) 
            
    return



printHello()
printAnimal('cat','bat')
printAnimal('bear')
#printAnimal('bat')
#printAnimal()
#printAnimal('zebra')




# %%
