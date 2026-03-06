dB=float(input("Enter the decibels: "))
if dB==130:
    print("jackhammer")
elif dB==106:
    print("petrol lawnmower")
elif dB==70:
    print("Alarm Clock")
elif dB==40:
    print("Quiet Room")
elif dB >40 and dB < 70:
    print("Between Quiet room and Alarm clock")
elif dB >70 and dB < 106:
    print("Between Petrol lawnmower and Alarm clock")
elif dB >106 and dB < 130:
    print("Between Petrol Lawnmower and Jackhammer")
else:
    print("Enter valid dB!")