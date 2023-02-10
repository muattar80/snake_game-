from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        # self.write(f"Level: {self.score} ", align="center", font=("Courier", 40, 'normal'))
        self.level()

    def level(self):
        self.clear()
        # self.score += 1
        self.pu()
        self.goto(-220, 270)
        # self.pu()
        self.write(f"Level: {self.score} ", align="center", font=("Courier", 20, 'normal'))
        self.score += 1

    def over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Courier", 80, 'normal'))
