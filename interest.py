'''
Docstring for interest
Q4:[That’s My Interest] A simple interest on a Principal amount can be calculated as
(P * R * T)/100, where:
● P- Principal amount
● R - Rate of Interest
● T - Time period.
The user takes input for P, R and T respectively and compute and print the Simple Interest- S.
Input :
The first 3 lines contain integers denoting P, R and T
Output:
Print the Simple Interest- S corresponding to P, R and T
Sample Input 1 :
12
25
4
Sample Output 1:
12

'''

p = int(input("Principal: "))
r = int(input("Rate: "))
t = int(input("Time: "))

Interest = int((p*r*t)/100)

print(Interest)

