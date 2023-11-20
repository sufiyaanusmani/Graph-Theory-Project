import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

app = tk.Tk()
app.title("Graph Theory Project")

label = tk.Label(app, text="Hello, Tkinter!")

button = tk.Button(app, text="Click me!", command=on_button_click)

label.grid(row=0, column=0, padx=10, pady=10)
button.grid(row=1, column=0, padx=10, pady=10)

app.mainloop()
