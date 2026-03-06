password = "python123"
attempts = 0
while attempts < 4:
    user = input("Enter password: ")
    if user == "exit":
        print("Program terminated.")
        break
    if user == password:
        print("Access granted.")
        break
    else:
        print("Wrong password.")
        attempts = attempts + 1
if attempts == 4:
    print("Too many attempts.")