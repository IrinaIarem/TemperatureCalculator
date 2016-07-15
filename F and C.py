def temperature(a):
    tem = (a - 32)/ 1.8
    return tem

def convert(b):
    con = b* 1.8 + 32
    return con

c = True
while c == True:



    counter = int(input("What is the temperature in F?"))
    print (temperature(counter),(counter))

    europe = int(input("what is the temperature in C?"))
    print (convert(europe),(europe))


    ans = input("Do you want to continue?")
    if ans == "yes":
        c = True
    else: c = False