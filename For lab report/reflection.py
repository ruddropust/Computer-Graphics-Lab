import matplotlib.pyplot as plt

def reflect_object(points, axis='x'):
    reflected_points = []
    for x, y in points:
        if axis == 'x':
            reflected_points.append((x, -y))
        elif axis == 'y':
            reflected_points.append((-x, y))
        elif axis == 'origin':
            reflected_points.append((-x, -y))
        elif axis == 'y=x':
            reflected_points.append((y, x))
        else:
            raise ValueError("Invalid reflection axis. Choose from 'x', 'y', 'origin', 'y=x'.")
    return reflected_points

# Input: Triangle coordinates
n = int(input("Enter number of vertices (should be 3 for a triangle): "))
original_points = []
for i in range(0,n):
    x, y = map(float, input(f"Enter coordinates for point {i+1} (x y): ").split())
    original_points.append((x, y))

# Input: Reflection axis
print("\nChoose axis of reflection (x, y, origin, y=x):")
axis = input("Enter axis: ").strip().lower()

# Reflect the triangle
reflected_points = reflect_object(original_points, axis)

# Output
print("\nOriginal Points:", original_points)
print("Reflected Points:", reflected_points)

# Plotting
# Close the triangle for plotting
original_points.append(original_points[0])
reflected_points.append(reflected_points[0])

ox, oy = zip(*original_points)
rx, ry = zip(*reflected_points)

plt.figure(figsize=(6, 6))
plt.plot(ox, oy, 'bo-', label='Original Triangle')
plt.plot(rx, ry, 'ro--', label='Reflected Triangle')
plt.title(f"Reflection across {axis}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
