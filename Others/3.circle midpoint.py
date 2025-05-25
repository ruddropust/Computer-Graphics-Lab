import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, x_points, y_points, plot_steps, full_table, p):
    # Representative point for the table
    rep_point = (xc + x, yc + y)
    full_table.append((len(full_table), p, x, y, rep_point))

    # 8-way symmetry points
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        if (px, py) not in zip(x_points, y_points):
            x_points.append(px)
            y_points.append(py)

    plot_steps.append(f"({xc}+{x},{yc}+{y}) = ({rep_point[0]},{rep_point[1]})")

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    x_points = []
    y_points = []
    plot_steps = []
    full_table = []

    # Step 0
    plot_circle_points(xc, yc, x, y, x_points, y_points, plot_steps, full_table, p)

    # Loop
    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1

        plot_circle_points(xc, yc, x, y, x_points, y_points, plot_steps, full_table, p)

    # Print full step-by-step table
    print("\nFull Calculation Table:")
    print(f"{'Step':<5}{'p':<10}{'x':<8}{'y':<8}(x_plot, y_plot)")
    print("-" * 45)
    for step, p_val, x_val, y_val, pt in full_table:
        print(f"{step:<5}{p_val:<10}{x_val:<8}{y_val:<8}{pt}")

    # Final points for plotting
    print("\nX plot values:", x_points)
    print("Y plot values:", y_points)

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.plot(x_points, y_points, 'bo', label='Circle Pixels')
    plt.plot(xc, yc, 'ro', label='Center')  # Mark center
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.title("Midpoint Circle Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

# User input
try:
    xc = int(input("Enter center x (xc): "))  # e.g., 5
    yc = int(input("Enter center y (yc): "))  # e.g., 7
    r = int(input("Enter radius r: "))        # e.g., 6

    midpoint_circle(xc, yc, r)

except ValueError:
    print("Invalid input! Please enter integer values.")
