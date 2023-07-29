from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

BG_COLOR = "black"
GAME_TITLE = "Ping Pong Game"
PADDLE_UP = "Up"
PADDLE_DOWN = "Down"
RISE_THE_PADDLE = "w"
LOWER_THE_PADDLE = "s"

my_screen = Screen()
my_screen.bgcolor(BG_COLOR)
my_screen.setup(width=800,height=600)
my_screen.title(GAME_TITLE)
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
game_scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(r_paddle.go_up, PADDLE_UP)
my_screen.onkey(r_paddle.go_down, PADDLE_DOWN)
my_screen.onkey(l_paddle.go_up, RISE_THE_PADDLE)
my_screen.onkey(l_paddle.go_down, LOWER_THE_PADDLE)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        game_scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        game_scoreboard.r_point()


my_screen.exitonclick()