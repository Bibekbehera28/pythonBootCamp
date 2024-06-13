import random
while True:
    trials = 0
    while True:
        number = random.randint(1,3)
        trials += 1
        guess = int(input("Enter Guess Number:"))
        if guess == number:
            break
        elif guess>number:
            print("Try lower number!")
        elif guess<number:
            print("Try higher number")
    print(f"you guessed it correct in {trials} trials.")
    guess = input("Do you want to continue (y/n):")
    if guess == "n":
        break
print("Thank You!")
        