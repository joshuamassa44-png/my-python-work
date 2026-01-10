'''
given the number of operation 
ask for the operation type at each instance
i.e 1 for division, 2 for subtraction, 3 for absolute test, 4 for divisibilty test, 
5 for the special opeartion 
then ask for the necessary inputs and perform the required operation 
'''

def int_div():
    a = int(input("a: "))
    b = int(input("b: "))
    print(a//b)

def subtraction():
    a = int(input("a: "))
    b = int(input("b: "))
    print(a-b)

def absolute():
    a = int(input("a: "))
    abs(a)

def div_test():
    a = int(input("a: "))
    b = int(input("b: "))
    if a%b == 0:
        print(True)
    else:
        print(False)

def spec_op():
    a = int(input("a: "))
    b = int(input("b: "))
    if a%4 == 0:
        print((a+b)**2)
    else:
        print(min(a,b))
        
def make_op(t):
    if t == 1:
        int_div()
    elif t == 2:
        subtraction()
    elif t == 3:
        absolute()
    elif t == 4:
        div_test()
    elif t == 5:
        spec_op()

operation_number = int(input("Enter the number of operations: "))
for i in range(operation_number):
    operation_type = int(input("Enter the operation: "))
    make_op(operation_type)

