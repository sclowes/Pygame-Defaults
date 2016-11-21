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
    
    
    
  

Example:

button = Button(
