import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)    


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)  


# Keyboard Binding
wn.listen()
wn.onkey(paddleA_up, "w")
wn.onkey(paddleA_down, "s")
wn.onkey(paddleB_up, "Up")
wn.onkey(paddleB_down, "Down")



# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1   
        scoreA += 1
        pen.clear() 
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB) , align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  
        scoreB += 1
        pen.clear()         
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB) , align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball conditions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1   
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)     