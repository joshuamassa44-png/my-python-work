n = int(input("n: "))

pos_count = 0
neg_sum= 0

for v in range(n):
    y = int(input("integer: "))
    if y > 0:
        pos_count += 1
    else:
        neg_sum += y

print(pos_count)
print(neg_sum)


