''' The following program uses a turtle to draw a capital T in white 
 on a green background as shown to the left,
 image of a letter T drawn by Turtle.
 The program should do all necessary set-up, create the turtle, 
 and set the pen size to 10. 
 After that the turtle should turn to face north, draw a line
 that is 150 pixels long, turn to face west, and draw a line that is 50 pixels long.
 Next, the turtle should turn 180 degrees and draw a line that is 100 pixels long. 
 Finally, set the window to close when the user clicks in it.'''


import turtle
wn = turtle.Screen()
wn.bgcolor("green")
jamal = turtle.Turtle()
jamal.pensize(10)
jamal.color("white")
jamal.left(90)
jamal.forward(150)
jamal.left(90)
jamal.forward(50)
jamal.right(180)
jamal.forward(100)