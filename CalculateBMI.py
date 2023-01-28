w=float(input("Enter your weight in Kilogram:  "))
h=float(input("Enter your height in Meter:  "))
if w<=0 or h<=0:
    print("You entered the wrong number.\nPlease be sure that the numbers are bigger than Zero for next try ")
else:
    print("Your BMI is equal to:" , w/(h**2) )