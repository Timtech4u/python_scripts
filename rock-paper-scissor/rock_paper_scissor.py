
print("\nPlay Rock Paper Scissors.")

while(1):
    print("Enter your choice in lower cases (rock/paper/scissor): ")
    rock="rock"
    paper="paper"
    scissor="scissor"
    human= input()
    if human==rock:
        human=rock
        print("You chose " + rock + ".")
    elif human==paper:
        human=paper
        print("You chose " + paper + ".")
    elif human==scissor:
        human=scissor
        print("You chose " + scissor + ".")
    else:
        print("invalid choice")



    import random
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer_choice="rock"
    elif computer_choice==2:
        computer_choice="paper"
    elif computer_choice==3:
        computer_choice="scissor"





    if computer_choice=="rock" and human=="rock":
        print("Its a Tie!")
    elif computer_choice=="rock" and human=="paper":
        print("You won!")
    elif computer_choice=="rock" and human=="scissors":
        print("You lose!")

    elif computer_choice=="paper" and human=="paper":
        print ("Its a Tie!")
    elif computer_choice=="paper" and human=="rock":
        print ("You lose!")
    elif computer_choice=="paper" and human=="scissor":
        print ("You won!")

    elif computer_choice=="scissor" and human=="paper":
        print ("You lose!")
    elif computer_choice=="scissor" and human=="rock":
        print ("You won!")
    elif computer_choice=="scissor" and human=="scissor":
        print ("Its a Tie!")
    elif computer_choice=="scissor" and human=="paper":
        print ("You lose!")
    elif computer_choice=="scissor" and human=="rock":
        print ("You won!")
    elif computer_choice=="scissor" and human=="scissor":
        print ("Its a Tie!")

    print("Computer chose " + computer_choice + ".")

    print("\n\nPlay Rock Paper Scissors again...")

