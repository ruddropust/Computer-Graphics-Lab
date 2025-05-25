import turtle

def draw_axes():
    axis = turtle.Turtle()
    axis.speed(0)
    axis.color("gray")
    axis.penup()
    axis.goto(-200, 0)  # X-axis from left to right
    axis.pendown()
    axis.goto(200, 0)
    axis.penup()
    axis.goto(0, -200)  # Y-axis from bottom to top
    axis.pendown()
    axis.goto(0, 200)
    axis.hideturtle()

def draw_circle_midpoint(xc, yc, radius):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    
    x = 0
    y = radius
    p = 1 - radius

    def plot_circle_points(xc, yc, x, y):
        points = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ]
        for point in points:
            t.goto(point)
            t.dot(3, "blue")

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

def main():
    screen = turtle.Screen()
    screen.setup(width=700, height=700)
    screen.title("Midpoint Circle Drawing Algorithm")

    draw_axes()

    # Get user input for center and radius
    try:
        center_x = int(screen.numinput("Center X", "Enter center X coordinate:", default=0, minval=-200, maxval=200))
        center_y = int(screen.numinput("Center Y", "Enter center Y coordinate:", default=0, minval=-200, maxval=200))
        radius = int(screen.numinput("Radius", "Enter radius of the circle:", default=100, minval=1, maxval=180))
    except TypeError:
        print("User cancelled input. Exiting...")
        turtle.bye()
        return

    draw_circle_midpoint(center_x, center_y, radius)

    turtle.done()

if __name__ == "__main__":
    main()
