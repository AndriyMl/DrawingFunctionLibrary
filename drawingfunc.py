import turtle

class GraphFunction:
    all_functions = []

    def __init__(self,function: str,color = "red"):
        self.function = function
        self.color = color
        GraphFunction.all_functions.append(self)

    def __add__(self, other):
        if isinstance(other, GraphFunction):
            pass
        return self
    # Function drawing function
    def draw_function(self,line_size = 200,pen_size = 1,speed = 0,coordinate = (True, 250)):
        screen = turtle.Screen()
        turtle.speed(speed)
        turtle.tracer(False)
        if coordinate[0]:
            turtle.goto(0, -coordinate[1])
            turtle.goto(0, coordinate[1])
            turtle.up()
            turtle.goto(-coordinate[1], 0)
            turtle.down()
            turtle.goto(coordinate[1], 0)

        for element in GraphFunction.all_functions:
            element_color = element.color
            left, element = element.function.split("=")
            x = -(line_size / 2)

            turtle.pensize(pen_size)
            turtle.pencolor(element_color)
            turtle.up()

            for i in range(line_size * 10):
                try:
                    y = eval(element.replace("x", f"({x})"))
                    turtle.goto(x, y)
                    turtle.down()
                except:
                    pass
                x += 0.1

        turtle.update()
        screen.mainloop()

f1 = GraphFunction("y=x**2/20-25",color="blue")
f2 = GraphFunction("y=0/x-25",color="red")
f3 = f1 + f2
f3.draw_function(coordinate=(True, 400))