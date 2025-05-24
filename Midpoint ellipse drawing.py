import turtle

def draw_axes(center_x, center_y, screen_width=400, screen_height=300):
    turtle.color("gray")
    turtle.pensize(1)
    turtle.penup()

    # Draw X-axis
    turtle.goto(-screen_width // 2, center_y)
    turtle.pendown()
    turtle.goto(screen_width // 2, center_y)
    turtle.penup()

    # Draw Y-axis
    turtle.goto(center_x, -screen_height // 2)
    turtle.pendown()
    turtle.goto(center_x, screen_height // 2)
    turtle.penup()

    turtle.color("blue")  # Reset to default color

def draw_midpoint_ellipse(a, b, h, k):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    a2 = a * a
    b2 = b * b

    x = 0
    y = b

    # Region 1
    p1 = b2 - (a2 * b) + (0.25 * a2)
    dx = 2 * b2 * x
    dy = 2 * a2 * y

    while dx <= dy:
        plot_ellipse_points(x, y, h, k)
        x += 1
        dx = 2 * b2 * x
        if p1 < 0:
            p1 += dx + b2
        else:
            y -= 1
            dy = 2 * a2 * y
            p1 += dx - dy + b2

    # Region 2
    p2 = (b2 * (x + 0.5) ** 2) + (a2 * (y - 1) ** 2) - (a2 * b2)
    while y >= 0:
        plot_ellipse_points(x, y, h, k)
        y -= 1
        dy = 2 * a2 * y
        if p2 > 0:
            p2 -= dy + a2
        else:
            x += 1
            dx = 2 * b2 * x
            p2 += dx - dy + a2

def plot_ellipse_points(x, y, h, k):
    for dx, dy in [(x, y), (-x, y), (x, -y), (-x, -y)]:
        turtle.goto(h + dx, k + dy)
        turtle.dot(3, "blue")  
try:
    center_x = int(input("Enter center X-coordinate: "))
    center_y = int(input("Enter center Y-coordinate: "))
    major_axis = int(input("Enter length of semi-major axis (a): "))
    minor_axis = int(input("Enter length of semi-minor axis (b): "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    draw_axes(center_x, center_y)
    draw_midpoint_ellipse(major_axis, minor_axis, center_x, center_y)

    screen.mainloop()

except ValueError:
    print("Invalid input. Please enter integer values.")
