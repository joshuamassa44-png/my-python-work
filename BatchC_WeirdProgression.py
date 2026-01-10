x = int(input("Enter x: "))

n = int(input("n terms: "))

def final_term(x,n):
    term = 0
    for d in range(n):
        term += (x**(d+1))//(d+1)
    return term

print(final_term(x,n))

