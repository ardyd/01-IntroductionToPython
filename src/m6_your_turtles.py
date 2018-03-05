"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and David Ardy.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

tyler1 = rg.SimpleTurtle('turtle')
tyler1.pen = rg.Pen('red', 5)
tyler1.speed = 15

imaqtpie = rg.SimpleTurtle('turtle')
imaqtpie.pen = rg.Pen('blue', 3)
imaqtpie.speed = 20

sizet1 = 100
sizeqt = 75

for k in range(15):
    tyler1.draw_circle(sizet1)

    tyler1.pen_up()
    tyler1.forward(20)
    tyler1.left(45)
    tyler1.pen_down()

    sizet1 = sizet1 - 4

for k in range(13):
    imaqtpie.draw_square(sizeqt)

    imaqtpie.pen_up()
    imaqtpie.backward(10)
    imaqtpie.right(45)
    imaqtpie.backward(20)
    imaqtpie.pen_down()

    sizeqt = sizeqt - 3

window.close_on_mouse_click()



