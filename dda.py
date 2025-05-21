import turtle

# Plotting a point
def plot(x, y, color="blue"):
    turtle.goto(x, y)
    turtle.dot(4, color)

# DDA line drawing algorithm using dot plotting
def dda_line(x1, y1, x2, y2):
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        plot(round(x), round(y), color="blue")
        x += x_inc
        y += y_inc

# Input from user
start_x = int(input("Enter start x: "))
start_y = int(input("Enter start y: "))
end_x = int(input("Enter end x: "))
end_y = int(input("Enter end y: "))

# Turtle setup
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")
turtle.setworldcoordinates(-200, -200, 200, 200)
turtle.penup()

# Draw reference line using turtle pen (actual line)
turtle.color("red")
turtle.goto(start_x, start_y)
turtle.pendown()
turtle.goto(end_x, end_y)
turtle.penup()

# Draw DDA line using dots
turtle.color("blue")
dda_line(start_x, start_y, end_x, end_y)


turtle.done()
