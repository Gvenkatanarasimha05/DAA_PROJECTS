import random

def guessing_number():
    print("Welcome to the Number Guessing Game!")
    print("This is Venkat Guessing Master")
    print("You need to guess a number chosen by me ")
    num1 = int(input("Enter a start range: "))
    num2 = int(input("Enter an end range: "))
    x = random.randint(num1, num2)
    guess_chance = 0
    while True:
        guess = int(input(f"Guess a number between {num1} and {num2}: "))
        guess_chance += 1
        if x == guess:
            print(f"Congratulations! Your guess is correct. It took you {guess_chance} attempts.")
            break
        elif guess < x:
            print("Your guess is lower than the number.")
        else:
            print("Your guess is higher than the number.")
            
if __name__ =='__main__':
    guessing_number()