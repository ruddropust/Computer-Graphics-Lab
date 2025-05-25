import matplotlib.pyplot as plt

def translate_object(points, tx, ty):
    translated_points = []
    for x, y in points:
        new_x = x + tx
        new_y = y + ty
        translated_points.append((new_x, new_y))
    return translated_points

# Get user input
print('Input:')
n = int(input("Enter number of points: "))
original_points = []
for i in range(n):
    x, y = map(int, input(f"Enter coordinates for point {i+1} (x y): ").split())
    original_points.append((x, y))

tx = int(input("Enter translation in x (tx): "))
ty = int(input("Enter translation in y (ty): "))

# Perform translation
translated_points = translate_object(original_points, tx, ty)

# Close the shape for proper plotting
print('Output:\n')
original_points.append(original_points[0])
translated_points.append(translated_points[0])
# Output
print("Original Points:", original_points)
print("Translated Points:", translated_points)

# Extract x and y for plotting
ox, oy = zip(*original_points)
tx, ty = zip(*translated_points)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(ox, oy, 'bo-', label='Original Shape')
plt.plot(tx, ty, 'ro--', label='Translated Shape')
plt.title("2D Object Translation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
