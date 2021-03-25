# Import Library
import arcade

def fins():
    arcade.draw_triangle_filled(300, 250, 300, 300, 250, 250, arcade.color.ASH_GREY)
    arcade.draw_triangle_filled(300, 250, 300, 300, 350, 250, arcade.color.DAVY_GREY)

def wind():
    arcade.draw_line(100, 500, 250, 470, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_line(400, 500, 550, 450, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_line(221, 300, 140, 210, arcade.csscolor.WHITE_SMOKE)
def fire():
    arcade.draw_parabola_filled(260, 200, 340, 30, arcade.csscolor.ORANGE_RED)
    arcade.draw_parabola_filled(320, 200, 280, 40, arcade.csscolor.ORANGE)

def bodyofrocket():
    arcade.draw_circle_filled(300, 420, 25, arcade.color.RED_DEVIL)
    arcade.draw_rectangle_filled(300, 350, 50, 150, arcade.color.COOL_GREY)

def startupprogram():
   # Background color, I used the same one as the website since I like it
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    # Get ready to draw
    arcade.start_render()

def finishprogram():

    arcade.finish_render()
    arcade.run()

arcade.open_window(600, 600, "Drawing")

startupprogram()
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.LIME)
wind()
fire()
fins()
bodyofrocket()
finishprogram()





