import random
x = random.randint(1,10)
count = 1
guess = 0

while guess != x and guess != "exit":
    guess = int(input("Enter a guess brtween 1 and 10: "))

    if guess =="exit":
        print("by")
        break

    elif guess < x:
        print("to low")
        count += 1
    elif guess > x:
        print("to high")
        count += 1

    else:
        print("You do it this is the number")
        print("And you did it in ", count , "tries")
        print("Game over")
