import turtle

def plot(x, y):
    turtle.goto(x, y)
    turtle.dot(3, "black")

def bresenham_line(x1, y1, x2, y2):
    x1, y1, x2, y2 = int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2))
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    x, y = x1, y1

    if dx >= dy:
        err = dx / 2.0
        while x != x2:
            plot(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            plot(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    plot(x, y)


# Example: Remove unwanted default line drawing
start_x, start_y = int(input("Enter start x: ")), int(input("Enter start y: "))
end_x, end_y = int(input("Enter end x: ")), int(input("Enter end y: "))


# Setup Turtle
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.bgcolor("white")
turtle.setworldcoordinates(-200, -200, 200, 200)
turtle.penup()
turtle.bgcolor("white")


# Draw reference line with turtle pen (optional, for comparison)
turtle.goto(start_x, start_y)
turtle.pendown()
turtle.goto(end_x, end_y)
turtle.penup()

# Now draw Bresenham line
bresenham_line(start_x, start_y, end_x, end_y)

turtle.done()
