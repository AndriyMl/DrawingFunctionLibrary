import turtle

class GraphFunction:
    all_functions = []

    def __init__(self,function: str):
        self.function = function
        GraphFunction.all_functions.append(self.function)

    def __add__(self, other):
        if isinstance(other, GraphFunction):
            pass
        return self
    # Function drawing function
    def draw_function(self,line_size = 200,color = "red",pen_size = 1,speed = 0,coordinate = (True, 250)):
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
            left, element = element.split("=")
            x = -(line_size / 2)

            turtle.pensize(pen_size)
            turtle.pencolor(color)
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