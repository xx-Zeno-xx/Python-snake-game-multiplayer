import turtle
from turtle import Turtle
import random

turtle.colormode(255)

color_list = ["red", "green", "blue", "white", "purple", "pink", "orange", "violet", "cyan",
              "yellow", "lightgreen", "skyblue", "grey"]


class Food:

    def __init__(self):
        self.food_obj = Turtle("circle")
        self.food_obj.penup()
        self.food_obj.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.food_obj.speed("fastest")
        self.food_color = ""
        self.refresh()

    def refresh(self):
        self.food_obj.color(self.food_colors())
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.food_obj.goto(random_x, random_y)

    def food_colors(self):
        a = random.choice(color_list)
        self.food_color = a
        return a


