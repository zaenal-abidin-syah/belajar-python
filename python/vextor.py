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
        coords1 = []
        coords2 = []
        for i in range(self.points * 2):
            radius = self.outer_radius if i % 2 == 0 else self.inner_radius
            x = self.x + radius * math.cos(math.radians(90 + i * angle))
            y = self.y - radius * math.sin(math.radians(90 + i * angle))
            x1 = self.x + (radius - 30) * math.cos(math.radians(90 + i * angle))
            y1= self.y - (radius - 30) * math.sin(math.radians(90 + i * angle))
            x2 = self.x + (radius - 60) * math.cos(math.radians(90 + i * angle))
            y2 = self.y - (radius - 60) * math.sin(math.radians(90 + i * angle))
            coords.extend((x, y))
            coords1.extend((x1, y1))
            coords2.extend((x2, y2))

        # Draw the star
        print(coords)
        self.canvas.create_polygon(coords, fill='blue', outline='blue')
        self.canvas.create_polygon(coords1, fill='white', outline='white')
        self.canvas.create_polygon(coords2, fill='green', outline='green')

# Create the main window
root = tk.Tk()
root.title("Star Vector")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()


star = Star(canvas, 200, 200, 150, 100, 8) 



# Run the Tkinter event loop
root.mainloop()
