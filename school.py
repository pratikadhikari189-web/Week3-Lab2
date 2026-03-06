distance = float(input("Enter distance from school (km): "))
age = int(input("Enter student age: "))
right_to_stay = input("Does the student have the right to stay in NZ? (yes/no): ")
international_fees = input("Will the student pay international fees? (yes/no): ")

if age < 18:
    if distance < 4 and right_to_stay == "yes":
        print("Student can enrol.")
    elif international_fees == "yes":
        print("Student can enrol as an international student.")
    else:
        print("Student cannot enrol.")
else:
    print("Student cannot enrol (must be under 18).")
