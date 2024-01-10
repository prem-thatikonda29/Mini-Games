import random

decision = ""  # Global variable for user decision
comp_decision = ""  # Global variable for computer decision
user_score = 0
comp_score = 0

opp_teams = ["Crocodiles", "DoFlamingos", "Magellen Eleven", "Moria Shadows", "Dragons", "Mermaid Lords"]
opp_team = random.choice(opp_teams)
print("""Welcome to the game of cricket!
Enter the name of your team""")
name = input("> ")
print("Enter your name.")
user = input("> ")
print(f"{user}\'s {name} is playing against {opp_team}!")

def toss():
    global decision, comp_decision  # Declare the variables as global within the function
    print("Let\'s do the toss")
    choice = input("Choose : odd or even : ")

    if choice.lower() == "odd" or choice.lower() == "even":
        choice_num = int(input("Enter a number from 0 - 6: "))
        if choice_num > 6 or choice_num < 0:
            print("Please enter a number between 0 and 6")
            choice_num = int(input("> "))
            choice_comp = random.randint(0, 6)
            print("Computer chose: " + str(choice_comp))
            tosss = int(choice_num) + int(choice_comp)
            if choice.lower() == "odd":
                if tosss % 2 == 0:
                    print('Sorry you lost!')
                    comp_decision = random.choice(["Bat", "Bowl"])
                    print("Computer chose to: " + comp_decision)
                else:
                    print("Congrats you won! \nWhat would you like to choose?")
                    decision = input("Bat or Bowl: ")
            else:
                if tosss % 2 == 0:
                    print("Congrats you won! \nWhat would you like to choose?")
                    decision = input("Bat or Bowl: ")
                else:
                    print('Sorry you lost!')
                    comp_decision = random.choice(["Bat", "Bowl"])
                    print("Computer chose to: " + comp_decision)
        else:
            choice_comp = random.randint(0, 6)
            print("Computer chose: " + str(choice_comp))
            tosss = int(choice_num) + int(choice_comp)
            if choice.lower() == "odd":
                if tosss % 2 == 0:
                    print('Sorry you lost!')
                    comp_decision = random.choice(["Bat", "Bowl"])
                    print("Computer chose to: " + comp_decision)
                else:
                    print("Congrats you won! \nWhat would you like to choose?")
                    decision = input("Bat or Bowl: ")
            else:
                if tosss % 2 == 0:
                    print("Congrats you won! \nWhat would you like to choose?")
                    decision = input("Bat or Bowl: ")
                else:
                    print('Sorry you lost!')
                    comp_decision = random.choice(["Bat", "Bowl"])
                    print("Computer chose to: " + comp_decision)
    else:
        print("ODD OR EVEN?!")
        toss()

def user_bat():
    global user_score, comp_score
    if decision.lower() == "bat" or comp_decision.lower() == "bowl":
        print("You are Batting..\n")
        while True:
            user_input = int(input("Enter a number between 0 to 6: "))
            comp_input = random.randint(0, 6)
            if user_input > 6 or user_input < 0:
                print("Enter a valid number batsman!")
                continue
            if user_input == comp_input:
                print("Computer chose: "+str(comp_input))
                print("You are out! HOWZATT! \n")
                print("Score is :"+str(user_score))
                target = (user_score+1)
                print("Target is: "+str(target))
                break
            else:
                user_score = user_score+user_input
                print("Computer chose: "+str(comp_input))
                print("Score is :"+str(user_score)+"\n")
        print("\nYou are now Bowling..")

        while True:
            if comp_score >= target:
                print(f"{opp_team} won!")
                exit()
            else:
                comp_input = random.randint(0, 6)
                user_input = int(input("Enter a number between 0 to 6: "))
                if user_input > 6 or user_input < 0:
                    print("Enter a valid number batsman!")
                    continue
                if user_input == comp_input:
                    print("Computer chose: "+str(comp_input))
                    print("Computer is out! \n")
                    print("Score is :"+str(comp_score))
                    print(f"{user} won!")
                    exit()
                else:
                    comp_score = (comp_score+comp_input)
                    print("Computer chose: "+str(comp_input))
                    print("Score is :"+str(comp_score)+"\n")

def user_bowl():
    global user_score, comp_score, decision, comp_decision
    target = 0  # Declare target within the function
    if decision.lower() == "bowl" or comp_decision.lower() == "bat":
        print("You are Bowling..\n")
        while True:
            user_input = int(input("Enter a number between 0 to 6: "))
            if user_input > 6 or user_input < 0:
                print("Enter a valid number bowler!")
                continue
            comp_input = random.randint(0, 6)
            if user_input == comp_input:
                print("Computer chose: "+str(comp_input))
                print("Computer is out! \n")
                print("Score is :"+str(comp_score))
                target = (comp_score + 1)  # Fix: calculate target based on comp_score
                print("Target is: "+str(target))
                break
            else:
                comp_score = (comp_score+comp_input)
                print("Computer chose: "+str(comp_input))
                print("Score is :"+str(comp_score)+"\n")
        print("\nYou are now Batting..Target is "+str(target))
        while True:
            if user_score >= target:
                print(f"{user} Won!")
                exit()
            else:
                comp_input = random.randint(0, 6)
                user_input = int(input("Enter a number between 0 to 6: "))
                if user_input > 6 or user_input < 0:
                    print("Enter a valid number batsman!")
                    continue
                if user_input == comp_input:
                    print("Computer chose: "+str(comp_input))
                    print("Computer is out! \n")
                    print("Score is :"+str(user_score))
                    print(f"{user} won!")
                    exit()
                else:
                    user_score = (user_score + user_input)
                    print("Computer chose: "+str(comp_input))
                    print("Score is :"+str(user_score)+"\n")

def main():
    toss()
    user_bat()
    user_bowl()


if __name__=="__main__":
    main()
