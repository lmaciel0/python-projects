import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

# Function to perform temperature conversion
def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        unit_from = var_unit_from.get()
        unit_to = var_unit_to.get()

        if unit_from == unit_to:
            result_message = "Result: Units are the same."
        else:
            if unit_from == "Celsius":
                if unit_to == "Fahrenheit":
                    result = celsius_to_fahrenheit(temperature)
                elif unit_to == "Kelvin":
                    result = celsius_to_kelvin(temperature)
            elif unit_from == "Fahrenheit":
                if unit_to == "Celsius":
                    result = fahrenheit_to_celsius(temperature)
                elif unit_to == "Kelvin":
                    result = fahrenheit_to_kelvin(temperature)
            elif unit_from == "Kelvin":
                if unit_to == "Celsius":
                    result = kelvin_to_celsius(temperature)
                elif unit_to == "Fahrenheit":
                    result = kelvin_to_fahrenheit(temperature)

            result_message = f"Result: {temperature:.2f} {unit_from} is equal to {result:.2f} {unit_to}"
            show_result(result_message)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid numeric value for the temperature.")

def show_result(result_message):
    messagebox.showinfo("Conversion Result", result_message)

def clear_fields():
    entry_temperature.delete(0, tk.END)
    result_label.config(text="Result:")

# Window configuration
window = tk.Tk()
window.title("Temperature Converter")

# Get the width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Define the window width and height
window_width = 500
window_height = 500

# Calculate the x and y coordinates to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window's position at the center of the screen
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set the font to "Lexend"
font_style = ("Lexend", 12)

# Temperature input
label_temperature = tk.Label(window, text="Enter temperature:", font=font_style)
label_temperature.pack()

# Apply the custom style to the entry field
style = ttk.Style()
style.theme_use("default")
style.configure("Rounded.TEntry", borderwidth=15, relief="ridge", font=font_style)
entry_temperature = ttk.Entry(window, style="Rounded.TEntry")
entry_temperature.pack(pady=5)

# Source unit selection
label_unit_from = tk.Label(window, text="From:", font=font_style)
label_unit_from.pack()

var_unit_from = tk.StringVar()
var_unit_from.set("Celsius")
unit_options = ["Celsius", "Fahrenheit", "Kelvin"]

# Dropdown menus with the same style as "Convert" and "Clear" buttons
menu_unit_from = tk.OptionMenu(window, var_unit_from, *unit_options)
menu_unit_from.config(font=font_style)
menu_unit_from.pack(pady=5)

# Destination unit selection
label_unit_to = tk.Label(window, text="To:", font=font_style)
label_unit_to.pack()

var_unit_to = tk.StringVar()
var_unit_to.set("Fahrenheit")

# Dropdown menus with the same style as "Convert" and "Clear" buttons
menu_unit_to = tk.OptionMenu(window, var_unit_to, *unit_options)
menu_unit_to.config(font=font_style)
menu_unit_to.pack(pady=5)

# Convert button with larger size
convert_button = tk.Button(window, text="Convert", command=convert_temperature, font=font_style)
convert_button.pack(pady=(20, 0))

# Clear button with larger size
clear_button = tk.Button(window, text="Clear", command=clear_fields, font=font_style)
clear_button.pack(pady=(10, 20))

# Result display
result_label = tk.Label(window, text="Result:", font=font_style)
result_label.pack()

# Start GUI event loop
window.mainloop()