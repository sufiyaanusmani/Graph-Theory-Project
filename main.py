import tkinter as tk

class Point:

def clear_content():
    label.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()

def simpleGraph():
    label.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()

    label1 = tk.Label(app, text="Simple Graph")
    label1.grid(row=0, column=0, padx=10, pady=10)
    canvas = tk.Canvas(app, width=500, height=500, bg="lightgray")
    canvas.bind("<Button-1>", on_canvas_click)
    canvas.grid(row=2, column=0, padx=10, pady=10)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(2, weight=1)

def on_button_click():
    label.config(text="Button Clicked!")

def on_canvas_click(event):
    x = event.x
    y = event.y
    print(f"Clicked at coordinates: ({x}, {y})")

app = tk.Tk()
app.geometry("800x600")

app.title("Graph Theory Project")

label = tk.Label(app, text="Main Page")

btn1 = tk.Button(app, text="Draw Simple Graph", command=simpleGraph)
btn2 = tk.Button(app, text="Generate Complete Graph", command=clear_content)
btn3 = tk.Button(app, text="Bipartite and Tripartite Graph", command=clear_content)
btn4 = tk.Button(app, text="Havel Hakimi", command=clear_content)

# canvas = tk.Canvas(app, width=400, height=400, bg="lightgray")
# canvas.bind("<Button-1>", on_canvas_click)

label.grid(row=0, column=0, padx=10, pady=10)
btn1.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
btn2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
btn3.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
btn4.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
# canvas.grid(row=2, column=0, padx=10, pady=10)

# app.columnconfigure(0, weight=1)

# app.rowconfigure(2, weight=1)

app.mainloop()
