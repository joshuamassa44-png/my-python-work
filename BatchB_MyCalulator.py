def multiplication():
    a = int(input("a: "))
    b = int(input("b: "))
    print(a*b)

def addition(a,b):
    a = int(input("a: "))
    b = int(input("b: "))
    print(a+b)

def negation(a):
    a = int(input("a: "))
    print(-1*a)

def power(a,b):
    a = int(input("a: "))
    b = int(input("b: "))
    print(a**b)

def special_operation(a,b):
    a = int(input("a: "))
    b = int(input("b: "))
    if a//2 == 0:
        print((a-2)*b)
    else:
        print(max(a,b))

operation_type = int(input("operation: "))

if operation_type == 1:
    multiplication()
elif operation_type == 2:
    addition()
elif operation_type == 3:
    negation()
elif operation_type == 4:
    power()
elif operation_type == 5:
    special_operation()

