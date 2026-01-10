'''
Q1 .[Easy Squares]A number ‘n’ is called a perfect square if it can be expressed as a product of 2 equal
integers, let say x. In other words, the equation: x * x = n must hold for some integer x and n. For
example, if n = 25, then x = 5 will satisfy the equation. For a given perfect square number n, find
integer x.
Input :
The first line contains an integer denoting perfect square n.
Output:
For the first line, print an integer x satisfying the equation x * x = n
Sample Input 1 :
25
Sample Output 1:
5
Sample Input 2 :
625
Sample Output 2 :
25
'''


n = int(input("Enter perfect square: "))

n_half = n//2

for i in range(1,n_half):
    if i*i == n:
        print(i)
        break
    
