import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(2)

# Parameters
circle_radius = 30
circle_count = 6
circle_spacing = 80  # Horizontal shift

# Draw shifted circles
x_start = -((circle_count - 1) * circle_spacing) // 2  # Centering
y_pos = 0
circle_centers = []

for i in range(circle_count):
    x = x_start + i * circle_spacing
    circle_centers.append((x, y_pos))
    
    # Move to position without drawing
    pen.penup()
    pen.goto(x, y_pos - circle_radius)  # Adjust for turtle drawing circle from bottom
    pen.pendown()
    
    pen.circle(circle_radius)

# Draw a line connecting all circle centers
pen.color("red")
pen.penup()
pen.goto(circle_centers[0])
pen.pendown()

for center in circle_centers[1:]:
    pen.goto(center)

# Hide turtle and finish
pen.hideturtle()
screen.mainloop()
