import math
import matplotlib.pyplot as plt

def rotate_object(points, angle_degrees, pivot=(0, 0)):
    angle_rad = math.radians(angle_degrees)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    h, k = pivot
    rotated_points = []

    for x, y in points:
        # Translate point back to origin
        x -= h
        y -= k
        # Apply rotation
        x_new = x * cos_theta - y * sin_theta
        y_new = x * sin_theta + y * cos_theta
        # Translate point back
        x_rotated = x_new + h
        y_rotated = y_new + k
        rotated_points.append((round(x_rotated, 2), round(y_rotated, 2)))

    return rotated_points

# Take user input for triangle

n = int(input("Enter number of vertices (should be 3 for a triangle):"))
original_points = []
for i in range(0,n):
    x, y = map(float, input(f"Enter coordinates for point {i+1} (x y): ").split())
    original_points.append((x, y))

# Input rotation angle
angle = float(input("Enter rotation angle (in degrees): "))

# Input pivot point
pivot_x, pivot_y = map(float, input("Enter pivot point (x y): ").split())
pivot_point = (pivot_x, pivot_y)

# Rotate triangle
rotated_points = rotate_object(original_points, angle, pivot_point)

# Output
print("\nOriginal Points:", original_points)
print("Rotated Points:", rotated_points)

# Plotting (optional)
# Close the triangle
original_points.append(original_points[0])
rotated_points.append(rotated_points[0])

ox, oy = zip(*original_points)
rx, ry = zip(*rotated_points)

plt.figure(figsize=(6, 6))
plt.plot(ox, oy, 'bo-', label='Original Triangle')
plt.plot(rx, ry, 'ro--', label='Rotated Triangle')
plt.scatter(*pivot_point, color='green', label='Pivot Point')
plt.title(f"Rotation of Triangle by {angle}° about {pivot_point}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
