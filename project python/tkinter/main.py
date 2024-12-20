import tkinter as tk


root = tk.Tk()
label = tk.Label(text=1, fg='red', bg="skyblue", width=100, height=20)
label.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button(text="Click Me", command=label.configure(text=x+1))


button.pack()
root.mainloop()


