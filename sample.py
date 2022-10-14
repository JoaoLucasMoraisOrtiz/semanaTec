import tkinter as tk # Use `import Tkinter as tk` for Python 2

root = tk.Tk()
root.geometry("150x50+680+350")

def function():
    global button_start
    root.attributes("-fullscreen", True)
    label = tk.Label(root, text="Loaded!", height=6, width=8)
    label.pack()
    button_start.place_forget() # You can also use `button_start.destroy()`



button_start = tk.Button(root, text="Start", height=3, width=20, command=function)
button_start.place(x = 0, y = 10)
button_exit = tk.Button(root, text="Exit", command=root.destroy)
button_exit.place(x=1506, y=0)

root.mainloop()