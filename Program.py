# by MagykalMystique
from turtle import *
button_shape = "square"
color_load_speed = 0 #it's 0 so that loading the color buttons doesn't take forever :P
t2 = Turtle()# This creates the 2nd turtle pen

# turtle buttons named by their color; 21 total drawing colors to choose from :)
# I abbreviated some of the names, but they're fairly easy to read
powblue = Turtle()
royal_B = Turtle()
blue = Turtle()
red = Turtle()
dark_O = Turtle()
orange = Turtle()
light_G = Turtle()
sea_G = Turtle()
green = Turtle()
yellow = Turtle()
magenta = Turtle()
peach = Turtle()
aqua = Turtle()
teal = Turtle()
black = Turtle()
purple = Turtle()
indigo = Turtle()
gray = Turtle()
violet = Turtle()
silver = Turtle()
gold = Turtle()

# this is probably a bit of an eyesore, it looks like a lot, but really
# all it's doing is creating the different color buttons and placing them
# on the screen. It also places the second pen :) the second pen is smaller than the first
def place_colors():
    shape("triangle")

    powblue.speed(color_load_speed)
    powblue.color("PowderBlue")
    powblue.shape(button_shape)
    powblue.pu()
    powblue.goto(-500,-300)

    royal_B.speed(color_load_speed)
    royal_B.color("royal blue")
    royal_B.shape(button_shape)
    royal_B.pu()
    royal_B.goto(-450,-300)

    blue.speed(color_load_speed)
    blue.color("blue")
    blue.shape(button_shape)
    blue.pu()
    blue.goto(-400,-300)

    red.speed(color_load_speed)
    red.color("red")
    red.shape(button_shape)
    red.pu()
    red.goto(-350,-300)

    dark_O.speed(color_load_speed)
    dark_O.color("orange red")
    dark_O.shape(button_shape)
    dark_O.pu()
    dark_O.goto(-300,-300)

    orange.speed(color_load_speed)
    orange.color("orange")
    orange.shape(button_shape)
    orange.pu()
    orange.goto(-250,-300)
    
    light_G.speed(color_load_speed)
    light_G.color("pale green")
    light_G.shape(button_shape)
    light_G.pu()
    light_G.goto(-200,-300)

    sea_G.speed(color_load_speed)
    sea_G.color("SeaGreen2")
    sea_G.shape(button_shape)
    sea_G.pu()
    sea_G.goto(-150,-300)

    green.speed(color_load_speed)
    green.color("green")
    green.shape(button_shape)
    green.pu()
    green.goto(-100,-300)

    yellow.speed(color_load_speed)
    yellow.color("yellow")
    yellow.shape(button_shape)
    yellow.pu()
    yellow.goto(-50,-300)

    gold.speed(color_load_speed)
    gold.color("goldenrod")
    gold.shape(button_shape)
    gold.pu()
    gold.goto(0,-300)

    magenta.speed(color_load_speed)
    magenta.color("magenta")
    magenta.shape(button_shape)
    magenta.pu()
    magenta.goto(50,-300)
    
    peach.speed(0)
    peach.color("Salmon")
    peach.shape(button_shape)
    peach.pu()
    peach.goto(100,-300)
    
    aqua.speed(color_load_speed)
    aqua.color("aqua")
    aqua.shape(button_shape)
    aqua.pu()
    aqua.goto(150,-300)
    
    teal.speed(color_load_speed)
    teal.color("turquoise4")
    teal.shape(button_shape)
    teal.pu()
    teal.goto(200,-300)
     
    purple.speed(color_load_speed)
    purple.color("purple")
    purple.shape(button_shape)
    purple.pu()
    purple.goto(250,-300)
    
    indigo.speed(color_load_speed)
    indigo.color("indigo")
    indigo.shape(button_shape)
    indigo.pu()
    indigo.goto(300,-300)

    violet.speed(color_load_speed)
    violet.color("VioletRed")
    violet.shape(button_shape)
    violet.pu()
    violet.goto(350,-300)
    
    black.speed(color_load_speed)
    black.color("black")
    black.shape(button_shape)
    black.pu()
    black.goto(400,-300)

    gray.speed(color_load_speed)
    gray.color("gray")
    gray.shape(button_shape)
    gray.pu()
    gray.goto(450,-300)

    silver.speed(color_load_speed)
    silver.color("silver")
    silver.shape(button_shape)
    silver.pu()
    silver.goto(500,-300)
    
# and lastly, the 2nd turtle pen is placed a little to the left so it is visible
    t2.shape("classic")
    t2.pu()
    t2.goto(-50,0)
    t2.pd()

###### Cleaning/Reseting the screen ######
def clean():
    resetscreen()
    screensize(canvwidth=1100, canvheight=700, bg=None)
    place_colors()
    
###### callback functions to change the turtles'  colors #####
    
# again it looks like a lot, but that's really only because
# I made a lot of color options available :)
def color1(x,y):
    color("PowderBlue")
def color2(x,y):
    t2.color("PowderBlue")

def color3(x,y):
    color("royal blue")
def color4(x,y):
    t2.color("royal blue")

def color5(x,y):
    color("blue")
def color6(x,y):
    t2.color("blue")

def color7(x,y):
    color("red")
def color8(x,y):
    t2.color("red")

def color9(x,y):
    color("orange red")
def color10(x,y):
    t2.color("orange red")
    
def color11(x,y):
    color("orange")
def color12(x,y):
    t2.color("orange")

def color13(x,y):
    color("pale green")
def color14(x,y):
    t2.color("pale green")

def color15(x,y):
    color("SeaGreen2")
def color16(x,y):
    t2.color("SeaGreen2")

def color17(x,y):
    color("green")
def color18(x,y):
    t2.color("green")

def color19(x,y):
    color("yellow")
def color20(x,y):
    t2.color("yellow")

def color21(x,y):
    color("goldenrod")
def color22(x,y):
    t2.color("goldenrod")

def color23(x,y):
    color("magenta")
def color24(x,y):
    t2.color("magenta")

def color25(x,y):
    color("Salmon")
def color26(x,y):
    t2.color("Salmon")

def color27(x,y):
    color("aqua")
def color28(x,y):
    t2.color("aqua")

def color29(x,y):
    color("turquoise4")
def color30(x,y):
    t2.color("turquoise4")

def color31(x,y):
    color("purple")
def color32(x,y):
    t2.color("purple")

def color33(x,y):
    color("indigo")
def color34(x,y):
    t2.color("indigo")

def color35(x,y):
    color("VioletRed")
def color36(x,y):
    t2.color("VioletRed")

def color37(x,y):
    color("black")
def color38(x,y):
    t2.color("black")

def color39(x,y):
    color("gray")
def color40(x,y):
    t2.color("gray")

def color41(x,y):
    color("silver")
def color42(x,y):
    t2.color("silver")

######### Moving the 2nd turtle ###########

# orients the 2nd turtle to face the left and moves 20 pixels forward
def move_left2():
    t2.setheading(180)
    t2.fd(20)

# orients the 2nd turtle to face the right and moves 20 pixels forward
def move_right2():
    t2.setheading(0)
    t2.fd(20)

# orients the 2nd turtle to face up and moves 20 pixels forward    
def move_up2():
    t2.setheading(90)
    t2.fd(20)

# orients the 2nd turtle to face down and moves 20 pixels forward    
def move_down2():
    t2.setheading(270)
    t2.fd(20)


#####shape/special draw functions#####

# draws a lattice pattern with the 2nd turtle
def draw_lattice():
    for i in range(50):
        t2.fd(5)
        t2.right(20)
        t2.left(15)
        t2.fd(35)
        t2.right(45)
        t2.fd(50)

# this also draws a lattice-like object, but of course the end result is
# different from above
def draw_lattice2():
    for i in range (30):
        t2.circle(200, extent = 45, steps = 3)
        t2.left(20)
        t2.circle(200, extent = 45, steps = 3)
        t2.left(60)

# draws a filled pentagon with the 2nd turtle
def draw_pent():
    t2.begin_fill()
    t2.circle (75, steps = 5)
    t2.end_fill()

# draws a filled teardrop with the 2nd turtle
def draw_drop():
    t2.begin_fill()
    t2.circle(65, extent = 180)
    t2.right(30)
    t2.circle(75, steps = 3)
    t2.end_fill()

# draws a filled trapezoid with the 2nd turtle
def draw_trapzd():
    t2.begin_fill()
    t2.circle(75, extent = 180, steps = 3)
    t2.end_fill()

# draws a filled circle with the 2nd turtle
def draw_circle():
    t2.begin_fill()
    t2.circle(65)
    t2.end_fill()

# draws a filled triangle with the 2nd turtle
def draw_tri():
    t2.begin_fill()
    t2.circle(75, steps=3)
    t2.end_fill()






###### beginning of the program #####

    
#this right here makes the screen bigger :)    
screensize(canvwidth=1100, canvheight=700, bg=None)
place_colors()
print(""" HELLO! AND WELCOME TO SHAYLA'S SCRIBBLE SCREEN! PLEASE READ THE FOLLOWING
TIPS/INSTRUCTIONS TO MAKE THE MOST OUT OF YOUR THERAPUTIC DOODLING EXPERIENCE AND MOST IMPORTANTLY,
RELAX AND SCRIBBLE AWAY YOUR STRESS :D

********There are two different pen tips*********

***The pen tip shaped like a triangle is a free-draw pen that follows mouse movement
when clicked and dragged.
   *To change this pen tip's color, left-click one of the color buttons.
   *To lift up the triangle pen tip, so you can move it without making marks on the screen,
press "1". To put it back down again, press "2".
      
***The pen tip shaped like an arrow is for drawing straight lines, you can move it using the arrow keys.
You can also use this pen to draw special shapes and patterns :D
   *To change this pen tip's color, right click one of the color buttons
   *To lift up the arrow pen tip so you can move it without making marks on the screen, press "!". To put it down
again, press"@".
   *To draw the first special pattern with the arrow-shaped pen tip, press "3"
   *To draw the second special pattern with the arrow-shaped pen tip, press "4"
   *To draw a filled pentagon with the arrow-shaped pen tip, press "5"
   *To draw a filled teardrop with the arrow-shaped pen tip, press "6"
   *To draw a filled trapezoid with the arrow-shaped pen tip, press "7"
   *To draw a filled circle with the arrow-shaped pen tip, press "8"
   *To draw a filled triangle with the arrow-shaped pen tip, press "9"
   
*******To reset the drawing screen, press SPACEBAR********
""")


listen()

##### drawing functions with key mapping #####

onkey(draw_lattice, "3")
onkey(draw_lattice2, "4")
onkey(draw_pent,"5")
onkey(draw_drop, "6")
onkey(draw_trapzd, "7")
onkey(draw_circle, "8")
onkey(draw_tri, "9")

###### Basic utilities #####

# resets the screen 
onkey(clean, "space")

# penup and pendown for the turtles linked to specific keys
onkey(pu,"1")
onkey(t2.pu, "!")
onkey(pd, "2")
onkey(t2.pd, "@")

# click and drag to move 1st turtle 
ondrag(goto)
# arrow keys to move 2nd turtle 
onkey(move_up2, "Up")
onkey(move_down2, "Down")
onkey(move_left2, "Left")
onkey(move_right2, "Right")

###### changing pen colors #######

# these all change the 2nd or first turtle's pen color when the corresponding button is
# left-clicked or right-clicked
# the btn=3 part differentiates and makes turtle
# respond to a right-click rather than a left-click

powblue.onclick(color1)
powblue.onclick(color2, btn = 3)

royal_B.onclick(color3)
royal_B.onclick(color4, btn = 3)

blue.onclick(color5)
blue.onclick(color6, btn = 3)

red.onclick(color7)
red.onclick(color8, btn = 3)

dark_O.onclick(color9)
dark_O.onclick(color10, btn = 3)

orange.onclick(color11)
orange.onclick(color12, btn = 3)

light_G.onclick(color13)
light_G.onclick(color14, btn = 3)

sea_G.onclick(color15)
sea_G.onclick(color16, btn = 3)

green.onclick(color17)
green.onclick(color18, btn = 3)

yellow.onclick(color19)
yellow.onclick(color20, btn = 3)

gold.onclick(color21)
gold.onclick(color22, btn = 3)

magenta.onclick(color23)
magenta.onclick(color24, btn = 3)

peach.onclick(color25)
peach.onclick(color26, btn = 3)

aqua.onclick(color27)
aqua.onclick(color28, btn = 3)

teal.onclick(color29)
teal.onclick(color30, btn = 3)

purple.onclick(color31)
purple.onclick(color32, btn = 3)

indigo.onclick(color33)
indigo.onclick(color34, btn = 3)

violet.onclick(color35)
violet.onclick(color36, btn = 3)

black.onclick(color37)
black.onclick(color38, btn = 3)

gray.onclick(color39)
gray.onclick(color40, btn = 3)

silver.onclick(color41)
silver.onclick(color42, btn = 3)


# instead of using exitonclick, I decided to have the program execute bye()
# on clicking the ESC key. The reason for this is that choosing a turtle color
# requires being able to click the turtles. I tried using exitonclick(), but
# it would close out the program even when I clicked a specific turtle
# This way, you can use alllll the fun colors I put, which you'd better
# enjoy... it took **4 hours** to set it up! XD
onkey(bye, "Escape")


