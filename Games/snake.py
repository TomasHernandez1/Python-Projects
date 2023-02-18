import random
from tkinter import *

def SnakeGame():
    WIDTH = 500
    HEIGHT = 500
    SPEED = 50  
    SQUARE = 25
    SNAKE_COLOR = "#00FF00"
    FOOD_COLOR = "#FF0000"
    BG_COLOR = "#000000"

    class Snake:
        def __init__(self):
            self.coordinates = [0,0]
            self.body_size = 3

            for i in range(0, 3):
                canvas.create_rectangle(0,0, SQUARE, SQUARE, fill=SNAKE_COLOR)        
            
    class Food:
        pass


    window = Tk()
    window.title("Snake")
    window.resizable(False, False)

    score = 0
    direction = 'right'

    label = Label(window, text="score: {}".format(score), font=(40))
    label.pack()

    canvas = Canvas(window, background=BG_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()

    snake = Snake()

    window.mainloop()