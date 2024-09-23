import tkinter as tk
from math import pi

class AreaCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Area Calculator")

        self.shape_label = tk.Label(master, text="Choose a Shape:")
        self.shape_label.grid(row=0, column=0, sticky=tk.W)

        self.shape_var = tk.StringVar()
        self.shape_var.set("Circle")

        self.shape_option = tk.OptionMenu(master, self.shape_var, "Circle", "Cube", "Cylinder", "Sphere", command=self.show_hide_entries)
        self.shape_option.grid(row=0, column=1, sticky=tk.W)

        self.radius_label = tk.Label(master, text="Radius:")
        self.radius_label.grid(row=1, column=0, sticky=tk.W)
        self.radius_entry = tk.Entry(master)
        self.radius_entry.grid(row=1, column=1)

        self.height_label = tk.Label(master, text="Height:")
        self.height_label.grid(row=2, column=0, sticky=tk.W)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=2, column=1)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, columnspan=2)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, columnspan=2)
        self.height_entry.grid_forget()
        self.height_label.grid_forget()

        
    def show_hide_entries(self, shape):
        self.height_entry.grid_forget()
        self.height_label.grid_forget()
        self.radius_entry.grid_forget()
        self.radius_label.grid_forget()
        
        if shape == "Circle" or shape == "Sphere":
            self.radius_label.grid(row=1, column=0, sticky=tk.W)
            self.radius_entry.grid(row=1, column=1)
        elif shape == "Cube":
            self.height_label.grid(row=2, column=0, sticky=tk.W)
            self.height_entry.grid(row=2, column=1)
        elif shape == "Cylinder":
            self.radius_label.grid(row=1, column=0, sticky=tk.W)
            self.radius_entry.grid(row=1, column=1)
            self.height_label.grid(row=2, column=0, sticky=tk.W)
            self.height_entry.grid(row=2, column=1)
    def calculate(self):
        shape = self.shape_var.get()
        if shape == "Circle":
            radius = float(self.radius_entry.get())
            area = pi * radius ** 2
        elif shape == "Cube":
            side = float(self.height_entry.get())
            area = 6 * side ** 2
        elif shape == "Cylinder":
            radius = float(self.radius_entry.get())
            height = float(self.height_entry.get())
            area = 2 * pi * radius * height + 2 * pi * radius ** 2
        elif shape == "Sphere":
            radius = float(self.radius_entry.get())
            area = 4 * pi * radius ** 2
        else:
            area = 0

        self.result_label.config(text=f"Area of {shape}: {area:.2f}")

root = tk.Tk()
app = AreaCalculator(root)
root.mainloop()
