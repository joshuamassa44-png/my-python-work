'''
Docstring for discr_quad
Q3. [Discriminating Quadratic ]The standard form of quadratic equation is defined as : ax^2 + bx + c.
For a given quadratic equation with given a, b and c, find its discriminant. (Discriminant is defined as
b^2 - 4ac).
Input :
The first 3 lines contain integers denoting a,b and c.
Output:
Print the discriminant of the polynomial
Sample Input 1 :
1
-10
25
Sample Output 1:
0

'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = b**2 - 4*a*c

print(discriminant)

