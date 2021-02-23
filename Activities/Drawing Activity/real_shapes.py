#Importing Library and creating the window
import arcade
arcade.open_window(600, 600, "Very Cool Drawing Created By Me")
arcade.set_background_color(arcade.csscolor.WHITE)
arcade.start_render()
#shapes start here
arcade.draw_triangle_filled(150, 200, 450, 200, 300, 450, arcade.csscolor.GREEN)
arcade.draw_circle_filled(300,300,40, arcade.csscolor.WHITE)
arcade.draw_circle_filled(300,300,20, arcade.csscolor.BLACK)
arcade.draw_circle_filled(314,315,10, arcade.csscolor.WHITE)
arcade.draw_text("Why is centering text bad", 217.5 , 150, arcade.csscolor.BLACK, font_size=12,)
#stop rendering here
arcade.finish_render()
arcade.run()
