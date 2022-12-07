from turtle import Turtle
INITIAL_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Creates the initial body of the snake"""
        self.snake_body = []
        self.create_body()

    def create_body(self):
        """Creates each individual pieces of the initial body"""
        for position in INITIAL_POSITIONS:
            self.big_snake(position)

    def big_snake(self, position):
        """Add a new piece of the snakes body to the list of body pieces"""
        new_piece = Turtle(shape="square")
        new_piece.penup()
        new_piece.color("white")
        new_piece.goto(position)
        self.snake_body.append(new_piece)
        new_piece.showturtle()

    def add(self):
        """Snakes becomes bigger everytime eats a piece of food"""
        self.big_snake(self.snake_body[-1].position())

    def move(self):
        """Moves the snake forward"""
        for piece in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[piece - 1].xcor()
            new_y = self.snake_body[piece - 1].ycor()
            self.snake_body[piece].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self,):
        """Changes the snake heading to North"""
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        """Changes the snake heading to South"""
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        """Changes the snake heading to West"""
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        """Changes the snake heading to East"""
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_body()
        # self.snake_body[0] = self.snake_body[0]



