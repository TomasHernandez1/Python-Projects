import random

def RPSGame():
    c_score = p_score = computer = 0
    
    while player := input("choose between Rock, Paper or Scissors (0 to exit): ").lower():
        if player != "rock" and player != "paper" and player != "scissors" and player != "0":
            print("please enter a valid input")
        else:
            if player=="0":
                print("final score-> Player: {} Computer: {}".format(p_score, c_score))
                if p_score > c_score:
                    print("you win!")
                elif p_score < c_score:
                    print("you lose :()")
                break
            else:
                RPS = ['rock', 'paper', 'scissors']
                computer = random.choice(RPS)
                print("computer choose " + computer)

                if player=="rock":
                    if computer=="scissors":
                        print("you win")
                        p_score+=1
                    elif computer=="paper":
                        print("you lose")
                        c_score+=1
                if player=="paper":
                    if computer=="rock":
                        print("you win")
                        p_score+=1
                    elif computer=="scissors":
                        print("you lose")
                        c_score+=1
                if player=="scissors":
                    if computer=="paper":
                        print("you win")
                        p_score+=1
                    elif computer=="rock":
                        print("you lose")
                        c_score+=1
                
                if player==computer:
                    print("tie!")

                print("Player: {} Computer: {}".format(p_score, c_score))
    
