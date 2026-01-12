x = int(input("x: "))
y = int(input("y: "))

while True:
    x = x - 7
    y = y + 6
    if y > x:
        break

print(x)
print(y)