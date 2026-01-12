eff_resistance = 0
while True:
    res_value = int(input("Enter Resistance: "))
    if res_value <= 0:
        break
    eff_resistance += 1/res_value

print(eff_resistance)