from turtle import *

cuff = Turtle()

cuff.color("purple")
cuff.pensize(2)
cuff.speed(9)
cuff.shape("turtle")

for x in range(4):
	cuff.forward(100)
	cuff.left(90)
	cuff.forward(100)
	cuff.left(90)
	cuff.forward(100)
	cuff.left(90)
	cuff.forward(100)
	cuff.left(90)

mainloop()