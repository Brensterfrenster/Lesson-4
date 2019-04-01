from turtle import *

ft = Turtle()

def petal(t, r, angle):
	for t in range(2):
		t.circle(r-angle)
		t.circle(180-angle)

def flower(t, r, angle):
	for t in range(n):
		petal(t, r, angle)
		t-left(360.0/n)

def move(t, length):
	window = turtle.Screen()
	window.bgcolor("Yellow")
	t.pu()
	t.fd(length)
	t.pd()

ft = Turtle()
ft = speed(8)

ft.color("green")
ft.shape("turtle")
move(sum, -150)
sum.begin_fill()
flower(sum, 7, 60.0, 60.0)
sum.end_fill()

sum.color("red")
move(sum, 150)
flower(sum, 10, 40.0, 80.0)

screen = Screen()
screen.bgcolor("yellow")

mainloop()