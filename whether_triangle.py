'''
Docstring for whether_triangle
given the 3 sides of a triangle a, b and c.
check whether the triangele is valid. 
that is: sum of any 2 sides must be greater than the third side
print "valid" if valid and "invalid" otherwise
'''

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a+b>=c and a+c>=b and b+c>=a: 
    print("valid")
else:
    print("invalid")

