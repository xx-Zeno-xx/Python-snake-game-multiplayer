from turtle import Screen
import time
from snake2 import Snake2
from food import Food
from scoreboard import Scoreboard1, Scoreboard2
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)
user1 = screen.textinput(title="Player 1", prompt="Enter your name")
user1_color = screen.textinput(title='Player 1', prompt="Enter color")
user2 = screen.textinput(title='Player 2', prompt="Enter your name")
user2_color = screen.textinput(title='Player 2', prompt="Enter color")

snake2 = Snake2(user1_color)
snake = Snake(user2_color)
food = Food()
food2 = Food()

scoreboard1 = Scoreboard1(user1)
scoreboard2 = Scoreboard2(user2)

screen.listen()
screen.onkey(fun=snake2.up, key="Up")
screen.onkey(fun=snake2.right, key="Right")
screen.onkey(fun=snake2.left, key="Left")
screen.onkey(fun=snake2.down, key="Down")
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.down, key="s")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake2.move()
    snake.move()

    if snake2.head.distance(food.food_obj) < 18:
        snake2.extend()
        if snake2.new_color == food.food_color:
            scoreboard1.increase_score(point=5)
        else:
            scoreboard1.increase_score(point=1)
        food.refresh()
    elif snake2.head.distance(food2.food_obj) < 18:
        snake2.extend()
        if snake2.new_color == food2.food_color:
            scoreboard1.increase_score(point=5)
        else:
            scoreboard1.increase_score(point=1)
        food2.refresh()
    elif snake.head.distance(food.food_obj) < 18:
        snake.extend()
        if snake.new_color == food.food_color:
            scoreboard2.increase_score(point=5)
        else:
            scoreboard2.increase_score(point=1)
        food.refresh()
    elif snake.head.distance(food2.food_obj) < 18:
        snake.extend()
        if snake.new_color == food2.food_color:
            scoreboard2.increase_score(point=5)
        else:
            scoreboard2.increase_score(point=1)
        food2.refresh()

    if snake2.head.xcor() >= 300:
        snake2.head.goto(x=-300, y=snake2.head.ycor())
    elif snake2.head.xcor() <= -300:
        snake2.head.goto(x=300, y=snake2.head.ycor())
    if snake2.head.ycor() >= 300:
        snake2.head.goto(x=snake2.head.xcor(), y=-300)
    elif snake2.head.ycor() <= -300:
        snake2.head.goto(x=snake2.head.xcor(), y=300)

    if snake.head.xcor() >= 300:
        snake.head.goto(x=-300, y=snake.head.ycor())
    elif snake.head.xcor() <= -300:
        snake.head.goto(x=300, y=snake.head.ycor())
    if snake.head.ycor() >= 300:
        snake.head.goto(x=snake.head.xcor(), y=-300)
    elif snake.head.ycor() <= -300:
        snake.head.goto(x=snake.head.xcor(), y=300)

    # for segment in snake.segments[1:]:
    #     if snake2.head.distance(segment) < 10:
            # is_game_on = False
            # scoreboard.game_over()

screen.exitonclick()
