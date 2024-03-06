from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("The Pong Game")
screen.tracer(0)

R_paddle = Paddle(350, 0)
L_paddle = Paddle(-350,0)
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkeypress(R_paddle.up, 'Up')
screen.onkeypress(R_paddle.down, 'Down')
screen.onkeypress(L_paddle.up, 'w')
screen.onkeypress(L_paddle.down, 's')

game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_wall()

    if ball.distance(R_paddle) <50 and ball.xcor() >320 or ball.distance(L_paddle) <50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 400 :
        ball.restart()
        score.lpoint()

    if ball.xcor() < -400:
        ball.restart()
        score.rpoint()




screen.exitonclick()