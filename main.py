import tkinter as tk
import math

homePageButtonColor = 'blue'
totalPointsSelected = 0
x1, y1, x2, y2 = 0, 0, 0, 0


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = []

def draw_point(event):
    global points
    global selectedValue
    x = event.x
    y = event.y
    if selectedValue == 1:
        points.append(Point(x, y))
        canvas.create_oval(x-4, y-4, x+4, y+4, fill="red")


def on_radio_select():
    global selectedValue
    selectedValue = radio_var.get()

def update_label(value):
    global sliderValue
    canvas.delete("all")
    sliderValue = int(sliderValue) - 1

    radius = 200
    center_x, center_y = 225, 225
    angle_increment = 360 / sliderValue

    vertices = []
    for i in range(sliderValue):
        angle_rad = i * angle_increment
        x = center_x + radius * math.cos(math.radians(angle_rad))
        y = center_y + radius * math.sin(math.radians(angle_rad))
        vertices.append((x, y))
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

    for i in range(sliderValue):
        for j in range(i + 1, sliderValue):
            x1, y1 = vertices[i]
            x2, y2 = vertices[j]
            canvas.create_line(x1, y1, x2, y2, fill="blue")
    sliderValue = value

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
    radio_button1.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    radio_button2.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    canvas.bind("<Button-1>", simpleGraphCanvasClicked)
    canvas.grid(row=3, column=0, padx=10, pady=10)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(2, weight=1)

def drawEdge(event):
    global points
    global selectedValue
    global totalPointsSelected
    global x1
    global y1
    global x2
    global y2

    x = event.x
    y = event.y
    for point in points:
        if(abs(point.x - x) <= 5 and abs(point.y - y) <= 5):
            if totalPointsSelected == 0:
                x1, y1 = point.x, point.y
                totalPointsSelected += 1
            elif totalPointsSelected == 1:
                x2, y2 = point.x, point.y
                totalPointsSelected = 0
                canvas.create_line(x1, y1, x2, y2, fill="blue")

def simpleGraphCanvasClicked(event):
    global selectedValue
    if selectedValue == 1:
        draw_point(event)
    elif selectedValue == 2:
        drawEdge(event)

def completeGraph():
    label.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()

    label1 = tk.Label(app, text="Complete Graph")
    label1.grid(row=0, column=0, padx=10, pady=10)
    slider.grid(row=1, column=0, padx=10, pady=10)
    canvas.bind("<Button-1>", draw_point)
    canvas.grid(row=3, column=0, padx=10, pady=10)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(2, weight=1)

    


app = tk.Tk()
app.geometry("800x600")

app.title("Graph Theory Project")

label = tk.Label(app, text="Main Page")
selectedValue = -1
radio_var = tk.IntVar()
btn1 = tk.Button(app, text="Draw Simple Graph", command=simpleGraph, bg=homePageButtonColor)
btn2 = tk.Button(app, text="Generate Complete Graph", command=completeGraph, bg=homePageButtonColor)
btn3 = tk.Button(app, text="Bipartite and Tripartite Graph", command=clear_content, bg=homePageButtonColor)
btn4 = tk.Button(app, text="Havel Hakimi", command=clear_content, bg=homePageButtonColor)
radio_button1 = tk.Radiobutton(app, text="Add Vertices", variable=radio_var, value=1, command=on_radio_select)
radio_button2 = tk.Radiobutton(app, text="Add Edges", variable=radio_var, value=2, command=on_radio_select)
canvas = tk.Canvas(app, width=450, height=450, bg="lightgray")
slider = tk.Scale(
    app,
    from_=10,
    to=100,
    orient=tk.HORIZONTAL,
    length=200,
    command=update_label
)
sliderValue = 10


label.grid(row=0, column=0, padx=10, pady=10)
btn1.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
btn2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
btn3.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
btn4.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
# canvas.grid(row=2, column=0, padx=10, pady=10)

# app.columnconfigure(0, weight=1)

# app.rowconfigure(2, weight=1)

app.mainloop()
