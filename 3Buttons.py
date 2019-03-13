import tkinter as tk

root = tk.Tk()
b = tk.Button(root, text="Click me")

def close_window(event):
	root.destroy()

b.bind('<Button-1>', close_window)

b.pack(side = 'right')
root.mainloop()
