import random

print("I have a number in my mind from 1 to 100 ,let's see if you can guess it ")
#string hard,easy
rand_no = random.randint(0,100)
end_game = False
user_diff = input("Select the difficulty level :: Hard or easy:  ")
if user_diff == "hard":
    print("you have five guesses: ")
    guesses = 5
    for i in range(0,5):
        user_no = int(input("enter your guess"))
        if user_no > rand_no:
            print("too high")
        elif user_no < rand_no:
            print("too low")
        elif user_no == rand_no:
            print("it's exact match , you win")
            end_game = True
elif user_diff == "easy":
    print("you have ten guesses")

    guesses = 10
    for i in range(0, 10):
        user_no = int(input("enter your guess"))
        if user_no > rand_no:
            print("too high")
        elif user_no < rand_no:
            print("too low")
        elif user_no == rand_no:
            print("it's exact match , you win")
            end_game = True

            
