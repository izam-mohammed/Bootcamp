def hai(): #Rasing exception
    val = input('Press a number apart from 1 : ')
    if val=="1":
        raise ValueError("1 is not allowed")

#handling
try:
    hai()
except ValueError:
    print("value error found")