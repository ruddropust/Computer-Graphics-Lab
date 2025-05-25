import matplotlib.pyplot as plt

# === USER INPUT for Clipping Window ===
try:
    print("Enter the clipping window boundaries:")
    xmin = float(input("xmin: "))
    xmax = float(input("xmax: "))
    ymin = float(input("ymin: "))
    ymax = float(input("ymax: "))
except ValueError:
    print("Invalid input for window. Please enter numbers.")
    exit()

# === USER INPUT for Point ===
try:
    print("\nEnter coordinates of the point:")
    x, y = map(float, input("Point (x y): ").split())
except ValueError:
    print("Invalid input for point. Please enter two numbers.")
    exit()

# === POINT CLIPPING LOGIC ===
def is_point_inside(x, y, xmin, xmax, ymin, ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

inside = is_point_inside(x, y, xmin, xmax, ymin, ymax)

# === PLOTTING ===
fig, ax = plt.subplots()

# Draw clipping window
window = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                       edgecolor='blue', facecolor='none', linewidth=2, label='Clipping Window')
ax.add_patch(window)

# Draw the point
if inside:
    ax.plot(x, y, 'go', markersize=10, label='Point Inside')
    print(f"\n The point ({x:.2f}, {y:.2f}) is INSIDE the clipping window.")
else:
    ax.plot(x, y, 'ro', markersize=10, label='Point Outside')
    print(f"\n The point ({x:.2f}, {y:.2f}) is OUTSIDE the clipping window.")

# Axis settings
ax.set_xlim(min(x, xmin) - 10, max(x, xmax) + 10)
ax.set_ylim(min(y, ymin) - 10, max(y, ymax) + 10)
ax.set_title("Point Clipping with User Input")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.grid(True)
ax.legend()
ax.set_aspect('equal', adjustable='box')
plt.show()
