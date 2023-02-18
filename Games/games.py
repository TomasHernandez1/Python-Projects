from pong import PongGame
from snake import SnakeGame
from RPS import RPSGame

while op := input("\nwhat do you want to play? \n 1: Pong \n 2: Snake \n 3: RPS \n 0: exit \n"):
    if op != "1" and op != "2" and op != "3" and op != "0":
            print("please enter a valid input")
    else:
        match op:
            case "1":
                PongGame()
            case "2":
                pass
                SnakeGame()
            case "3":
                pass
                RPSGame()
            case "0":
                print("bye!")
                break