a = int(input("Enter working days: ")) #working days
b = int(input("Enter absent days: "))

attendance_percentage = ((a-b)/a)*100

if attendance_percentage < 60:
    print("CANNOT GIVE EXAM")
else:
    print("CAN GIVE EXAM")


