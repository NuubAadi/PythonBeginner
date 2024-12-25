"""
Write an algorithm that performs the following:
 Ask a user to enter a number. If the number is
between 5 and 15, write the word GREEN. If the
number is between 15 and 25, write the word BLUE.
if the number is between 25 and 35, write the word
ORANGE. If it is any other number, write that ALL
COLOURS ARE BEAUTIFUL.
"""
a = int(input("Enter a number between 5 and 35 : "))
if a>5 and a<15:
    print("GREEN")
elif a>15 and a<25:
    print("BLUE")
elif a>25 and a<35:
    print("ORANGE")
else:
    print("ALL COLOURS ARE BEAUTIFUL!!")