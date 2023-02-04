from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 275)
        self.color("white")
        self.write(f"score: {self.score}", align="center", font=("Arial", 15, 'normal'))
        self.hideturtle()
        self.score += 1

    def increase_score(self):
        # self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align="center", font=("Arial", 15, 'normal'))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Courier", 20, "normal"))

