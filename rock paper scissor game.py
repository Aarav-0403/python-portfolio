import random
import time
setup_file=open('highscore.txt','a')
setup_file.close()

with open('highscore.txt','r')as file:
     content=file.read()

if content=="":
   highest_streak=0
else:
    highest_streak=int(content.strip())


current_streak=int(0)

print("--- WELCOME TO ROCK~PAPER~SCISSORS ---")
time.sleep(1)
print(f"current highscore={highest_streak}")
time.sleep(1)
print(" lets start! choose either :- ")
time.sleep(1)
print("~rock~")
time.sleep(0.5)
print("~paper~")
time.sleep(0.5)
print("~scissors~")
time.sleep(0.7)

while True:
    player=input(" choose rock , paper or scissors ")
    if player not in["rock", "paper",  "scissors"]:
      print(" sorry , u need to type either rock , paper or scissors or type quit if you want")
    if player==str("quit"):
      break
     
  
    choices=["rock","paper","scissors","quit"]
    computer=random.choice(choices)
    print(" computer is thinking")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(1)
    if player==computer:
     print(" Its a TIE , both choices were same (streak was unaffected) ")

    elif player=="rock":
      if computer=="scissors":
        print(" The bot chose scissors , You WIN ! ")
        current_streak =int(current_streak)+ 1
      else:
        print(" Oops, The bot chose paper , You LOSE ! ")
        break

     
    elif player=="paper":
      if computer=="rock":
         print("The bot chose rock , You WIN ! ")
         current_streak =int(current_streak)+ 1
      else:
        print("Oops, The bot chose scissors , You LOSE ! ")
        break
     
    elif player=="scissor":
      if computer=='paper':
          print("The bot chose paper , You WIN ! ")
          current_streak = int(current_streak) + 1
      else:
        print("Oops , The bot chose rock , You LOSE ! ")
        break


if current_streak > highest_streak:
    with open("highscore.txt","w") as new_file:
        new_file.write(str(current_streak))
        print(f"Your current streak is {current_streak} which is now your NEW HIGHEST STREAK !! ")
        print(" Saving new highscore.... ")
        print("Highscore saved ")
else:
    print(f"Your current streak: {current_streak} could not beat your highest streak :( ")

input("\npress Enter to exit")


     



