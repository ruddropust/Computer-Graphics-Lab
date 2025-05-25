import matplotlib.pyplot as plt
def scale_object(points, sx, sy, pivot=(0, 0)):
    h, k = pivot
    scaled_points = []

    for x, y in points:
        x_scaled = h + (x - h) * sx
        y_scaled = k + (y - k) * sy
        scaled_points.append((round(x_scaled, 2), round(y_scaled, 2)))
    return scaled_points

n = int(input("Enter number of vertices (should be 3 for a triangle): "))
original_points = []
for i in range(0,n):
    x, y = map(float, input(f"Enter coordinates for point {i+1} (x y): ").split())
    original_points.append((x, y))

sx = float(input("Enter scaling factor in x-direction (sx): "))
sy = float(input("Enter scaling factor in y-direction (sy): "))

pivot_x, pivot_y = map(float, input("Enter pivot point (x y): ").split())
pivot_point = (pivot_x, pivot_y)

scaled_points = scale_object(original_points, sx, sy, pivot_point)

print("\nOriginal Points:", original_points)
print("Scaled Points:", scaled_points)

original_points.append(original_points[0])
scaled_points.append(scaled_points[0])

ox, oy = zip(*original_points)
sx_, sy_ = zip(*scaled_points)

plt.figure(figsize=(6, 6))
plt.plot(ox, oy, 'bo-', label='Original Triangle')
plt.plot(sx_, sy_, 'ro--', label='Scaled Triangle')
plt.scatter(*pivot_point, color='green', label='Pivot Point')
plt.title(f"Scaling of Triangle about {pivot_point}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
