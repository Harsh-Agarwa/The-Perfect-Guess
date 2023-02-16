import random
randnumber = random.randint(1,100)
userguess = None
guesses=0
print("\n")
print("Hello and Welcome to the game")
print("     THE PERFECT GUESS")
print("Developed by ")
print(" - HARSH AGARWAL.")
print("\n")
print("Lets goo.")
while(userguess != randnumber):
    userguess=int(input("Enter Your Guess: "))
    guesses+=1
    if(userguess==randnumber):
        print("Your Guess is Right!!")
    elif(userguess-randnumber>40 and userguess-randnumber<50):
            print("You have entered a LARGER number which has a difference in the Range of 40-50.")
            print("Enter some SMALLER NUMBERS.")
    elif(randnumber-userguess>40 and randnumber-userguess<50):
            print("You have entered a SMALLER number which has a difference in the Range of 40-50.")
            print("Enter some LARGER NUMBERS.")
    elif(userguess-randnumber>20 and userguess-randnumber<40):
            print("You have entered a LARGER number which has a difference in the Range of 20-40.")
            print("Enter some SMALLER NUMBERS.")
    elif(randnumber-userguess>20 and randnumber-userguess<40):
            print("You have entered a SMALLER number which has a difference in the Range of 20-40.")
            print("Enter some LARGER NUMBERS.")
    elif(userguess-randnumber>10 and userguess-randnumber<20):
            print("You have entered a LARGER number which has a difference in the Range of 10-20")
            print("Enter some SMALLER NUMBERS.")
    elif(randnumber-userguess>10 and randnumber-userguess<20):
             print("You have entered a SMALLER number which has a difference in the Range of 10-20")
             print("Enter some LARGER NUMBERS.")
    elif(randnumber-userguess>2 and randnumber-userguess<10):
            print("The difference in the numbers is in a single digit now..")
            print("Enter a LARGER number.")
    elif(userguess-randnumber>2 and userguess-randnumber<10):
             print("The difference in the numbers is in a single digit now..")
             print("Enter a SMALLER number.")
    elif(randnumber-userguess==1):
            print("The difference between the two numbers is exactly equal to 1..")
            print("Just Enter the NEXT number.")
    elif(userguess-randnumber==1):
             print("The difference between the two numbers is exactly equal to 1..")
             print("Just Enter the PREVIOUS number.")
    elif(userguess-randnumber==50):
            print("The difference between the numbers is 50.")
            print("Enter the previous 50th element.")
    elif(randnumber-userguess==50):
            print("The difference between the numbers is 50.")
            print("Enter next 50th element.")
    elif(userguess-randnumber==40):
            print("The difference between the numbers is 40.")
            print("Enter the previous 40th element.")
    elif(randnumber-userguess==40):
            print("The difference between the numbers is 40.")
            print("Enter next 40th element.") 
    elif(userguess-randnumber==20):
            print("The difference between the numbers is 20.")
            print("Enter the previous 20th element.")
    elif(randnumber-userguess==20):
            print("The difference between the numbers is 20.")
            print("Enter next 20th element.")   
    elif(userguess-randnumber==10):
            print("The difference between the numbers is 10.")
            print("Enter the previous 10th element.")
    elif(randnumber-userguess==10):
            print("The difference between the numbers is 10.")
            print("Enter next 10th element.") 
    elif(userguess-randnumber==2):
            print("The difference between the numbers is 2.")
            print("Enter the previous 2nd element.")
    elif(randnumber-userguess==2):
            print("The difference between the numbers is 2.")
            print("Enter next 2nd element.")                   

    else:
         print("Try some more numbers.")
print(f"You Have Guessed the number in {guesses} guesses.")
print("THANK YOU FOR PLAYING!!")
print("HOPE U MIGHT HAVE ENJOYED!!")