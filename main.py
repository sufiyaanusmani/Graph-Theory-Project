import tkinter as tk
import customtkinter
import math

homePageButtonColor = 'blue'
totalPointsSelected = 0
x1, y1, x2, y2 = 0, 0, 0, 0
canvasDimension = 450
colorTemp = "white"
vertexRadius = 6
degreeSequence = []
graphExists = False
userInput = ""


class Point:
    def __init__(self, x, y, color="red"):
        self.x = x
        self.y = y
        self.color = color

points = []

def draw_point(event):
    global points
    global selectedValue
    global vertexRadius
    x = event.x
    y = event.y
    if selectedValue == 1:
        points.append(Point(x, y))
        canvas.create_oval(x-vertexRadius, y-vertexRadius, x+vertexRadius, y+vertexRadius, fill="red")


def on_radio_select():
    global selectedValue
    selectedValue = radio_var.get()

def completeGraphSlider(value):
    global sliderValue
    global vertexRadius
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
        canvas.create_oval(x - vertexRadius, y - vertexRadius, x + vertexRadius, y + vertexRadius, fill="red")

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
    btn5.destroy()

def simpleGraph():
    clear_content()

    label1 = customtkinter.CTkLabel(app, text="Simple Graph")
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
    global colorTemp

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
                canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

def simpleGraphCanvasClicked(event):
    global selectedValue
    if selectedValue == 1:
        draw_point(event)
    elif selectedValue == 2:
        drawEdge(event)

def completeGraph():
    clear_content()

    label1 = customtkinter.CTkLabel(app, text="Complete Graph")
    label1.grid(row=0, column=0, padx=10, pady=10)
    slider.grid(row=1, column=0, padx=10, pady=10)
    canvas.bind("<Button-1>", draw_point)
    canvas.grid(row=3, column=0, padx=10, pady=10)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(2, weight=1)

def drawBipartitePoint(event):
    global points
    global selectedValue
    global vertexRadius
    x = event.x
    y = event.y
    mid = canvasDimension // 2
    if selectedValue == 1:
        if x < mid:
            color = "red"
        else:
            color = "green"
        points.append(Point(x, y, color))
        canvas.create_oval(x-vertexRadius, y-vertexRadius, x+vertexRadius, y+vertexRadius, fill=color)

def drawBipartiteEdge(event):
    global points
    global selectedValue
    global totalPointsSelected
    global x1
    global y1
    global x2
    global y2
    global colorTemp

    x = event.x
    y = event.y
    for point in points:
        if(abs(point.x - x) <= 5 and abs(point.y - y) <= 5):
            if totalPointsSelected == 0:
                x1, y1 = point.x, point.y
                totalPointsSelected += 1
                colorTemp = point.color
            elif totalPointsSelected == 1:
                x2, y2 = point.x, point.y
                totalPointsSelected = 0
                if point.color != colorTemp:
                    canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

def bipartiteGraphCanvasClicked(event):
    global selectedValue
    if selectedValue == 1:
        drawBipartitePoint(event)
    elif selectedValue == 2:
        drawBipartiteEdge(event)

def bipartiteGraphButtonClicked():
    global selectedValue
    global canvasDimension
    selectedValue = -1
    clear_content()

    label1 = customtkinter.CTkLabel(app, text="Bipartite Graph")
    label1.grid(row=0, column=0, padx=10, pady=10)
    radio_button1.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    radio_button2.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    canvas.create_line(canvasDimension // 2, 0,  canvasDimension // 2, canvasDimension, width=1, fill="grey")
    canvas.bind("<Button-1>", bipartiteGraphCanvasClicked)
    canvas.grid(row=3, column=0, padx=10, pady=10)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(2, weight=1)

def drawTripartitePoint(event):
    global points
    global selectedValue
    global vertexRadius
    x = event.x
    y = event.y
    mid1 = canvasDimension // 3
    mid2 = 2 * mid1
    if selectedValue == 1:
        if x < mid1:
            color = "red"
        elif x > mid1 and x < mid2:
            color = "green"
        else:
            color = "yellow"
        points.append(Point(x, y, color))
        canvas.create_oval(x-vertexRadius, y-vertexRadius, x+vertexRadius, y+vertexRadius, fill=color)

def drawTripartiteEdge(event):
    global points
    global selectedValue
    global totalPointsSelected
    global x1
    global y1
    global x2
    global y2
    global colorTemp

    x = event.x
    y = event.y
    for point in points:
        if(abs(point.x - x) <= 5 and abs(point.y - y) <= 5):
            if totalPointsSelected == 0:
                x1, y1 = point.x, point.y
                totalPointsSelected += 1
                colorTemp = point.color
            elif totalPointsSelected == 1:
                x2, y2 = point.x, point.y
                totalPointsSelected = 0
                if point.color != colorTemp:
                    canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

def tripartiteGraphCanvasClicked(event):
    global selectedValue
    if selectedValue == 1:
        drawTripartitePoint(event)
    elif selectedValue == 2:
        drawTripartiteEdge(event)

def tripartiteGraphButtonClicked():
    global selectedValue
    global canvasDimension
    selectedValue = -1
    clear_content()

    label1 = customtkinter.CTkLabel(app, text="Tripartite Graph")
    label1.grid(row=0, column=0, padx=10, pady=10)
    radio_button1.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    radio_button2.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    canvas.create_line(canvasDimension // 3, 0,  canvasDimension // 3, canvasDimension, width=1, fill="grey")
    canvas.create_line((canvasDimension // 3) * 2, 0,  (canvasDimension // 3) * 2, canvasDimension, width=1, fill="grey")
    canvas.bind("<Button-1>", tripartiteGraphCanvasClicked)
    canvas.grid(row=3, column=0, padx=10, pady=10)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(2, weight=1)

def havelHakimiSteps(a, steps):
    for ch in a:
        steps += f'{ch},'
    steps = steps[:-1]
    steps += '\n'
    return steps

def havelHakimi():
    global degreeSequence
    global graphExists
    global userInput
    userInput = str(text.get())
    userInput = userInput.split(',')
    degreeSequence = [int(x) for x in userInput]
    graphExists = False
    steps = ""
    a = degreeSequence
    l = []
    havelHakimiStepsLabel = tk.Label(app, height=10, text="")
    havelHakimiStepsLabel.grid(row=5, column=0, padx=10, pady=10)
    havelHakimiStepsLabel.config(text=steps)
    while True: 
        steps = havelHakimiSteps(a, steps)
        havelHakimiStepsLabel.config(text=steps)
        a = sorted(a, reverse = True)
        steps = havelHakimiSteps(a, steps)
        havelHakimiStepsLabel.config(text=steps)
        l.append(a)
        if a[0]== 0 and a[len(a)-1]== 0:
            graphExists = True
            steps += 'Graph Exists'
            havelHakimiStepsLabel.config(text=steps)
            return

        v = a[0]
        a = a[1:]
 
        if v>len(a): 
            graphExists = False
            steps = havelHakimiSteps(a, steps)
            steps += 'Graph Does Not Exists'
            havelHakimiStepsLabel.config(text=steps)
            return
 
        for i in range(v):
            a[i]-= 1
            if a[i]<0:
                graphExists = False
                steps = havelHakimiSteps(a, steps)
                steps += 'Graph Does Not Exists'
                havelHakimiStepsLabel.config(text=steps)
                return
            


def havelHakimiWindow():
    global userInput
    clear_content()
    label1 = customtkinter.CTkLabel(app, text="Havel Hakimi")
    label1.grid(row=0, column=0, padx=10, pady=10)
    label2 = customtkinter.CTkLabel(app, text="Enter degree sequence")
    label2.grid(row=1, column=0, padx=10, pady=10)
    
    text.grid(row=2, column=0, padx=10, pady=10)
    btn6 = customtkinter.CTkButton(app, text="Run", command=havelHakimi)
    btn6.grid(row=3, column=0, padx=10, pady=10)

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')
app = customtkinter.CTk()
windowWidth = 800
windowHeight = 600
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_position = (screen_width - windowWidth) // 2
y_position = (screen_height - windowHeight) // 2

app.geometry(f"{windowWidth}x{windowHeight}+{x_position}+{y_position}")
app.title("Graph Theory Project")

label = customtkinter.CTkLabel(app, text="Main Page", font=("Helvetica", 20))
selectedValue = -1
radio_var = tk.IntVar()
btn1 = customtkinter.CTkButton(app, text="Draw Simple Graph", command=simpleGraph)
btn2 = customtkinter.CTkButton(app, text="Generate Complete Graph", command=completeGraph)
btn3 = customtkinter.CTkButton(app, text="Bipartite Graph", command=bipartiteGraphButtonClicked)
btn4 = customtkinter.CTkButton(app, text="Tripartite Graph", command=tripartiteGraphButtonClicked)
btn5 = customtkinter.CTkButton(app, text="Havel Hakimi", command=havelHakimiWindow)
radio_button1 = customtkinter.CTkRadioButton(app, text="Add Vertices", variable=radio_var, value=1, command=on_radio_select)
radio_button2 = customtkinter.CTkRadioButton(app, text="Add Edges", variable=radio_var, value=2, command=on_radio_select)
canvas = customtkinter.CTkCanvas(app, width=canvasDimension, height=canvasDimension, bg="grey")
text = customtkinter.CTkEntry(app, textvariable=userInput)
slider = customtkinter.CTkSlider(
    app,
    from_=10,
    to=100,
    orientation=tk.HORIZONTAL,
    width=200,
    command=completeGraphSlider
)
sliderValue = 10

app.columnconfigure(0, weight=1) 
label.grid(row=0, column=0, padx=10, pady=10)
btn1.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
btn2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
btn3.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
btn4.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
btn5.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
# canvas.grid(row=2, column=0, padx=10, pady=10)

# app.columnconfigure(0, weight=1)

# app.rowconfigure(2, weight=1)

app.mainloop()
