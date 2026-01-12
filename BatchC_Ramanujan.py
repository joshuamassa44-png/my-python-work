N = int(input("N:"))

v = int(N**(1/3)) + 1

count = 0
for g in range(1,v):
    if count == 2:
        break
    for f in range(v,0,-1):
        if (g**3 + f**3) == N:
            #print(str(f)+" "+str(g))
            count += 1
        if count == 2:
            break

if count == 2:
    print(True)
else:
    print(False)
    
