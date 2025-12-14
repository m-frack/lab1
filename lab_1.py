import winsound

wzrost = float(input("podaj wzrost w cm: "))
masa = float(input("podaj masę ciała w kg: "))
bmi = round(masa/(wzrost/100)**2, 2)
if bmi < 18.5:
    print("niedowaga")
    winsound.Beep(400,700)
elif bmi < 24.9:
    print("waga prawidłowa")
    winsound.Beep(800, 700)
elif bmi < 29.9:
    print("nadwaga")
    winsound.Beep(400, 700)
else:
    print("otyłość")
    winsound.Beep(400,700)
