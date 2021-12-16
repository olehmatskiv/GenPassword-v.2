from tkinter import *
import random

Window = Tk()
Window.title('Generator Password v.2 by OlehDev')

Window.geometry("700x500")
Window.resizable(width=False , height=False)


def new_rand():
    pw_entry.delete(0, END)

    pw_length = int(my_entry.get())

    chars = list(
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(chars)
    my_password = ''.join([random.choice(chars) for x in range(pw_length)])
    
    pw_entry.insert(0, my_password)


def clipper():
    Window.clipboard_clear()
    Window.clipboard_append(pw_entry.get())


def responser():
    with open("Your Password.txt", "w", encoding="utf-8") as file:
        file.write(str(pw_entry.get()))


lf = LabelFrame(Window, text="Задайте довжину паролю")
lf.pack(pady=20)


my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)


pw_entry = Entry(Window, text="", font=(
    "Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)


my_frame = Frame(Window)
my_frame.pack(pady=20)


my_button = Button(my_frame, text="Генерація паролю", command=new_rand)
my_button.grid(row=0, column=0, padx=10)


clip_button = Button(
    my_frame, text="Скопіюйте до буферу обміну", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

response_button = Button(my_frame, text="Записати в файл", command=responser)
response_button.grid(row=0, column=2, padx=10)


Window.mainloop()
