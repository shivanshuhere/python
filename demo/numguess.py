import random 

num = random.randint(1, 100)
print("Guess number between 1 to 100 ! press any key to continue...")
guess = None
attempt  = 0

while guess != num :
    guess = int(input("guess number :"))
    attempt += 1
    if guess == num:
        print(f"You win! after {attempt} attempts\n")
    elif guess > num:
        print("too high")
    elif guess < num:
        print("too low")
    

