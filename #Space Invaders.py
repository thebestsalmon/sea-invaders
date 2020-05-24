# Space Invaders
import turtle
import os
import math
import random

# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Shapes
turtle.register_shape("enemy.gif")



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

# Score
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorerestring = "Score: %s" %score
score_pen.write(scorerestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

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
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


enemyspeed = 2


# player's bullet
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# bullet state
bulletstate = "ready"

# player movement
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move bullet to the above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


# key bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# loop
while True:

    for enemy in enemies:
        # enemy move
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # enemy back
        if enemy.xcor() > 280:
            # Move enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # Move enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change direction
            enemyspeed *= -1

            # Collision
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update score
            score += 10
            scorerestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorerestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # bullet movement
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #bullet top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"











delay = input("Press enter")
