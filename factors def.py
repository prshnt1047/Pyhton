def factors(x):
    for i in range(1,x+1):
        if (x%i==0):
            print(i)


x=int(input("enter any number"))
factors(x)
