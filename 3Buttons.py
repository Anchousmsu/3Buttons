import tkinter as tk

root = tk.Tk()
root.geometry("280x200+300+300")
e1 = tk.Entry(width=30)
l1 = tk.Label(bg='black', fg='white',width=20)
b1 = tk.Button(root, text="Click me", fg="green")
b2 = tk.Button(root, text="Click me too", fg="blue")
b3 = tk.Button(root, text="Don't click me", bg="yellow", fg="red")

def close_window(event):
	root.destroy()

def str_write(event):
    s = e1.get()
    l1['text'] = s

def str_sort(event):
    s = e1.get()
    s = s.split()
    s.sort()
    l1['text'] = ' '.join(s)

b3.bind('<Button-1>', close_window)
b2.bind('<Button-1>', str_sort)
b1.bind('<Button-1>', str_write)

b1.pack(side = 'left')
b2.pack(side = 'top')
b3.pack(side = 'right')
l1.pack(side = 'bottom')
e1.pack(side = 'bottom')
root.mainloop()
