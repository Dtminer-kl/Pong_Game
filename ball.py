from turtle import Turtle

START_POS = (0,0)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(START_POS)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_wall(self):
        self.y_move *=-1

    def bounce_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def restart(self):
        self.goto(START_POS)
        self.bounce_paddle()