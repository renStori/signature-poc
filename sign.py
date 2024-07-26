import turtle
from helpers import from_coords_to_int
from base62 import int_to_base62

from config import canvas_size

width = canvas_size[0]
height = canvas_size[1]

screen = turtle.Screen()
screen.setup(width=width, height=height)
screen.title("Signature Canvas")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()

painted_pixels = []


def re_coords(coord: tuple) -> tuple:
    return int(coord[0] + (width / 2)), int(coord[1] + (height / 2))


def draw_signature(x, y):
    pen.pendown()
    pen.goto(x, y)
    painted_pixels.append(re_coords((x, y)))


def lift_pen(x, y):
    pen.penup()
    pen.goto(x, y)
    painted_pixels.append(re_coords((x, y)))


screen.onscreenclick(lift_pen)
pen.ondrag(draw_signature)


def close_window():
    screen.bye()

    # Save the list of painted pixels to a text file
    with open("output/painted_pixels", "w") as f:
        for pixel in painted_pixels:
            coords = f"{pixel[0]},{pixel[1]}"
            f.write(str(coords).replace(" ", "") + "\n")
    print("Painted pixel coordinates saved to painted_pixels")

    # Encode the list and save it
    with open("output/painted_pixels_encoded", "w") as f:
        print(painted_pixels)
        b58_string = int_to_base62(from_coords_to_int(painted_pixels))
        f.write(b58_string)
    print("Painted pixel coordinates saved to painted_pixels_encoded")


screen.listen()
screen.onkey(close_window, "q")

turtle.mainloop()
