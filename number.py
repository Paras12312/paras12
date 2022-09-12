#importing library
import random
number=random.randint(1,10)
name = input("Please enter your name:")
print("best of luck ",name)
number_of_guesses=0
print("okay",name," !I am going to guess a number from the range 1 to 10")

#main condition
while number_of_guesses < 5:
    guess=int(input("please enter a number:"))
    number_of_guesses+=1
    if guess<number:
        print("your guess is too low.please enter again")
    if guess>number:
        print("your guess is too high.please enter again")
    if guess==number:
        break

if guess==number:
    print("you guessed it correct and you guessed in " +str(number_of_guesses)+" tries")
else:
    print("you didn't guess the number. the number was "+str(number)+" . ")