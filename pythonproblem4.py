from turtle import *

Cuff = Turtle()

Link = Turtle()

Cuff.color("blue")
Link.color("green")
Cuff.pensize(7)
Link.pensize(7)
Cuff.speed(0)
Link.speed(0)
Cuff.shape("turtle")
Link.shape("turtle")

def drawEquilateralTriangle():
	for x in range (1):
		Cuff.forward(200)
		Cuff.left(120)
		Cuff.forward(200)
		Cuff.left(120)
		Cuff.forward(200)

for x in range (2):
	Link.circle(25)

drawEquilateralTriangle()
drawEquilateralTriangle()
drawEquilateralTriangle()
drawEquilateralTriangle()
drawEquilateralTriangle()
drawEquilateralTriangle()
drawEquilateralTriangle()

mainloop()