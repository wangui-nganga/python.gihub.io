# python script that checks if  number is even or odd number


num=int(input("Enter a number: "))

if num%2==0:
    print(f"{num}is Even")
else:
    print(f"{num} is Odd")

# create a program that prints the largest of three numbers

num2=int(input("Enter the first number:"))
num3=int(input("Enter the second number:"))
num4=int(input("Enter the third number:"))
largest=max(num2,num3,num4)

if num2 >= num3 and num2 >= num4:
    print(f"{num2} ")
elif num3 >= num2 and num3 >= num4:
    print(f"{num3} ")
else:
    largest = num4
    print(f"The largest number is: {largest}")

    # master data structure and algorithms


