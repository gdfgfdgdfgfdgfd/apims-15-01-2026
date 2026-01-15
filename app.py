import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Меню Tkinter")
root.geometry("400x300")

devices = ["Камера", "Микроконтроллер", "Датчик движения", "Термометр", "Андрей Зеленин"]

specs = {
    "Камера": ["Разрешение: 4K", "Угол: 120°", "Ночное видение"],
    "Микроконтроллер": ["ARM Cortex-M4", "512 КБ Flash", "Интерфейсы: UART"],
    "Датчик движения": ["PIR с линзой", "Дальность: 10м", "Угол: 110°"],
    "Термометр": ["Диапазон: -40°C…+125°C", "Точность: ±0.5°C", "I2C / SPI"],
    "Андрей Зеленин": ["Специальность: Программист", "Опыт: 5 лет", "Курсы: Python, Tkinter"]
}

icons = {
    "Камера": "📷",
    "Микроконтроллер": "🖥️",
    "Датчик движения": "⚡",
    "Термометр": "🌡️",
    "Андрей Зеленин": "👤"
}

def show_image(device):
    window = tk.Toplevel(root)
    window.title(f"Изображение: {device}")
    window.geometry("400x350")
    tk.Label(window, text=device, font=("Arial", 14, "bold")).pack(pady=10)

    image_label = tk.Label(window)
    image_label.pack()

    image_folder = "images"
    image_file = os.path.join(image_folder, f"{device.lower().replace(' ', '_')}.jpg")

    if os.path.isfile(image_file):
        img = Image.open(image_file)
        img = img.resize((250, 200))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        tk.Label(window, text=f"Файл: {os.path.basename(image_file)}").pack(pady=5)
    else:
        tk.Label(window, text="Изображение не найдено", fg="red").pack(pady=10)
        tk.Label(window, text=icons.get(device, "📸"), font=("Arial", 48)).pack(pady=10)

    tk.Button(window, text="Закрыть", command=window.destroy).pack(pady=10)

def show_specs(device):
    text = f"{device}:\n\n" + "\n".join(f"• {s}" for s in specs[device])
    messagebox.showinfo("Характеристики", text)

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Выход", command=root.quit)

image_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Изображение", menu=image_menu)
for d in devices:
    image_menu.add_command(label=d, command=lambdagit --version
    dev=d: show_image(dev))

specs_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Характеристики", menu=specs_menu)
for d in devices:
    specs_menu.add_command(label=d, command=lambda dev=d: show_specs(dev))

func_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Функции", menu=func_menu)
for func in ["Автоматизация", "Анализ данных", "Отчёты"]:
    func_menu.add_command(label=func)

tk.Label(root, text="Меню Tkinter", font=("Arial", 14, "bold")).pack(pady=50)
tk.Label(root, text="Выберите пункт меню", font=("Arial", 11)).pack()

root.mainloop()
