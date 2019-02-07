import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

        #square
   
        brad =  turtle.Turtle()
        brad.shape("turtle")
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)

        #circle   
        antur = turtle.Turtle()
        antur.shape("arrow")
        antur.color("blue")
        antur.circle(100)

        #star
        star = turtle.Turtle()
        for i in range(50):
            star.forward(50)
            star.right(144)
        
        turtle.clickonexit()
  
draw_art()
