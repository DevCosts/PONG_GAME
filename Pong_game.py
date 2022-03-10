import turtle


# create window

wn = turtle.Screen()
wn.title("Pong by MaTT")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Scoreboard

score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # animation speed ( maxed)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)  # start


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # animation speed ( maxed)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # size of paddle
paddle_b.penup()
paddle_b.goto(350, 0)  # start


# Ball
ball = turtle.Turtle()
ball.speed(0)  # animation speed ( maxed)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)  # start
ball.dx = 0.1 # seperates ball parametrs by pixels
ball.dy = -0.1 # seperates ball parametrs by pixels ( set speed )


# Scorring / PEN

pen = turtle.Turtle()
pen.speed(0) 
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier" ,24, "normal"))



# Functions
def paddle_a_up():
  y = paddle_a.ycor()  # set start point
  y += 20  # add 20px to up
  paddle_a.sety(y)  # new y

def paddle_a_down():
  y = paddle_a.ycor() # set start point
  y -= 20 # add 20px to up
  paddle_a.sety(y) # new y 
  
def paddle_b_up():
  y = paddle_b.ycor()  # set start point
  y += 20  # add 20px to up
  paddle_b.sety(y)  # new y

def paddle_b_down():
  y = paddle_b.ycor() # set start point
  y -= 20 # add 20px to up
  paddle_b.sety(y) # new y 
  
  
  
# Keyboard binding

wn.listen() # get keyborad input
wn.onkeypress(paddle_a_up, "w") # wen user press w call function paddle a up
wn.onkeypress(paddle_a_down, "s") # wen user press s call function paddle a down
wn.onkeypress(paddle_b_up, "Up") # wen user press Up (arrow key) call function paddle a up
wn.onkeypress(paddle_b_down, "Down") # wen user press Down (arrow key) call function paddle a down

# main game looop
while True:
  wn.update()  # updates Screen
  
  
  # Move the ball 
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  
  # Border checking
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
    
  if ball.ycor() < -280:
    ball.sety(-280)
    ball.dy *= -1
  
  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier" ,24, "normal"))

    
  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier" ,24, "normal"))
    
    
    
    
  # Paddle and Ball collisions
  
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+ 40 and ball.ycor() > paddle_b.ycor() - 40):
    ball.setx(340)
    ball.dx *= -1
    
  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+ 40 and ball.ycor() > paddle_a.ycor() - 40):
    ball.setx(-340)
    ball.dx *= -1    