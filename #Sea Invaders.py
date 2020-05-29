# Sea Invaders
import turtle
import math
import winsound



# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Sea Invaders")
wn.bgpic("bg.gif")
wn.tracer(0)


# Shapes
wn.register_shape("enemy.gif")
wn.register_shape("player.gif")
wn.register_shape("bubble.gif")

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
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-290, 280)
scorerestring = "Score: {}".format(score)
score_pen.write(scorerestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# player
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 0

# Enemy
# enemy number
number_of_enemies = 30
# enemy list
enemies = []

# Add enemy
for i in range(number_of_enemies):
    # Create
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0


for enemy in enemies:
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50*enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # update number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0


enemyspeed = 0.1


# player's bullet
bullet = turtle.Turtle()
bullet.shape("bubble.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 3

# bullet state
bulletstate = "ready"

# player movement
def move_left():
    player.speed = -2


def move_right():
    player.speed = 2


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = - 280
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        fname = "bubbleeffect.wav"
        winsound.PlaySound(fname, winsound.SND_FILENAME)
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
wn.listen()
wn.onkey(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# loop
while True:

    wn.update()
    move_player()

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
            hname = "hiteffect.wav"
            winsound.PlaySound(hname, winsound.SND_FILENAME)
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            

            # Update score
            score += 10
            scorerestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorerestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            for enemy in enemies:
                enemy.hideturtle()
            GO = turtle.Turtle()
            GO.speed(0)
            GO.color("red")
            GO.penup()
            GO.setposition(-70, 0)
            GO.hideturtle()
            GOrestring = "Game Over"
            GO.write(GOrestring, False, align="left", font=("Arial", 20, "normal"))
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


