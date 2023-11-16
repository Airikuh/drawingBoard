from cis515 import *


# callback function for mouse click
def clicked(mx, my):
    global x, y, drawn
    drawn = True  # whenever a mouse is clicked, start to draw
    x = mx
    y = my

# draw function
def draw_frame():
    global first_time, old_x, old_y, x, y
    global first_click, second_time
    global pressed_R, pressed_G, pressed_B, pressed_Y, pressed_W
    if first_time is True:
        #set_clear_color(0, 0, 0)
        set_clear_color(0.0, 0.0, 0.0)
        clear()
        set_stroke_width(2)
        first_time = False  # Make sure the setting is done only once
        old_x = x
        old_y = y

    if pressed_R == True:
        set_stroke_color(1.0, 0, 0)
    elif pressed_B == True:
        set_stroke_color(0, 0, 1.0)
        #previous version
    #else:
        #set_stroke_color(0, 1.0, 0)
    elif pressed_G == True:
        set_stroke_color(0, 1.0, 0)
        #might not be correct yellow color
    elif pressed_Y == True:
        set_stroke_color(1.0, 1.0, 0)
        #might not be correct color
    else:
        set_stroke_color(1.0, 1.0, 1.0)
    






    if drawn: # at beginning or when a key is pressed, don't draw until 
              # a mouse is clicked
              
        if first_click is True:  # avoid start from (0, 0)
            old_x = x
            old_y = y
            first_click = False
        
        
        draw_line(old_x, old_y, x, y)
        old_x = x
        old_y = y

# callback function for key press
def keydown(key):
    global pressed_R, pressed_G, pressed_B, pressed_Y, pressed_W
    global first_click, drawn

    if key == "r":
        pressed_R = True
        pressed_G = False
        pressed_B = False
        pressed_Y = False
        pressed_W = False
        first_click = True
        drawn = False
    elif key == "b":
        pressed_B = True
        pressed_R = False
        pressed_G = False
        pressed_Y = False
        pressed_W = False
        first_click = True
        drawn = False
    elif key == "g":
        pressed_G = True
        pressed_R = False
        pressed_B = False
        pressed_Y = False
        pressed_W = False
        first_click = True
        drawn = False
    elif key == "y":
        pressed_G = False
        pressed_R = False
        pressed_B = False
        pressed_Y = True
        pressed_W = False
        first_click = True
        drawn = False
    elif key == "w":
        pressed_G = False
        pressed_R = False
        pressed_B = False
        pressed_Y = False
        pressed_W = True
        first_click = True
        drawn = False

old_x = 0
old_y = 0
x = 0
y = 0
drawn = False
first_time = True
first_click = True
pressed_R = False
pressed_G = True
pressed_B = False


start_graphics(draw_frame, 2400, mouse_press=clicked, key_press=keydown)

#start_graphics(draw_frame, mouse_press=clicked, key_press=keydown)

