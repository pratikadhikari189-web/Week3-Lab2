rating=float(input("Enter the rating: "))
if  rating == 0.0:
    print("Unacceptabe")
elif rating == 0.4:
    print("Acceptable")
elif rating== 0.6 or rating > 0.6:
    print("Meritorious performance")
else:
    print("Enter a valid rating!")