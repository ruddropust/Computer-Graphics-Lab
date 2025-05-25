import matplotlib.pyplot as plt

def dda_slope_increment(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        print("Start and end points are the same.")
        return

    # Calculate slope m
    if dx != 0:
        m = dy / dx
    else:
        m = None  # vertical line, slope undefined

    x_points = []
    y_points = []

    print("\nDDA Line Drawing Using slope m and increments:")
    print("Step\tX\tY\tPlotted Pixel")

    x, y = x1, y1
    x_points.append(x)
    y_points.append(y)

    # Decide which axis to increment by 1 based on which difference is greater
    if m is None:
        # Vertical line special case
        steps = abs(int(dy))
        y_inc = 1 if dy > 0 else -1
        for i in range(1, steps + 1):
            y += y_inc
            x_points.append(x)
            y_points.append(y)
            print(f"{i}\t{round(x, 2)}\t{round(y, 2)}\t({round(x)}, {round(y)})")
    else:
        if abs(dx) >= abs(dy):
            # Case 1: x is dominant, increment x by 1 each step, y by m
            steps = abs(int(dx))
            x_inc = 1 if dx > 0 else -1
            for i in range(1, steps + 1):
                x += x_inc
                y += m * x_inc
                x_points.append(x)
                y_points.append(y)
                print(f"{i}\t{round(x, 2)}\t{round(y, 2)}\t({round(x)}, {round(y)})")
        else:
            # Case 2: y is dominant, increment y by 1 each step, x by 1/m
            steps = abs(int(dy))
            y_inc = 1 if dy > 0 else -1
            for i in range(1, steps + 1):
                y += y_inc
                x += (1 / m) * y_inc
                x_points.append(x)
                y_points.append(y)
                print(f"{i}\t{round(x, 2)}\t{round(y, 2)}\t({round(x)}, {round(y)})")

    # Round points for pixels
    rounded_x = [round(px) for px in x_points]
    rounded_y = [round(py) for py in y_points]

    # Plotting only DDA pixels
    plt.plot(rounded_x, rounded_y, color='blue', marker='s', linestyle='None', markersize=8, label='DDA Pixels')

    plt.grid(True)
    plt.title("DDA Line Drawing Using Slope and Increments")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.xticks(range(int(min(rounded_x)) - 1, int(max(rounded_x)) + 2))
    plt.yticks(range(int(min(rounded_y)) - 1, int(max(rounded_y)) + 2))
    plt.xlim(min(0, min(rounded_x) - 1), max(rounded_x) + 1)
    plt.ylim(min(0, min(rounded_y) - 1), max(rounded_y) + 1)

    plt.legend()
    plt.axis("equal")
    plt.show()

# Take input and run
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    dda_slope_increment(x1, y1, x2, y2)

except ValueError:
    print("Invalid input! Please enter numeric values.")
