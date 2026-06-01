import tkinter as tk
from tkinter import messagebox

def BMI_Calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        height_m = height/100
        if height <= 0 or weight <= 0:
            messagebox.showwarning("Warning","Please input valid information.")
        bmi = weight / (height_m**2)
        if bmi < 18.5 :
            category = "Underweight"
        elif bmi < 25.0 :
            category = "Normal Weight"
        elif bmi < 30.0 :
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text = f"{bmi:.2f} BMI - {category}"
        )
    except ValueError:
        messagebox.showwarning("Warning","Please input valid information.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("600x350")

BMI_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Optima", 20, "bold"),
    fg="Black",
    bg="Cyan"
)
BMI_label.pack(pady=15)

#Weight
weight_frame = tk.Frame(root)
BMI_weight = tk.Label(
    weight_frame,
    text="Weight in kg : ",
    font = ("Arial",19),
)
weight_entry = tk.Entry(
    weight_frame,
   font=("Arial",19)
)
BMI_weight.pack(side="left",padx=5)
weight_entry.pack(side="left")
weight_frame.pack(pady=10)


#Height
height_frame = tk.Frame(root)
BMI_height = tk.Label(
    height_frame,
    text="Height in cm :  ",
    font = ("Arial",19)
)
height_entry = tk.Entry(
    height_frame,
   font=("Arial",19)
)
BMI_height.pack(side="left",padx=5)
height_entry.pack(side="left")
height_frame.pack(pady=10)

calculate_button = tk.Button(
    root,
    text="Calculate",
    fg="Black",
    bg = "Cyan",
    font=("Optima",19,"bold"),
    command= BMI_Calculate
)
calculate_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Optima",19,"bold")
)
result_label.pack()

root.mainloop()