import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
my_Dog = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
my_Dog.shape('turtle')
# Set your turtle's speed using .speed(2)
my_Dog.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
my_Dog.color('blue')
my_Dog.pencolor('red')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
my_Dog.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
my_Dog.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
my_Dog.forward(100)
my_Dog.left(90)
my_Dog.forward(100)
my_Dog.left(90)
my_Dog.forward(100)
my_Dog.left(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
my_Dog.goto(x=100, y=100)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
my_Dog.begin_fill()
my_Dog.circle(20, steps=30)
my_Dog.end_fill()
# Draw 3 more shapes with different fill colors!
my_Dog.goto(x=200, y=200)
my_Dog.begin_fill()
my_Dog.forward(100)
my_Dog.left(90)
my_Dog.forward(100)
my_Dog.left(90)
my_Dog.forward(100)
my_Dog.left(90)
my_Dog.end_fill()
my_Dog.goto(x=180, y=40)
my_Dog.begin_fill()
my_Dog.circle(20, steps=30)
my_Dog.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
