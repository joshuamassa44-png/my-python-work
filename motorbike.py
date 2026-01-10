'''
Docstring for motorbike
Given the cost price of a motorbike, calculate the final amount
that the motorbike costs given the following tax criteria

cost price                tax
> 100000                  15%
> 75000 and <= 100,000    12%
> 50000 and <= 75000      10%
<= 50000                  5%
'''

cost = int(input("Enter Cost Price: "))

if cost > 100000:
    print(int(cost + 0.15*cost))
elif cost > 75000 and cost <= 100000:
    print(int(cost + 0.12*cost))
elif cost > 50000 and cost <= 75000:
    print(int(cost + 0.1*cost))
else:
    print(int(cost + 0.05*cost))
 
