import turtle

# t = turtle.Turtle()
turtle.bgcolor("#4c00b0")
turtle.pencolor("#ffffff")

# 721 AB

# A
turtle.penup()
turtle.setx(-110)
turtle.sety(0)
turtle.pensize(20)
turtle.write(
    "A",
    font=("Verdana", 100, "bold")
)
turtle.penup()

# 2
turtle.setx(0)
turtle.sety(0)
turtle.pensize(20)
turtle.pendown()
turtle.write(
    "2",
    font=("Verdana", 100, "bold")
)

# B
turtle.penup()
turtle.setx(110)
turtle.sety(0)
turtle.pensize(20)
turtle.pendown()
turtle.write(
    "B",
    font=("Verdana", 100, "bold")
)

# 7
turtle.penup()
turtle.setx(0)
turtle.sety(130)
turtle.pensize(20)
turtle.pendown()
turtle.write(
    "7",
    font=("Verdana", 100, "bold")
)

# 1
turtle.penup()
turtle.setx(0)
turtle.sety(-130)
turtle.pensize(20)
turtle.pendown()
turtle.write(
    "1",
    font=("Verdana", 100, "bold")
)

turtle.Screen().exitonclick()