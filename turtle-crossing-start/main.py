import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
player = Player()
# cars = CarManager()
# for x in range(14):
cars = CarManager()
score = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # score.level()
    screen.onkey(player.up, "Up")
    cars.create_new_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            score.over()

    if player.ycor() == 280:
        player.goto(0, -280)
        score.level()
        cars.level_up()

screen.exitonclick()
