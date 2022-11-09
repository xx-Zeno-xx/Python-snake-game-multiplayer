from turtle import Turtle

STARTING_POSITION = [(0, 50), (-20, 50), (-40, 50)]
NORMAL = 17


class Snake:

    def __init__(self, s_color):
        self.segments = []
        self.create_snake(s_color)
        self.head = self.segments[0]
        self.new_color = s_color

    def create_snake(self, s_color):
        for position in STARTING_POSITION:
            self.add_segment(position, s_color)

    def add_segment(self, position, s_color):
        new_segment = Turtle("square")
        new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8)
        new_segment.penup()
        new_segment.color(s_color)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position(), self.new_color)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(NORMAL)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

