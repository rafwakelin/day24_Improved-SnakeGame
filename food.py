from turtle import Turtle
import random


class Food(Turtle):
    """Creates a piece of food with the attributes and methods of the super class Turtle"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.color("DarkGreen")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        """Creates a new food once the snake eats the previous one"""
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)
