from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 260)
        self.clear()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.write(f"Score {self.l_score} : {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        if self.r_score > self.l_score:
            self.n= "left_player"
        else:
            self.n= "right_player"
        self.write(f"Game Over - '{self.n}wins' ", False, align=ALIGNMENT, font=FONT)


    def increase_l(self):
        self.clear()
        self.l_score += 1
        self.update()

    def increase_r(self):
        self.clear()
        self.r_score += 1
        self.update()

