'''
Q2.[Help Me Newton] A constant retarding force of X Newton is applied to a body of mass Y kg
moving initially with a speed of Z m/s. Print how long does the body take to stop?
Formulae to be used:
As the retarding force X is constant, the acceleration will also be constant throughout(Why? - as mass
Y is constant, the acceleration, a = X/Y will also be constant)
Since the body comes to complete halt after some time t, its final velocity, V can be assigned as 0.
Therefore, the total time as required in the question, can be calculated as:
t= Z/a [From first equation of motion, v = u + at]

Input :
The first line contains the value of x

The second line contains the value of y
The third line contains the value of z
Output:
Print how long does the body take to stop
Sample Input 1 :
50
20
15
Sample Output 1:
6
'''

x = int(input("Enter x: "))

y = int(input("Enter y: "))

z = int(input("Enter z: "))

acc = x/y 

t = z/acc

print(t)

