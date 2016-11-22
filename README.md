# Pygame-Defaults
A module for python's pygame to allow easy creation of key elements in object oriented form, as well as some extra functions.

  WIP

Current Functions:
  create_grad(colour1, colour2, (width, height))
    Returns a surface with a gradient between the 2 colours

  draw_round_rect( (x, y, width, height), rad, colour, surface)
    Draws a rounded rectangle at given location with radius in pixels on the corners, on a given surface.

  draw_half_round_rect( (x, y, width, height), rad, colour, surface, top=False)
    Draws a half rounded rectangle at given location with radius in pixels on the top or bottom, on a given surface.

  draw_half_round_rect_sides( (x, y, width, height), rad, colour, surface, left=False)
    Draws a half rounded rectangle at given location with radius in pixels on the top or bottom, on a given surface.

  draw_qu_round_rect((x, y, width, height), rad, colour, surface, corner)
    Draws the rectangle that only has 1 corner rounded at a given location on a given surface, the corner is rounded with the given radius.

  image_create(file_loc, midtop, surface)
    Loads an image file from a specified location, and displays it on a given surface where the top centre of the image is at the co-ordinate given in midtop

  image_create_left(file_loc, (left, top), surface)
    Loads an image file from a specified location, and displays it on a given surface where the top left of the image is displayed in the position specified in the parameters top and left.

  image_create_centre(file_loc, (x, y), surface)
    Loads an image file from a specified location, and displays it on a given surface where the centre of the image is displayed in the position specified in the co-ordinate given.




Example:

button = Button(
