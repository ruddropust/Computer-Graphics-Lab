import matplotlib.pyplot as plt

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)
    
    print(f"Code1: {code1:04b}, Code2: {code2:04b}")  # Show binary region codes

    if code1 == 0 and code2 == 0:
        print(" Case 1: Line is completely inside. No clipping needed.")
        return True, x1, y1, x2, y2
    elif (code1 & code2) != 0:
        print("Case 2: Line is completely outside. It will be rejected.")
        return False, x1, y1, x2, y2
    else:
        print("Case 3: Line is partially inside. Clipping will be performed.")
        accept = False
        while True:
            if code1 == 0 and code2 == 0:
                accept = True
                break
            elif (code1 & code2) != 0:
                break
            else:
                x = y = 0.0
                code_out = code1 if code1 != 0 else code2

                if code_out & TOP:
                    x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                    y = ymax
                elif code_out & BOTTOM:
                    x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                    y = ymin
                elif code_out & RIGHT:
                    y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                    x = xmax
                elif code_out & LEFT:
                    y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                    x = xmin

                if code_out == code1:
                    x1, y1 = x, y
                    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
                else:
                    x2, y2 = x, y
                    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

        return accept, x1, y1, x2, y2

# ==== USER INPUT SECTION ====
print("Enter the clipping window boundaries:")
xmin = float(input("xmin: "))
xmax = float(input("xmax: "))
ymin = float(input("ymin: "))
ymax = float(input("ymax: "))

print("\nEnter coordinates for the line segment to clip:")
x1, y1 = map(float, input("Start point P1 (x y): ").split())
x2, y2 = map(float, input("End point P2 (x y): ").split())

# Apply Cohen-Sutherland
accepted, cx1, cy1, cx2, cy2 = cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

# Plotting
plt.figure()

# Clipping window (rectangle)
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'k', label="Clipping Window")

# Original line
plt.plot([x1, x2], [y1, y2], 'r--', label="Original Line")

# Clipped line
if accepted:
    if (cx1, cy1) == (x1, y1) and (cx2, cy2) == (x2, y2):
        plt.plot([x1, x2], [y1, y2], 'g-', linewidth=2, label="Line (Completely Inside)")
    else:
        plt.plot([cx1, cx2], [cy1, cy2], 'g-', linewidth=2, label="Clipped Line")
    print(f"\nFinal Accepted Segment: ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})")
else:
    print("\nLine fully outside: Nothing to draw.")

plt.title("Cohen-Sutherland Line Clipping - Simplified Window Input")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
