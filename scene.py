import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Grass and sky parameters
    grass_y0 = scene_top + 150
    grass_x1 = scene_right
    sky_x1 = scene_right
    sky_y1 = scene_top + 150
    # Tree parameters
    tree_center = scene_left + 250
    tree_top = scene_top + 100
    tree_height = 120
    tree_center2 = scene_left + 550
    tree_top2 = scene_top + 100
    tree_height2 = 120
    tree_center3 = scene_left + 600
    tree_top3 = scene_top + 150
    tree_height3 = 200
    tree_center4 = scene_left + 700
    tree_top4 = scene_top + 200
    tree_height4 = 300
    # River parameters
    left_topX = scene_left + 300
    left_topY = scene_top + 150
    long_top = 200
    long_bottom = 500
    left_topX2 = scene_left + 325
    left_topY2 = scene_top + 150
    long_top2 = 150
    long_bottom2 = 375
    river_topX = left_topX2 + 25
    river_topY = long_top2
    river_top = long_top2 - 50
    river_bottom = long_bottom2 - 125
    # Cloud Parameters
    top_leftX_cloud = 25
    top_leftY_cloud = 25
    length_cloud = 65

    draw_sky(canvas, scene_left, scene_top, sky_x1, sky_y1)
    draw_cloud(canvas, top_leftX_cloud, top_leftY_cloud, length_cloud)
    draw_cloud(canvas, top_leftX_cloud + 300,
               top_leftY_cloud - 10, length_cloud)
    draw_cloud(canvas, top_leftX_cloud + 500,
               top_leftY_cloud - 5, length_cloud)
    draw_mountain(canvas, 200, 75, 100)
    draw_mountain(canvas, 400, 75, 100)
    draw_mountain(canvas, 600, 75, 100)
    draw_mountain(canvas, 100, 50, 100)
    draw_mountain(canvas, 300, 50, 100)
    draw_mountain(canvas, 500, 50, 100)
    draw_mountain(canvas, 700, 50, 100)
    draw_cloud(canvas, top_leftX_cloud, top_leftY_cloud, length_cloud)
    draw_grass(canvas, scene_left, grass_y0, grass_x1, scene_right)
    draw_river_blue(canvas, left_topX, left_topY, long_top, long_bottom)
    draw_river_cyan(canvas, left_topX2, left_topY2, long_top2, long_bottom2)
    draw_river_blue(canvas, river_topX, river_topY, river_top, river_bottom)
    draw_river_cyan(canvas, left_topX2 + 50,
                    left_topY2, long_top2 - 100, long_bottom2 - 200)
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_pine_tree(canvas, tree_center - 50, tree_top3, tree_height3)
    draw_pine_tree(canvas, tree_center - 150, tree_top4, tree_height4)
    draw_pine_tree(canvas, tree_center2, tree_top2, tree_height2)
    draw_pine_tree(canvas, tree_center3, tree_top3, tree_height3)
    draw_pine_tree(canvas, tree_center4, tree_top4, tree_height4)

    # This grid was used just as reference
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 50)


def draw_river_blue(canvas, left_topX, left_topY, long_top, long_bottom):
    '''Creates an specific type of river
    left_topX and left_topY are the x and y locations where the river will starte at the top
    long_top and long_bottom are the lenght of each part of the river at the top and at the bottom
    height_river is defined in this case because it's needed for this specific type of river,
    this function is reusable just for this code.
    width and height are the scene_bottom and scene_right but in this case I decided leave it as it is
    here because we know it.'''
    height_river = 350
    width = 800
    height = 500
    right_topX = long_top + left_topX
    right_topY = left_topY
    right_downX = long_bottom / 2 + width / 2
    right_downY = height
    left_downX = width / 2 - long_bottom / 2
    left_downY = right_downY

    # Draw the blue river
    canvas.create_polygon(left_topX, left_topY, right_topX,
                          right_topY, right_downX, right_downY, left_downX, left_downY, fill='blue')


def draw_river_cyan(canvas, left_topX2, left_topY2, long_top2, long_bottom2):
    '''Creates an specific type of river
    left_topX2 and left_topY2 are the x and y locations where the river will starte at the top
    long_top2 and long_bottom2 are the lenght of each part of the river at the top and at the bottom.
    height_river is defined in this case because it's needed for this specific type of river,
    this function is reusable just for this code.
    width and height are the scene_bottom and scene_right but in this case I decided leave it as it is
    here because we know it.'''
    height_river = 350
    width = 800
    height = 500
    right_topX = long_top2 + left_topX2
    right_topY = left_topY2
    right_downX = long_bottom2 / 2 + width / 2
    right_downY = height
    left_downX = width / 2 - long_bottom2 / 2
    left_downY = right_downY

    # Draw the cyan river
    canvas.create_polygon(left_topX2, left_topY2, right_topX,
                          right_topY, right_downX, right_downY, left_downX, left_downY, fill='cyan')


def draw_grass(canvas, x0, y0, x1, y1):
    ''' Creates plane grass with the given coordenates'''
    canvas.create_rectangle(x0, y0, x1, y1, fill='green')


def draw_sky(canvas, x0, y0, x1, y1):
    '''Creates the sky like violet with the given coordenates'''
    canvas.create_rectangle(x0, y0, x1, y1, fill='#7133FF')


def draw_mountain(canvas, top_x, top_y, size):
    '''Creates a default mountain
    top_x and top_y are the coordenates of it, 
    and the size is the height of it
    '''
    width = size * 2
    left = top_x - width / 2
    right = top_x + width / 2
    bottom = top_y + size

    # Draw the mountain
    canvas.create_polygon(top_x, top_y, right, bottom,
                          left, bottom, fill="grey")


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_cloud(canvas, top_leftX, top_leftY, length):
    '''This funtion draws different clouds,
    the x2 and y2 are the coordenates and the lenght is the lenght of the three circles
    of the cloud'''
    x2 = top_leftX + length
    y2 = top_leftY + length

    # Draw the cloud with three circles
    canvas.create_oval(top_leftX, top_leftY, x2, y2,
                       outline='white', fill='white')
    canvas.create_oval(top_leftX + 30, top_leftY,
                       x2 + 30, y2, outline='white', fill='white')
    canvas.create_oval(top_leftX + 60, top_leftY,
                       x2 + 60, y2, outline='white', fill='white')


def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    '''This function draws a grid on the image as reference if you are lost.
    please active it in line 114'''
    text_horizontal_margin = 20
    text_vertical_margin = 10

    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin,
                           i + text_vertical_margin, text=f'{i}')

    # Draw Vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f'{i}')


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
                            trunk_right, trunk_bottom,
                            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
                          skirt_right, skirt_bottom,
                          skirt_left, skirt_bottom,
                          outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()
