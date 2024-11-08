# create a program that checks a student performance

marks=int(input("Enter marks: "))

if marks <= 100 and marks >= 80:
    print("Your grade is A")
elif marks <=79 and marks >=60:
    print("Your grade is B")
elif marks <=59 and marks >=40:
    print("Your grade is C")
elif marks <=39 and marks >=20:
    print("Your grade is D")
else:
    print("Your have Failed")



# create a program that is going to calculate BMI

height=int(input("Enter your height in meters: "))
weight=int(input("Enter your weight in kilograms: "))
bmi=weight / (height ** 2)

if bmi<18.5:
    print("underweight")
elif 18.5 <= bmi <25:
    print("normal")
elif 25 <= bmi <29:
    print("overweight")
else:
    print("obese")

print(f"Your BMI is {bmi:.2f}")


