# It imports the turtle module.
import turtle

# Defining the coordinates of the tree and the branch.
branch_list = [[50, 0], [-50, 0], [-50, -100], [50, -100], [50, 0]]
tree_list = [[0, 400], [-100, 300], [-50, 300], [-150, 200], [-50, 200], [-200, 0], [200, 0], [50, 200], [150, 200], [50, 300], [100, 300], [0, 400]]

# Creating a window and setting the speed of the turtle to 1000.
window = turtle.Screen()
turtle.speed(1000)
turtle = turtle.Turtle()

def draw_tree(tree_list):
    """
    It takes a list of coordinates and draws a filled in shape with those coordinates.
    
    :param tree_list: a list of coordinates that make up the tree
    """
    turtle.color("green")
    turtle.begin_fill()
    for edges in tree_list:
        turtle.goto(edges)
    turtle.end_fill()
    turtle.penup()
    

def draw_branch(branch_list):
    """
    It takes a list of coordinates and draws a brown line between them.
    
    :param branch_list: a list of tuples, each tuple is a point on the branch
    """
    turtle.color("brown")
    turtle.begin_fill()
    for branch in branch_list:
        turtle.goto(branch)
    turtle.end_fill()

def draw_star():
    """
    It draws a star.
    """
    turtle.goto(-50, 400)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()

def message():
    """
    It writes "Merry Christmas" in red at the coordinates (-50, -150)
    """
    turtle.goto(-50, -150)
    turtle.color("red")
    turtle.write("Merry Christmas", font=("Arial", 40, "normal"))
    
def draw_full_tree():
    """
    It draws a tree, a branch, and a star.
    """
    draw_tree(tree_list)
    draw_branch(branch_list)
    draw_star()

# Calling the functions draw_full_tree() and message().
draw_full_tree()
message()

# It keeps the window open until the user closes it.
window.mainloop()