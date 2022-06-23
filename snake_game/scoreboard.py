from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        with open("new_file.txt") as data:
            self.highest = int(data.read())
        self.hideturtle()
        self.goto(-20, 260)
        self.clear()
        self.pts = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.pts} Highest: {self.highest}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.pts > self.highest:
            self.highest = self.pts
            with open("new_file.txt", mode="w") as data:
                data.write(f"{self.pts}")
        self.pts = 0
        self.update()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.pts += 1
        self.update()