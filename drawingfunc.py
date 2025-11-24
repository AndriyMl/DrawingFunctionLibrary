import turtle


class GraphFunction:
    all_functions = []

    def __init__(self, function, color="red", pen_size=1):
        self.function = function
        self.color = color if not isinstance(color, list) else color
        self.pen_size = pen_size
        GraphFunction.all_functions.append(self)

    def draw_function(self, line_size="infinity", coordinate=(True, 250)):
        screen = turtle.Screen()
        turtle.tracer(False)

        if coordinate[0]:
            turtle.goto(0, -coordinate[1])
            turtle.goto(0, coordinate[1])
            turtle.up()
            turtle.goto(-coordinate[1], 0)
            turtle.down()
            turtle.goto(coordinate[1], 0)

        for func_obj in GraphFunction.all_functions:
            if line_size == "infinity":
                actual_line_size = 2 * 10 ** 3
                step = 1
            else:
                actual_line_size = line_size
                step = 0.1

            functions_list = func_obj.function if isinstance(func_obj.function, list) else [func_obj.function]
            colors_list = func_obj.color if isinstance(func_obj.color, list) else [func_obj.color] * len(functions_list)

            for idx, func_str in enumerate(functions_list):
                if not isinstance(func_str, str):
                    raise TypeError("Function must be string or list of strings")

                element_color = colors_list[idx] if idx < len(colors_list) else colors_list[0]
                element_pen_size = func_obj.pen_size

                left, expression = func_str.split("=")
                x = -(actual_line_size / 2)

                turtle.pensize(element_pen_size)
                turtle.pencolor(element_color)
                turtle.up()

                for i in range(int(actual_line_size / step)):
                    try:
                        y = eval(expression.replace("x", f"({x})"))
                        turtle.goto(x, y)
                        turtle.down()
                    except:
                        turtle.up()
                    x += step

        turtle.update()
        screen.mainloop()

# Test
f1 = GraphFunction(["y=x**2/20-25", "y=-x**2/20+25"], color=["blue", "green"], pen_size=2)
f2 = GraphFunction("y=0*x-25", color="red")
f1.draw_function(line_size="infinity", coordinate=(True, 400))