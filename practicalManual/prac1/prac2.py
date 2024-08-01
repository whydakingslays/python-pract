
""" Enter the number from the user and depending on whether the number is
even or odd, print out an appropriate message to the user."""

# Python program to check if the input number is odd or even.
# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.
num = int(input("Enter a number: "))
if (num % 2) == 0:
 print("{0} is Even".format(num))
else:
 print("{0} is Odd".format(num))