N = int(input("Enter N: "))


for g in range(1,N+1):
    if g%3 == 0:
        print("Fizz")
    elif g%5 == 0:
        print("Buzz") 
    elif (g%3 == 0 and g%5 == 0):
        print("FizzBuzz")
    else:
        print(g)

