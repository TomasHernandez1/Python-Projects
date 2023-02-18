import turtle
import winsound
import keyboard

def PongGame():
    A=B=0

    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Left 
    left = turtle.Turtle()
    left.speed(0)
    left.shape("square")
    left.color("white")
    left.shapesize(stretch_wid=5, stretch_len=1)
    left.penup()
    left.goto(-350, 0)

    #right
    right = turtle.Turtle()
    right.speed(0)
    right.shape("square")
    right.color("white")
    right.shapesize(stretch_wid=5, stretch_len=1)
    right.penup()
    right.goto(350, 0)

    #ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2

    #score
    score = turtle.Turtle()
    score.speed(0)
    score.penup()
    score.goto(-10, 270)
    score.color("white")
    score.hideturtle()
    score.write("Player 1: 0   Player 2: 0", align="center")

    # move left
    def left_up():
        left.sety(left.ycor()+20)
        if left.ycor() > 250:
            left.sety(left.ycor()-20)

    def left_down():
        left.sety(left.ycor()-20)
        if left.ycor() < -240:
            left.sety(left.ycor()+20)

    # move right
    def right_up():
        right.sety(right.ycor()+20)
        if right.ycor() > 250:
            right.sety(right.ycor()-20)

    def right_down():
        right.sety(right.ycor()-20)
        if right.ycor() < -240:
            right.sety(right.ycor()+20)

    # keyboard bindings
    wn.listen()
    wn.onkeypress(left_up, "w")
    wn.onkeypress(left_down, "s")
    wn.onkeypress(right_up, "Up")
    wn.onkeypress(right_down, "Down")

    # main loop
    while True:
        if keyboard.is_pressed("Escape"):
            wn.exitonclick()
            break
        else:
            wn.update()

            # ball moving
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # borders check
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
                winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

            if ball.ycor() < -280:
                ball.sety(-280)
                ball.dy *= -1
                winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

            if ball.xcor() > 380:
                ball.goto(0,0)
                ball.dx *= -1
                A+=1
                score.clear()
                score.write("Player 1: {}   Player 2: {}".format(A,B), align="center")       
                
            if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx *= -1
                B+=1
                score.clear()
                score.write("Player 1: {}   Player 2: {}".format(A,B), align="center")

            # ball collision
            rightTop = right.ycor() + 50
            rightBottom = right.ycor() - 50
            if ball.xcor() > 330:
                if ball.ycor() > rightBottom and ball.ycor() < rightTop:
                    ball.setx(330)
                    ball.dx *= -1
                    winsound.PlaySound("boing2.wav", winsound.SND_ASYNC)
                    ball.dx += 0.05
                    ball.dy += 0.05

            leftTop = left.ycor() + 50
            leftBottom = left.ycor() - 50
            if ball.xcor() < -330:
                if ball.ycor() > leftBottom and ball.ycor() < leftTop:
                    ball.setx(-330)
                    ball.dx *= -1
                    winsound.PlaySound("boing2.wav", winsound.SND_ASYNC)
                    ball.dx += 0.05
                    ball.dy += 0.05
        
