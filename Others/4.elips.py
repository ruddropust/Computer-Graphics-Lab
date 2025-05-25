import matplotlib.pyplot as plt

def plot_ellipse_points(xc, yc, x, y, points):
    # 4-way symmetry
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
    ])

def midpoint_ellipse(rx, ry, xc, yc):
    points = []
    x = 0
    y = ry

    # Decision parameter for Region 1
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    # Region 1
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y, points)
        x += 1
        dx = 2 * ry**2 * x
        if p1 < 0:
            p1 += dx + ry**2
        else:
            y -= 1
            dy = 2 * rx**2 * y
            p1 += dx - dy + ry**2

    # Decision parameter for Region 2
    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2

    # Region 2
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y, points)
        y -= 1
        dy = 2 * rx**2 * y
        if p2 > 0:
            p2 += rx**2 - dy
        else:
            x += 1
            dx = 2 * ry**2 * x
            p2 += dx - dy + rx**2

    return points

# --------- USER INPUT ---------
try:
    rx = int(input("Enter x-radius (rx): "))
    ry = int(input("Enter y-radius (ry): "))
    xc = int(input("Enter center x-coordinate (xc): "))
    yc = int(input("Enter center y-coordinate (yc): "))

    # Generate ellipse points
    ellipse_points = midpoint_ellipse(rx, ry, xc, yc)

    # Plotting
    x_vals, y_vals = zip(*ellipse_points)
    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, '.', color='blue')
    plt.plot(xc, yc, 'ro', label='Center')  # Mark the center
    plt.title('Midpoint Ellipse Algorithm')
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

except ValueError:
    print("Invalid input! Please enter integer values.")
