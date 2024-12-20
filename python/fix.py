import tkinter as tk
import math

class Star:
    def __init__(self, canvas, x, y, outer_radius, inner_radius, points):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.points = points
        self.draw()

    def draw(self):
        angle = 360 / (self.points * 2)  # Angle between each point

        # Coordinates list for creating the star
        coords = []
        for i in range(self.points * 2):
            radius = self.outer_radius if i % 2 == 0 else self.inner_radius
            x = self.x + radius * math.cos(math.radians(90 + i * angle))
            y = self.y - radius * math.sin(math.radians(90 + i * angle))
            coords.extend((x, y))

        # Draw the star
        self.canvas.create_polygon(coords, fill='blue', outline='blue')

# Create the main window
root = tk.Tk()
root.title("Star Vector")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()


star = Star(canvas, 200, 200, 100, 70, 8)  # Outer radius, Inner radius, Number of points



# Run the Tkinter event loop
root.mainloop()
