from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 18, "normal")
POSITION = (-270, 270)


class Scoreboard(Turtle):
    """Creates a score board"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(POSITION)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        """Once the snake eats food changes the score and displays the new value"""
        self.clear()
        self.write(arg=f"Score: {self.score}                        Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()




    # def game_over(self):
    #     """Write Game Over in the center of the screen"""
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write(arg="Game Over".upper(), align="center", font=("Courier", 40, "normal"))
