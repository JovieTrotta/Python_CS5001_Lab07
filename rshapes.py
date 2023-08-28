'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 7 Recursive Psychedelic Turtle

This program is run through the command line. It uses recursive funtions to draw pictures from the user's input. 
There are five options accessed via the main menu: Psychadelic Boxes, Bull's Eye, Turning Spiral, Box Tree, and Realistic Tree.
'''

import sys
import turtle as t

'''
Function that sends the turtle to specific coordinates
Parameters: two integers
Returning: a coordinate in the turtle window
'''
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

'''
Function that sends the turtle to the home position
Parameters: n/a
Returning: a coordinate in the turtle window
'''
def go_home():
    t.penup()
    t.home()
    t.pendown()

'''
Function that brings the turtle back to the home position and clears the screen
Parameters: n/a
Returning: a coordinate in the turtle window
'''
def reset_turtle():
    t.clear()
    go_home()

'''
Function that creates a basic square
Parameters: three integers
Returning: a square drawing
'''
def box(x,y,size):
    goto(x,y)
    count = 0 
    while count < 4:
        t.forward(size)
        t.left(90)
        count += 1
    go_home()

'''
Function that creates a basic circle
Parameters: three integers
Returning: a circle drawing
'''
def circle(x,y,radius):
    goto(x,y)
    t.circle(radius)
    go_home()

'''
Function that creates a shrinking tunnel using recursive squares
Parameters: four integers and a float (scaleDown)
Returning: a pattern using squares
'''
def psych_boxes(x,y,size,scaleDown,min_size):
    # Creates a 1000x1000 px window
    t.setup(1000,1000) 

    # Sets turtle to the fasest speed
    t.speed(0) 

    # Base case
    box(x,y,size) 

    # Recursive step begins
    # If the next box is larger than or equal to the minimum box size, then execute next step
    if (size - scaleDown) >= min_size: 

        # Creates a smaller square and centers it within the previous square
        psych_boxes((x + (0.5*(size * scaleDown))),(y + (0.5*(size * scaleDown))),(size - (size * scaleDown)),scaleDown,min_size) 

'''
Function that creates a bull's eye pattern using recursive circles
Parameters: four integers and a float (scaleDown)
Returning: a pattern using circles
'''
def bulls_eye(x,y,radius,scaleDown,min_radius):
    t.setup(1000,1000) 
    t.speed(0) 

    # Base case
    circle(x,y,radius)

    # Recursive step begins
    # If the next circle is larger than or equal to the minimum radius size, then execute next step
    if (radius - scaleDown) >= min_radius:

        # Creates a smaller circle and centers it within the previous circle
        bulls_eye((x + (0.025*(radius * scaleDown))),(y + (radius * scaleDown)),(radius - (radius * scaleDown)),scaleDown,min_radius)

'''
Function that creates a spiral maze pattern
Parameters: three integers
Returning: a pattern using lines
'''
def draw_spiral(x,y,lineLen):
    t.setup(1000,1000)
    t.speed(0)

    # Go to x and y position on the window
    # This begins the base case
    goto(x,y)

    # Go forward the length of the line
    t.forward(lineLen)

    # Turn right 90 degrees
    t.right(90)

    # Line decreases in size by 5
    # This ends the base case
    lineLen -= 5

    #This takes the current position of the x and y coordinates and changes the value for each to the current position
    x = t.xcor()
    y = t.ycor()

    # Recursive step begins
    # If the length of the line is greater than zero, execute next step
    if lineLen > 0:

        # Draws the line again with the new x, y, and lineLen values
        draw_spiral(x,y,lineLen)

'''
Function that creates a tree of boxes
Parameters: four integers and a float (scaleDown)
Returning: a pattern using squares
'''
def box_tree(x,y,size,scaleDown,min_size):
    t.setup(1000,1000)
    t.speed(0)

    # Base case
    box(x,y,size)

    # Recursive step begins
    # If the size of the scaled down box is greater than the minimum box size, execute the next two functions
    if (size * scaleDown) > min_size:

        # Draws the left box tree until condition is met
        box_tree((x - (size * 0.4)),(y + size),size * scaleDown,scaleDown,min_size)

        # Draws the right box tree once there are no more left boxes to draw
        box_tree((x + (size * 0.9)),(y + size),size * scaleDown,scaleDown,min_size)

'''
Function that creates a realistic looking tree
Parameters: one integer
Returning: a pattern using colored lines and circles
Solution from https://medium.com/@abhinav.mahapatra10/python-beginner-diy-make-fractal-trees-b1a0903414a9
'''
def tree(branchLen):
    t.speed(0)

    # If branchLen is greater than 5, execute the next steps
    if branchLen > 5:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-10)
        t.left(60)
        tree(branchLen-10)
        t.right(30)
        t.backward(branchLen)
    
    # branchLen is now too short, so draw circles at the end of each branch
    else:
        t.circle(5)

'''
Function that creates a menu and allows the user to select their option
Parameters: one integer
Returning: selected function and a string
'''
def menu():
    print("This program will use recursion to draw pictures. Your options are:")
    print("...1 for Psychadelic Boxes.")
    print("...2 for Bull's Eye.")
    print("...3 for Turning Spiral.")
    print("...4 for Box Tree.")
    print("...5 for Realistic Tree.")
    print("...6 to clear the window.")
    print("...0 to close the program.")
    while True:
        menu_choice = input("Please make a selection:\n")
        if menu_choice == "1":
            psych_boxes(int(input("What is the x value?\n")),int(input("What is the y value?\n")),abs(int(input("What is the size?\n"))),0.25,1)
            print("You have selected Psychadelic Boxes.") 
        elif menu_choice == "2":
            bulls_eye(int(input("What is the x value?\n")),int(input("What is the y value?\n")),abs(int(input("What is the radius?\n"))),0.25,1)
            print("You have selected Bull's Eye.")
        elif menu_choice == "3":
            draw_spiral(int(input("What is the x value?\n")),int(input("What is the y value?\n")),abs(int(input("What is the line length?\n"))))
            print("You have selected Turning Spiral.")
        elif menu_choice == "4":
            box_tree(int(input("What is the x value?\n")),int(input("What is the y value?\n")),abs(int(input("What is the size?\n"))),0.5,10)
            print("You have selected Box Tree.")
        elif menu_choice == "5":
            t.setup(1000,1000)

            # Turns the tree so it points upward
            t.left(90)

            # Moves the start point for the tree back 250 px
            t.up()
            t.backward(250)
            t.down()

            # Draws the tree
            tree(100)
            print("You have selected Realistic Tree.")
        elif menu_choice == "6":
            print("Screen cleared.")
            reset_turtle()
        elif menu_choice == "0":
            print("Goodbye!")
            sys.exit()
        else:
            print("Your options are 1, 2, 3, 4, 5, 6, or 0.")

# Driver function
# Calls the main menu
def main():
    menu()
main()