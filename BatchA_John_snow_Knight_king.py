'''
Docstring for John_snow_Knight_king

refer to readme

given that the knight king has 10000 health points  
given the for which time john snow will attack the knight shift
and the rate of attacks

print total damage done 
print true if knight king is dead and false otherwise  

'''

time = int(input("Time: "))
attacks_per_second = int(input("Attacks per second: "))
time_unit = input("unit: ") #lowercase

if time_unit == "hour":
    time = time*60*60
if time_unit == "minute":
    time = time*60

damage = time*attacks_per_second

print(damage)

if damage >= 10000:
    print(False)
else:
    print(True)

    


