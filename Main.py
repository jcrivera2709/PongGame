# Simple Pong Game in Python 3
# By Jose Rivera

import turtle
import winsound

win = turtle.Screen()
win.title("Pong By Jose")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions for Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    if y > 240:
        y = 250
        paddle_a.sety(y)
    else:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y < -220:
        y = -240
        paddle_a.sety(y)
    else:
        y -= 20
        paddle_a.sety(y)


# Functions for Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    if y > 240:
        y = 250
        paddle_b.sety(y)
    else:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y < -220:
        y = -240
        paddle_b.sety(y)
    else:
        y -= 20
        paddle_b.sety(y)


# KeyBoard Binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    win.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Y Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Border X Check
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound('C:\\Users\\15613\\PycharmProjects\\Pong\\applause2_x.wav', winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound('C:\\Users\\15613\\PycharmProjects\\Pong\\applause2_x.wav', winsound.SND_ASYNC)

    # Paddle and Ball Collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('C:\\Users\\15613\\PycharmProjects\\Pong\\bounce.wav', winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('C:\\Users\\15613\\PycharmProjects\\Pong\\bounce.wav', winsound.SND_ASYNC)
