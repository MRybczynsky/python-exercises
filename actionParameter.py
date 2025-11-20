# %%def doAction(action, parameter):
    print("action:",action)
    print("parameter:",parameter)
    return
    
doAction("buy", "shoes")

def doAction2(action,*parameter):
    print("action:",action)
    print("parameter:",parameter)
    for element in parameter:
        print("element is",element)
    return
    
doAction2("buy", "shoes", "socks")
doAction2("buy", "shoes", "socks", "t-shirt")


def doAction3(action,what,**parameter):
    print("action:",action)
    print("what:",what)
    print("parameter:",parameter)
    for element in parameter:
        print(element, "=", parameter[element])
    return

doAction3("buy", "shoes", size=45, color="brown", type="sport")
# %%
