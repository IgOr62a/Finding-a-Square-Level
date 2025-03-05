from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def show_help():
    messagebox.showinfo("Help", "Введите коэффициенты a, b, c и нажмите соответствующую кнопку для расчета.")

def show_about():
    messagebox.showinfo("About Us", "Программа для решения квадратных уравнений. Разработано на Python с Tkinter.")

def discriminant_viet(calc_type):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = (b**2) - (4*a*c)

        if calc_type == "discriminant":
            if d < 0:
                discr_label.config(text=f'Дискриминант: D = {d:.2f}\nКорней нет', foreground="red")
            elif d == 0:
                x = -b / (2 * a)
                discr_label.config(text=f'Дискриминант: D = {d:.2f}\nОдин корень: x = {x:.2f}', foreground="black")
            else:
                x1 = (-b + (d**0.5)) / (2 * a)
                x2 = (-b - (d**0.5)) / (2 * a)
                discr_label.config(text=f'Дискриминант: D = {d:.2f}\nКорни: x₁ = {x1:.2f}, x₂ = {x2:.2f}', foreground="black")
            plot_graph(a, b, c, d)
        elif calc_type == "vieta":
            if d >= 0:
                x1 = (-b + (d**0.5)) / (2 * a)
                x2 = (-b - (d**0.5)) / (2 * a)
                vieta_label.config(text=f'Виета: сумма = {x1 + x2:.2f}, произведение = {x1 * x2:.2f}', foreground="black")
            else:
                vieta_label.config(text='Виета неприменима', foreground="black")
    except ValueError:
        discr_label.config(text="Ошибка: введите числа!", foreground="red")
        vieta_label.config(text="", foreground="black")

def plot_graph(a, b, c, d):
    ax.clear()
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    ax.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, linestyle='--', linewidth=0.5)
    if d >= 0:
        x1 = (-b + (d**0.5)) / (2 * a)
        x2 = (-b - (d**0.5)) / (2 * a)
        ax.scatter([x1, x2], [0, 0], color='red', zorder=3, label='Корни')
    ax.legend()
    canvas.draw()

root = tk.Tk()
root.title("Решение квадратных уравнений")
root.geometry('1000x800')
root.resizable(False, False)
root.configure(bg="#E8EAF6")

top_frame = ttk.Frame(root)
top_frame.place(x=10, y=10, anchor="nw")  

btn_help = ttk.Button(top_frame, text='Help', command=show_help)
btn_help.pack(side="left", padx=5)

separator = ttk.Separator(top_frame, orient="vertical")
separator.pack(side="left", fill="y", padx=5)

btn_about = ttk.Button(top_frame, text='About Us', command=show_about)
btn_about.pack(side="left", padx=5)

frame = ttk.Frame(root, padding=10)
frame.place(x=20, y=60, anchor="nw")  

ttk.Label(frame, text="a =", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=3)
entry_a = ttk.Entry(frame, width=7)
entry_a.grid(row=0, column=1, padx=5, pady=3)

ttk.Separator(frame, orient="horizontal").grid(row=1, columnspan=2, sticky="ew", pady=5)

ttk.Label(frame, text="b =", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=3)
entry_b = ttk.Entry(frame, width=7)
entry_b.grid(row=2, column=1, padx=5, pady=3)

ttk.Separator(frame, orient="horizontal").grid(row=3, columnspan=2, sticky="ew", pady=5)

ttk.Label(frame, text="c =", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=3)
entry_c = ttk.Entry(frame, width=7)
entry_c.grid(row=4, column=1, padx=5, pady=3)

btn_discr = ttk.Button(root, text='Рассчитать дискриминант и корни', command=lambda: discriminant_viet("discriminant"), style="Big.TButton")
btn_discr.place(x=10, y=300, anchor="nw")

separator2 = ttk.Separator(root, orient="horizontal")
separator2.place(x=20, y=280, width=350)

btn_vieta = ttk.Button(root, text='Рассчитать по Виете', command=lambda: discriminant_viet("vieta"), style="Big.TButton")
btn_vieta.place(x=10, y=350, anchor="nw")

style = ttk.Style()
style.configure("Big.TButton", font=("Arial", 12, "bold"), padding=10, background="#B3E5FC", foreground="black")

discr_label = ttk.Label(root, text="", font=("Arial", 12, "bold"), foreground="green")
discr_label.place(x=20, y=200, anchor="nw") 

vieta_label = ttk.Label(root, text="", font=("Arial", 12, "bold"), foreground="black")
vieta_label.place(x=20, y=240, anchor="nw")

fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=480, y=40, anchor="nw")

formula_label = ttk.Label(root, text="Формулы:\nДискриминанта:D = b² - 4ac", font=("Arial", 12), justify="left")
formula_label.place(x=200, y=150, anchor="sw")
formula_label2 = ttk.Label(root, text="Виета: x₁ + x₂ = -b/a, x₁ * x₂ = c/a", font=("Arial", 12), justify="left")
formula_label2.place(x=200, y=170, anchor="sw")

root.mainloop()
