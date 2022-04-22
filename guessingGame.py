import random

number = random.randint(1, 9)
chances = 0
print("pick a number between 1 and 9)")

while chances < 5:
    guessNumber = int(input("Enter your Number - "))

    if guessNumber == number:
        print("you got it, you win")
        break

    elif guessNumber < number:
        print("your number is too low")
    else:
        print("your number is too high")
    chances += 1
if not chances < 5:
    print("you didnt get it in 5 tries the number is", number)