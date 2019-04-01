from turtle import *

franklin = Turtle()

franklin.color("green")
franklin.pensize(7)
franklin.speed(9)
franklin.shape("turtle")

for x in range (1):
	franklin.forward(80)
	franklin.left(50)
	franklin.forward(200)
	franklin.right(150)
	franklin.forward(50)
	franklin.circle(25)
	franklin.backward(30)
	franklin.circle(50)

mainloop()