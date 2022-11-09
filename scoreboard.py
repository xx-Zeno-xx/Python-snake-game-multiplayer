from turtle import Turtle


class Scoreboard1(Turtle):

    def __init__(self, player_name):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-230, y=270)
        self.player_name = player_name
        self.write(f"{player_name}: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def increase_score(self, point=1):
        self.score += point
        self.clear()
        self.write(f"{self.player_name}: {self.score}", align="center", font=("Arial", 20, "normal"))


class Scoreboard2(Turtle):

    def __init__(self, player_name):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=220, y=270)
        self.player_name = player_name
        self.write(f"{player_name}: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"{player} Wins!", align="center", font=("Arial", 20, "normal"))

    def increase_score(self, point=0):
        self.score += point
        self.clear()
        self.write(f"{self.player_name}: {self.score}", align="center", font=("Arial", 20, "normal"))

