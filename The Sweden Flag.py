from turtle import *

speed(0)
setup(800, 500)
bgcolor("#335cff")

penup()
goto(-400, -37)
pendown()

color("yellow")
begin_fill()
forward(800)
left(90)
forward(75)
left(90)
forward(800)
end_fill()

penup()
goto(-100, -250)
pendown()

begin_fill()
forward(75)
right(90)
forward(500)
right(90)
forward(75)
end_fill()

hideturtle()
