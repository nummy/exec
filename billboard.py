
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: PUT YOUR STUDENT NUMBER HERE
#    Student name: PUT YOUR NAME HERE
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#


#-----Assignment Description-----------------------------------------#
#
#  BILLBOARD
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "paste_up".
#  You are required to complete this function so that when the
#  program is run it produces an image of an advertising billboard
#  whose arrangement is determined by data stored in a list which
#  specifies how individual paper sheets are to be pasted onto the
#  backing.  See the instruction sheet accompanying this file for
#  full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#


#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

sheet_width = 200  # pixels
sheet_height = 500  # pixels
backing_margin = 20  # pixels
backing_width = sheet_width * 4 + backing_margin * 2
backing_height = sheet_height + backing_margin * 2
canvas_top_and_bottom_border = 150  # pixels
canvas_left_and_right_border = 300  # pixels
canvas_width = (backing_width + canvas_left_and_right_border)
canvas_height = (backing_height + canvas_top_and_bottom_border)

#
#--------------------------------------------------------------------#


#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_centre_points=True):

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 5  # pixels
    grass_height = 100  # pixels
    penup()
    goto(-(canvas_width // 2 + overlap),
         -(canvas_height // 2 + overlap))  # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90)  # face north
    forward(grass_height + overlap)
    right(90)  # face east
    forward(canvas_width + overlap * 2)
    right(90)  # face south
    forward(grass_height + overlap)
    end_fill()

    # Draw a nice warm sun peeking into the image
    penup()
    goto(-canvas_width // 2, canvas_height // 2)
    color('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height // 3)
    color('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Draw the billboard's wooden backing as four frames
    # and some highlighted coordinates
    #
    # Outer rectangle
    goto(- backing_width // 2, - backing_height // 2)  # bottom left
    pencolor('sienna')
    fillcolor('tan')
    width(3)
    begin_fill()
    pendown()
    setheading(90)  # face north
    forward(backing_height)
    right(90)  # face east
    forward(backing_width)
    right(90)  # face south
    forward(backing_height)
    right(90)  # face west
    forward(backing_width)
    end_fill()

    # Inner rectangle
    penup()
    goto(- backing_width // 2 + backing_margin,
         - backing_height // 2 + backing_margin)  # bottom left
    fillcolor('gainsboro')
    begin_fill()
    pendown()
    setheading(90)  # face north
    forward(backing_height - backing_margin * 2)
    right(90)  # face east
    forward(backing_width - backing_margin * 2)
    right(90)  # face south
    forward(backing_height - backing_margin * 2)
    right(90)  # face west
    forward(backing_width - backing_margin * 2)
    end_fill()

    # Draw lines separating the locations where the sheets go
    width(1)
    pencolor('dim grey')
    for horizontal in [-sheet_width, 0, sheet_width]:
        penup()
        goto(horizontal, sheet_height // 2)
        pendown()
        setheading(270)  # point south
        forward(sheet_height)

    # Mark the centre points of each sheet's location, if desired
    if mark_centre_points:
        penup()
        points = [[[round(-sheet_width * 1.5), 0], 'Location 1'],
                  [[round(-sheet_width * 0.5), 0], 'Location 2'],
                  [[round(sheet_width * 0.5), 0], 'Location 3'],
                  [[round(sheet_width * 1.5), 0], 'Location 4']]
        for centre_point, label in points:
            goto(centre_point)
            dot(4)
            write('  ' + label + '\n  (' + str(centre_point[0]) + ', 0)',
                  font=('Arial', 12, 'normal'))

    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# End the program by hiding the cursor and releasing the canvas
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()

#
#--------------------------------------------------------------------#


#-----Test Data------------------------------------------------------#
#
# The list in this section contains the data sets you will use to
# test your code.  Each of the data sets is a list specifying the
# way in which sheets are pasted onto the billboard:
#
# 1. The name of the sheet, from 'Sheet A' to 'Sheet D'
# 2. The location to paste the sheet, from 'Location 1' to
#    'Location 4'
# 3. The sheet's orientation, either 'Upright' or 'Upside down'
#
# Each data set does not necessarily mention all four sheets.
#
# In addition there is an extra value, either 'X' or 'O' at the
# start of each data set.  The purpose of this value will be
# revealed only in Part B of the assignment.  You should ignore it
# while completing Part A.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Note that your solution must work for all the data sets below
# AND ANY OTHER DATA SETS IN THE SAME FORMAT!
#

data_sets = [
    # These two initial data sets don't put any sheets on the billboard
    # Data sets 0 - 1
    ['O'],
    ['X'],
    # These data sets put Sheet A in all possible locations and orientations
    # Data sets 2 - 9
    ['O', ['Sheet A', 'Location 1', 'Upright']],
    ['O', ['Sheet A', 'Location 2', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright']],
    ['O', ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 2', 'Upside down']],
    ['O', ['Sheet A', 'Location 3', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down']],
    # These data sets put Sheet B in all possible locations and orientations
    # Data sets 10 - 17
    ['O', ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet B', 'Location 2', 'Upright']],
    ['O', ['Sheet B', 'Location 3', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 1', 'Upside down']],
    ['O', ['Sheet B', 'Location 2', 'Upside down']],
    ['O', ['Sheet B', 'Location 3', 'Upside down']],
    ['O', ['Sheet B', 'Location 4', 'Upside down']],
    # These data sets put Sheet C in all possible locations and orientations
    # Data sets 18 - 25
    ['O', ['Sheet C', 'Location 1', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 3', 'Upright']],
    ['O', ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upside down']],
    ['O', ['Sheet C', 'Location 3', 'Upside down']],
    ['O', ['Sheet C', 'Location 4', 'Upside down']],
    # These data sets put Sheet D in all possible locations and orientations
    # Data sets 26 - 33
    ['O', ['Sheet D', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 2', 'Upright']],
    ['O', ['Sheet D', 'Location 3', 'Upright']],
    ['O', ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet D', 'Location 2', 'Upside down']],
    ['O', ['Sheet D', 'Location 3', 'Upside down']],
    ['O', ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets place two sheets in various locations and orientations
    # Data sets 34 - 38
    ['O', ['Sheet D', 'Location 2', 'Upright'],
     ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
     ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down'],
     ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
     ['Sheet B', 'Location 2', 'Upside down']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
     ['Sheet B', 'Location 2', 'Upside down']],
    # These data sets place three sheets in various locations and orientations
    # Data sets 39 - 43
    ['O', ['Sheet A', 'Location 4', 'Upright'],
     ['Sheet B', 'Location 3', 'Upright'],
     ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upright'],
     ['Sheet A', 'Location 3', 'Upright'],
     ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
     ['Sheet D', 'Location 3', 'Upside down'],
     ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright'],
     ['Sheet D', 'Location 2', 'Upside down'],
     ['Sheet C', 'Location 1', 'Upside down']],
    ['X', ['Sheet A', 'Location 4', 'Upright'],
     ['Sheet D', 'Location 3', 'Upside down'],
     ['Sheet C', 'Location 2', 'Upright']],
    # These data sets place four sheets in various locations and orientations
    # Data sets 44 - 48
    ['O', ['Sheet C', 'Location 1', 'Upright'],
     ['Sheet B', 'Location 2', 'Upright'],
     ['Sheet A', 'Location 3', 'Upright'],
     ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
     ['Sheet B', 'Location 3', 'Upright'],
     ['Sheet D', 'Location 1', 'Upright'],
     ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
     ['Sheet B', 'Location 2', 'Upright'],
     ['Sheet A', 'Location 3', 'Upright'],
     ['Sheet D', 'Location 4', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
     ['Sheet B', 'Location 3', 'Upside down'],
     ['Sheet D', 'Location 1', 'Upside down'],
     ['Sheet A', 'Location 4', 'Upright']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
     ['Sheet B', 'Location 2', 'Upside down'],
     ['Sheet A', 'Location 3', 'Upright'],
     ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets draw the entire image upside down
    # Data sets 49 - 50
    ['X', ['Sheet A', 'Location 4', 'Upside down'],
     ['Sheet B', 'Location 3', 'Upside down'],
     ['Sheet C', 'Location 2', 'Upside down'],
     ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down'],
     ['Sheet B', 'Location 3', 'Upside down'],
     ['Sheet C', 'Location 2', 'Upside down'],
     ['Sheet D', 'Location 1', 'Upside down']],
    # These are the final, 'correct' arrangements of sheets
    # Data sets 51 - 52
    ['X', ['Sheet A', 'Location 1', 'Upright'],
     ['Sheet B', 'Location 2', 'Upright'],
     ['Sheet C', 'Location 3', 'Upright'],
     ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upright'],
     ['Sheet B', 'Location 2', 'Upright'],
     ['Sheet C', 'Location 3', 'Upright'],
     ['Sheet D', 'Location 4', 'Upright']]
]

#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "paste_up" function.
#

# Paste the sheets onto the billboard as per the provided data set
def paste_up(dummy_parameter):
    if len(dummy_parameter) >= 2:
        sheet_lst = dummy_parameter[1:]
        for sheet in sheet_lst:
            location = sheet[1]
            name = sheet[0]
            direction = sheet[2]
            x, y = 0, 0
            if location == "Location 1":
                x = round(-sheet_width * 1.5)
            elif location == "Location 2":
                x = round(-sheet_width * 0.5)
            elif location == "Location 3":
                x = round(sheet_width * 0.5)
            else:
                x = round(sheet_width * 1.5)

            # set background color
            goto(x-sheet_width//2, y-sheet_height//2)
            fillcolor("white")
            begin_fill()
            setheading(90)
            forward(sheet_height)
            right(90)
            forward(sheet_width)
            right(90)
            forward(sheet_height)
            end_fill()

            if name == "Sheet A":
                # draw sheetA
                penup()
                # start point -300, 0
                goto(x, y)
                color("blue")
                dot(180)
                color('white')
                dot(130)
                if direction == "Upright":
                    goto(x-90, y)
                    fillcolor("blue")
                    setheading(90)
                    begin_fill()
                    forward(150)
                    right(90)
                    forward(25)
                    right(90)
                    forward(150)
                    right(90)
                    forward(25)
                    end_fill()
                if direction == "Upside down":
                    goto(x+90, y)
                    fillcolor("blue")
                    setheading(270)
                    begin_fill()
                    forward(150)
                    right(90)
                    forward(25)
                    right(90)
                    forward(150)
                    right(90)
                    forward(25)
                    end_fill()
            elif name == "Sheet B":
                # draw sheetB
                # start point -100, 0
                if direction == "Upright":
                    penup()
                    goto(x, y+130)
                    color("yellow")
                    dot(40)
                    goto(x-15, y+100)
                    fillcolor("yellow")
                    setheading(0)
                    begin_fill()
                    forward(30)
                    right(90)
                    forward(180)
                    right(90)
                    forward(30)
                    end_fill()
                if direction == "Upside down":
                    penup()
                    goto(x, y-130)
                    color("yellow")
                    dot(40)
                    goto(x+15, y-100)
                    fillcolor("yellow")
                    setheading(180)
                    begin_fill()
                    forward(30)
                    right(90)
                    forward(180)
                    right(90)
                    forward(30)
                    end_fill()
            elif name == "Sheet C":
                # draw sheetC
                # start point 100, 0
                if direction == "Upright":
                    penup()
                    goto(x+90, y+40)
                    color("green")
                    setheading(90)
                    begin_fill()
                    circle(90, 180)
                    end_fill()
                    goto(x+70, y+40)
                    color("white")
                    setheading(90)
                    begin_fill()
                    circle(70, 180)
                    end_fill()

                    color("green")
                    goto(x+90, y+40)
                    begin_fill()
                    setheading(-90)
                    forward(120)
                    right(90)
                    forward(20)
                    right(90)
                    forward(120)
                    right(90)
                    forward(20)
                    end_fill()

                    goto(x-70, y+40)
                    begin_fill()
                    setheading(-90)
                    forward(120)
                    right(90)
                    forward(20)
                    right(90)
                    forward(120)
                    end_fill()
                if direction == "Upside down":
                    penup()
                    goto(x-90, y-40)
                    color("green")
                    setheading(270)
                    begin_fill()
                    circle(90, 180)
                    end_fill()
                    goto(x-70, y-40)
                    color("white")
                    setheading(270)
                    begin_fill()
                    circle(70, 180)
                    end_fill()

                    color("green")
                    goto(x-90, y-40)
                    begin_fill()
                    setheading(90)
                    forward(120)
                    right(90)
                    forward(20)
                    right(90)
                    forward(120)
                    right(90)
                    forward(20)
                    end_fill()

                    goto(x+70, y-40)
                    begin_fill()
                    setheading(90)
                    forward(120)
                    right(90)
                    forward(20)
                    right(90)
                    forward(120)
                    end_fill()
            else:
                # sheet D
                # start point 300, 0
                if direction == "Upright":
                    penup()
                    goto(x, y+50)
                    color("red")
                    dot(160)
                    color("white")
                    dot(120)

                    goto(x+80, y+100)
                    setheading(-90)
                    fillcolor("red")
                    begin_fill()
                    forward(180)
                    right(90)
                    forward(20)
                    right(90)
                    forward(180)
                    right(90)
                    forward(20)
                    end_fill()

                    goto(x-80, y-80)
                    begin_fill()
                    setheading(-90)
                    circle(80, 180)
                    end_fill()

                    goto(x-60, y-80)
                    fillcolor("white")
                    begin_fill()
                    setheading(-90)
                    circle(60, 180)
                    end_fill()
                if direction == "Upside down":
                    penup()
                    goto(x, y-50)
                    color("red")
                    dot(160)
                    color("white")
                    dot(120)

                    goto(x-80, y-100)
                    setheading(90)
                    fillcolor("red")
                    begin_fill()
                    forward(180)
                    right(90)
                    forward(20)
                    right(90)
                    forward(180)
                    right(90)
                    forward(20)
                    end_fill()

                    goto(x+80, y+80)
                    begin_fill()
                    setheading(90)
                    circle(80, 180)
                    end_fill()

                    goto(x+60, y+80)
                    fillcolor("white")
                    begin_fill()
                    setheading(90)
                    circle(60, 180)
                    end_fill()
    choice = dummy_parameter[0]
    if choice == "X":
        penup()
        # draw 'C'
        goto(-120, 100)
        pendown()
        pencolor('black')
        pensize(20)
        goto(-200, 90)
        goto(-240, 40)
        goto(-250, 10)
        goto(-250, -30)
        goto(-240, -60)
        goto(-200, -90)
        goto(-120, -90)
        penup()
        # draw 'L'
        goto(-50, 100)
        pendown()
        goto(-52, 80)
        goto(-50, 0)
        goto(-52, -100)
        goto(0, -95)
        goto(80, -100)
        # draw "J"
        penup()
        goto(150, 100)
        pendown()
        goto(250, 100)
        penup()
        goto(200, 100)
        pendown()
        goto(202, 50)
        goto(200, 0)
        goto(203, -50)
        goto(200, -100)
        goto(180, -120)
        goto(160, -140)
        goto(140, -120)
        goto(120, -100)
#
#--------------------------------------------------------------------#


#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your billboard.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the centre points of each sheet on the backing
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with one that describes the image
# ***** displayed on your billboard when the sheets are pasted
# ***** correctly
title("NOKIA")

# Call the student's function to display the billboard
# ***** Change the number in the argument to this function
# ***** to test your code with a different data set
paste_up(data_sets[39])


# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#
