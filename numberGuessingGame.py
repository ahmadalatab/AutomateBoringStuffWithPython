import random
def numberGame():
    randomNum=random.randint(1,20)
    counter=1
    print("I am thinking of a number between 1 and 20")
    while True:
        userInput=int(input("Take a guess: "))
        if(userInput < randomNum):
            print("Your guess is too low")
            counter=counter + 1
            continue
        elif(userInput > randomNum):
            print("Your guess is too high")
            counter=counter + 1
            continue
        else:
            print("Good job! You guessed my number in ", counter, " guesses")
            break
numberGame()