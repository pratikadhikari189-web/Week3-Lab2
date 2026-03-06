magnitude=float(input("Enter the magnitude: "))

if magnitude <2:
    print("Micro")

elif magnitude>=2.0 and magnitude <3.0:
    print("Very minor")

elif magnitude >= 3 and magnitude <4:
    print("Minor")

elif magnitude >= 4 and magnitude <5:
    print("Light")

elif magnitude >=5 and magnitude <6:
    print("moderate")

elif magnitude >=6 and magnitude <7:
    print("strong")

elif magnitude >=7 and magnitude <8:
    print("Major")

elif magnitude >=8 and magnitude <10:
    print("Great")

elif magnitude >=10:
    print("Metoric")
else:
    print("enter the valid magnitude!")