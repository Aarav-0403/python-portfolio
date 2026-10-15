import random
import time

def rules():
    print("In this game you have a specefic amount of cash at the beggining ,which is 100 at start if you are playing first time.\n")
    time.sleep(3)
    print("Which you will bet on a sample space of a rolling die,To either gain that amount more or lose that amount.\n")
    time.sleep(2.5)
    print("So, Let's start then .\n")
    

with open("wallet.txt","a") as file:
    file.close()

with open("wallet.txt","r") as balance:
    balance= balance.read()

if balance=="":
    cash=100
else:
  cash=int(balance)

print("----~WELCOME TO DIE-GUESSER~----")
time.sleep(1)
print("Let's get rolling")
time.sleep(0.9)


while True:
    bet_input=int(input(" enter your bet amount:  "))


    if bet_input > cash:
      print("You cant bet more than what you have.\n")
      continue
    elif bet_input == cash:
      print("You cannot bet all you have.\n")
      continue
    elif bet_input==0:
      print("You have to bet some amount.\n")
      continue

    bet=str(input("enter bet on the die whether the result will be under 3 , above 3 or exactly 3: \n"))
    if bet not in ["under 3","above 3","exactly 3"]:
      print("You have to choose between under 3 , above 3 or exactly 3 .\n")
      continue
    else:
        print("Bet saved")

    if bet=="quit":
        with open("wallet.txt","w")as file:
            file.write(cash)
            break
            
    time.sleep(0.5)
    print('rolling die')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')

    choices=['1','2','3','4','5','6']
    die=int(random.choice(choices))

    if die < 3:
      output="under 3"
      

    elif die > 3:
      output="above 3"
      

    elif die==3:
      output="exact 3"
      


    if bet == output:
      print("Congrats , you WON the bet ! .\n")
      cash= int(cash + bet_input)
      print(f"Your balance is now {cash} .\n")
      continue
    elif bet != output:
      print("Oops , You LOST this bet ! .\n")
      cash= int(cash - bet_input)
      print(f"Your balance is now {cash} .\n")
      continue


    if cash==0:
      print("You cannot bet more , You have lost the game")
      print("Resetting money......")
      cash=100
      print("Money setback to 100... , Restart to play again")
    break



    




   
