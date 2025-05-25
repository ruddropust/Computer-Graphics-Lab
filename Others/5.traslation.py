import matplotlib.pyplot as plt

def translate_shape(points, tx, ty):
    translated_points = []
    for x, y in points:
        translated_points.append((x + tx, y + ty))
    return translated_points

def plot_shapes(original, translated):
    # Close the shape for plotting
    original.append(original[0])
    translated.append(translated[0])

    x_orig, y_orig = zip(*original)
    x_trans, y_trans = zip(*translated)

    plt.figure(figsize=(6, 6))
    plt.plot(x_orig, y_orig, 'b-o', label='Original Shape')
    plt.plot(x_trans, y_trans, 'r--o', label='Translated Shape')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.title('2D Translation')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

# -------- USER INPUT --------
try:
    n = int(input("Enter number of vertices in the shape: "))
    shape_points = []

    for i in range(n):
        x = float(input(f"Enter x{i+1}: "))
        y = float(input(f"Enter y{i+1}: "))
        shape_points.append((x, y))

    tx = float(input("Enter translation along X (tx): "))
    ty = float(input("Enter translation along Y (ty): "))

    translated_points = translate_shape(shape_points, tx, ty)
    plot_shapes(shape_points.copy(), translated_points)

except ValueError:
    print("Invalid input! Please enter numeric values.")
