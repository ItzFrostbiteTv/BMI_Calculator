from time import sleep

height = float(input("Enter Height In Inchs: "))
lbs = float(input("Enter Weight In Pounds: "))

BMI = round(lbs / (height * height) * 703, 2)

print("Your BMI Is:", BMI)
if BMI <= 24.9 and BMI >= 18.5:
    print("You Are Healthy")
    sleep(3)
    exit = input("Press Enter To Exit: ")
elif BMI > 24.9:
    print("You Are Overweight")
    sleep(3)
    exit = input("Press Enter To Exit: ")
elif BMI < 18.5:
    print("You Are Underweight")
    sleep(3)
    exit = input("Press Enter To Exit: ")
