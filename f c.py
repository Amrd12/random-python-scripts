import tkinter as tk

def f_to_c():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    label_result.config(text=f"{fahrenheit}°F is {celsius:.2f}°C")

def c_to_f():
    celsius = float(entry.get())
    fahrenheit = celsius * 9/5 + 32
    label_result.config(text=f"{celsius}°C is {fahrenheit:.2f}°F")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Create entry widget
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=0, padx=5, pady=5)

# Create buttons
button_f_to_c = tk.Button(root, text="Convert F to C", command=f_to_c)
button_f_to_c.grid(row=0, column=1, padx=5, pady=5)

button_c_to_f = tk.Button(root, text="Convert C to F", command=c_to_f)
button_c_to_f.grid(row=0, column=2, padx=5, pady=5)

# Create result label
label_result = tk.Label(root, text="")
label_result.grid(row=1, columnspan=3, padx=5, pady=5)

root.mainloop()
