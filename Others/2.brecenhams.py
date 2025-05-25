import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx <= 0 or dy < 0 or dy > dx:
        print("This code supports only lines with 0 <= slope <= 1 and x2 > x1.")
        return

    x = x1
    y = y1

    p = 2 * dy - dx  # Decision parameter

    x_points = [x]
    y_points = [y]

    print("Step\tX\tY\tDecision Param (p)")
    print(f"0\t{x}\t{y}\t{p}")

    for i in range(1, dx + 1):
        if p < 0:
            x += 1
            # y unchanged
            p += 2 * dy
        else:
            x += 1
            y += 1
            p += 2 * (dy - dx)

        x_points.append(x)
        y_points.append(y)
        print(f"{i}\t{x}\t{y}\t{p}")

    # Plot points
    plt.plot(x_points, y_points, 'b-s', label='Bresenham Pixels')
    plt.title("Bresenham Line Drawing (0 <= slope <= 1)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

try:
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    bresenham_line(x1, y1, x2, y2)

except ValueError:
    print("Please enter valid integer values.")

