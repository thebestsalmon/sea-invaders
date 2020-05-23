# Space Invaders
import turtle
import os
import math
import random


# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
border_pen.hideturtle()

# player
player = turtle.Turtle()
player.color("pink")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Enemy
# enemy number
number_of_enemies = 5
# enemy list
enemies = []

# Add enemy
for i in range(number_of_enemies):
    # Create
    enemies.append(turtle.Turtle())


for enemy in enemies:
    enemy.color("yellow")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


enemyspeed = 2
