import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
x=random.randrange(1,100)
y=random.randrange(1,100)

michelangelo.forward(x)
leonardo.forward(y)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(0,10):
  x=random.randrange(0,10)
  y=random.randrange(0,10)
  michelangelo.forward(x)
  leonardo.forward(y)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# Part B - complete part B here

answer=[3,4,6,9,12]
michelangelo.goto(0,-60) #i made it centered here
michelangelo.down()
for i in answer: 
  for _ in range(i):
    michelangelo.left(360/i)
    michelangelo.forward(50)
  michelangelo.clear()
  

window.exitonclick()
