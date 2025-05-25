import matplotlib.pyplot as plt

def shear_object(points, shx=0, shy=0):
    sheared_points = []
    for x, y in points:
        x_sheared = x + shx * y
        y_sheared = y + shy * x
        sheared_points.append((round(x_sheared, 2), round(y_sheared, 2)))
    return sheared_points
n = int(input("Enter number of vertices: "))
original_points = []
print("Enter coordinates:")
for i in range(n):
    x, y = map(float, input(f"Point {i+1} (x y): ").split())
    original_points.append((x, y))
shx = float(input("Enter shear factor in X-direction (shx): "))
shy = float(input("Enter shear factor in Y-direction (shy): "))
sheared_points = shear_object(original_points, shx, shy)
print("\nOriginal Points:", original_points)
print("Sheared Points:", sheared_points)
original_points.append(original_points[0])
sheared_points.append(sheared_points[0])

ox, oy = zip(*original_points)
sx, sy = zip(*sheared_points)

plt.figure(figsize=(6, 6))
plt.plot(ox, oy, 'bo-', label='Original Shape')
plt.plot(sx, sy, 'ro--', label='Sheared Shape')
plt.title("Shearing Transformation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
