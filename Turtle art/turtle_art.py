import turtle

def draw_square(brush_obj, length,color):
    brush_obj.color(color)
    for i in range(1,5):
        brush_obj.forward(length)
        brush_obj.right(90)
def draw_circle(brush_obj, radius,color):
    brush_obj.color(color)
    brush_obj.circle(radius)
        
def turtle_art():
    window = turtle.Screen()
    window.bgcolor("orange")
    brush = turtle.Turtle()
    brush.shape("turtle")
    brush.speed(20)
    for i in range(1,37):
        draw_square(brush,150,"red")
        draw_circle(brush,75,"black")
        brush.right(10)
    window.exitonclick()

turtle_art()
