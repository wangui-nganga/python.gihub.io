#Q1
#Write a function reverse_string(s) that takes a string s and returns the reversed string.
#create a function
import string


def reverse_string(string):
    return string[::-1]
txt = reverse_string("Welcome to Ruby Group 2")
print(txt)


#Q2
#Create a function is_palindrome(word) that returns True ,
# if a given word is a palindrome (reads the same backward) and False otherwise.

# Define the function
def is_palindrome(string):
    if string == string[::-1]:
        return "True"
    else:
        return "False"

# Enter the input
string = input("Enter a string: ")
print(is_palindrome(string))

#Q3
#Write a function fibonacci(n) that generates a list,
# containing the first n numbers in the Fibonacci sequence.
#define the function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 10
for i in range(0,n):
    print(f"The sequence is {fibonacci(i)}")