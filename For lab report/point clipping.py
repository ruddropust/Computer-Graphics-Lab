import matplotlib.pyplot as plt

def point_clipping(points, xmin, ymin, xmax, ymax):
    inside_points = []
    for x, y in points:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            inside_points.append((x, y))
    return inside_points

# Input section
n = int(input("Enter number of points: "))
points = []
for i in range(n):
    x, y = map(float, input(f"Point {i+1} (x y): ").split())
    points.append((x, y))

# Define clipping window
xmin, ymin, xmax, ymax = map(float, input(f"Enter window (xmin, ymin, xmax, ymax): ").split())

# Perform clipping
accepted_points = point_clipping(points, xmin, ymin, xmax, ymax)

# Plotting
fig, ax = plt.subplots()
# Plot clipping window
rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, edgecolor='red', facecolor='none', linewidth=2)
ax.add_patch(rect)

print(f"Accepted Points: {accepted_points}")
# Plot accepted points
if accepted_points:
    x_vals, y_vals = zip(*accepted_points)
    plt.scatter(x_vals, y_vals, color='blue', label='Accepted Points')

# All points as reference
x_all, y_all = zip(*points)
plt.scatter(x_all, y_all, color='black', marker='x', label='All Input Points')

# Labels and legend
plt.title('Point Clipping')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
