from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_CREATE_RATE = 6


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    
    def create_car(self):
        if random.randint(1, CAR_CREATE_RATE) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def remove_offscreen_cars(self):
        for car in self.all_cars:
            if car.xcor() < -300:
                car.hideturtle()
                self.all_cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

        


        



