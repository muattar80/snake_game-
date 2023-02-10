from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.all_cars = []

    def create_new_car(self):
        obey = random.randint(1, 6)
        if obey == 1:
            tim = Turtle("square")
            tim.pu()
            tim.shapesize(stretch_wid=1, stretch_len=2)
            tim.color(random.choice(COLORS))
            tim.goto(280, random.randint(-250, 250))

            self.all_cars.append(tim)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
