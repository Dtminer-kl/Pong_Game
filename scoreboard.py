from turtle import Turtle
FONT = ("Courier", 80, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update()


    def update(self):
        self.clear()
        self.goto(-100, 190)
        self.write(arg=self.lscore, align='center', font=FONT)
        self.goto(100, 190)
        self.write(arg=self.rscore, align='center', font=FONT)

    def lpoint(self):
        self.lscore +=1
        self.update()


    def rpoint(self):
        self.rscore +=1
        self.update()