def hello_func(func):
    print("HELLO WORLD")
    return func
    
@hello_func
def hai():
    pass

hai()