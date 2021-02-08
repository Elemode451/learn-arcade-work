


import arcade


arcade.open_window(600, 600, "Drawing Example")


arcade.set_background_color(arcade.csscolor.RED)


arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,599,300,0,arcade.csscolor.BEIGE)
arcade.draw_rectangle_filled(100, 320, 20, 100, arcade.csscolor.LIME_GREEN)
arcade.draw_circle_filled(100, 350, 50, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(350, 320, 20, 100, arcade.csscolor.LIME_GREEN)
arcade.draw_circle_filled(350, 350, 40, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(225,320,20,270, arcade.csscolor.LIME_GREEN)
arcade.draw_parabola_filled(170,320,280,100, arcade.csscolor.SKY_BLUE)
arcade.draw_text("How it feels to go outside after working for six hours straight",
                 150, 230,
                 arcade.color.BLACK, 11)
arcade.draw_rectangle_filled(500, 320, 20, 100, arcade.csscolor.LIME_GREEN)
arcade.draw_arc_filled(500, 320, 90, 100, arcade.csscolor.YELLOW, 0, 180)


arcade.finish_render()
