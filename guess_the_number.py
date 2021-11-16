import random
print("\nWelcome to the Guess Number Game")
while True:
    level = int(input("The number is between 0 and: "))
    number = random.randrange(0,level)
    while True:
        number_guessing = int(input("The number is: "))
        if number_guessing > number:
            print("It's too higher")
        elif number_guessing < number:
            print("It's too lower")
        else:
            print("Correct")
            break
    still_playing = input("Do you want to keep playing? Press Y for Yes or N for Not: ")
    if still_playing == 'N':
        break
