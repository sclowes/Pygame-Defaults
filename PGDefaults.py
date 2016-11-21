import pygame
from sys import exit as leave
from pygame import gfxdraw
# imports pygame and exit so isnt needed in main program

pygame.init() # initializes pygame

FPS_CLOCK = pygame.time.Clock() # creates a framerate clock to limit the frames per second of a program


def create_grad(c1, c2, (width, height)): # creates a gradient surface with 2 colours and width/height
    fst = pygame.surface.Surface((width, height))
    snd = pygame.surface.Surface((width, height))
    fst.fill(c1) # 2 surfaces and gets progressivly less transparent as it is moved up the second surface
    snd.fill(c2)
    for i in range(height/3):
        snd.set_alpha(3)
        fst.blit(snd, (0, i*4))
    return fst


def draw_round_rect((x, y, width, height), rad, colour, surface): # draws a rounded rectangle on screen using 2 rectangles in a + shape and 4 
    pygame.draw.rect(surface, colour, [x + rad, y, width - rad * 2, height])
    pygame.draw.rect(surface, colour, [x, y + rad, width, height - rad * 2])
    pygame.draw.circle(surface, colour, [x + rad, y + rad], rad)
    pygame.draw.circle(surface, colour, [x - rad + width, y + rad], rad)
    pygame.draw.circle(surface, colour, [x + rad, y - rad + height], rad)
    pygame.draw.circle(surface, colour, [x - rad + width, y - rad + height], rad)


def draw_half_round_rect((x, y, width, height), rad, colour, surface, top=False): # draws rectangle that is round that is round on either top or bottom
    if top:
        pygame.draw.rect(surface, colour, [x + rad, y, width - rad * 2, rad])
        pygame.draw.rect(surface, colour, [x, y + rad, width, height - rad])
        pygame.draw.circle(surface, colour, [x + rad, y + rad], rad)
        pygame.draw.circle(surface, colour, [x - rad + width, y + rad], rad)
    else:
        pygame.draw.rect(surface, colour, [x, y, width, height-rad])
        pygame.draw.rect(surface, colour, [x+rad, y + height - rad, width - 2 * rad, rad])
        pygame.draw.circle(surface, colour, [x + rad, y - rad + height], rad)
        pygame.draw.circle(surface, colour, [x - rad + width, y - rad + height], rad)


def draw_half_round_rect_sides((x, y, width, height), rad, colour, surface, left=False): # draws rounded rectangle on left or right sides
    if width < 0:
        width = 0
    if height < 0:
        height = 0
    mask = pygame.surface.Surface((int(width), int(height))) # creates a mask in case of errors it will break the temporary surface
    mask.set_colorkey((255, 0, 0))
    mask.fill((255, 0, 0))
    if left:
        pygame.draw.rect(mask, colour, [rad, 0, width - rad, height])
        pygame.draw.rect(mask, colour, [0, rad, rad, height - rad * 2])
        pygame.draw.circle(mask, colour, [rad, rad], rad)
        pygame.draw.circle(mask, colour, [rad, height - rad], rad)
    else:
        pygame.draw.rect(mask, colour, [width - rad, rad, rad, height - rad * 2])
        pygame.draw.rect(mask, colour, [0, 0, width - rad, height])
        pygame.draw.circle(mask, colour, [width - rad, rad], rad)
        pygame.draw.circle(mask, colour, [width - rad, height - rad], rad)
    surface.blit(mask, (x, y))


def draw_qu_round_rect((x, y, width, height), rad, colour, surface, corner): # draws the rectangle that only has 1 corner rounded
    if corner == 0:
        pygame.draw.rect(surface, colour, [x + rad, y, width - rad, height])
        pygame.draw.rect(surface, colour, [x, y + rad, rad, height - rad])
        pygame.draw.circle(surface, colour, [x + rad, y + rad], rad)
    elif corner == 1:
        pygame.draw.rect(surface, colour, [x + width - rad, y + rad, rad, height - rad])
        pygame.draw.rect(surface, colour, [x, y, width - rad, height])
        pygame.draw.circle(surface, colour, [x + width - rad, y + rad], rad)
    elif corner == 2:
        pygame.draw.rect(surface, colour, [x + rad, y, width - rad, height])
        pygame.draw.rect(surface, colour, [x, y, rad, height - rad])
        pygame.draw.circle(surface, colour, [x + rad, y + height - rad], rad)
    elif corner == 3:
        pygame.draw.rect(surface, colour, [x + width - rad, y, rad, height - rad])
        pygame.draw.rect(surface, colour, [x, y, width - rad, height])
        pygame.draw.circle(surface, colour, [x + width - rad, y + height - rad], rad)


def image_create(file_loc, midtop, surface):
    # loads in a n image from a file and displays it
    im = pygame.image.load(file_loc)
    imrect = im.get_rect() # gets the rectangle it will occupy
    imrect.midtop = midtop # sets mid, top coordinates
    surface.blit(im, imrect)


def image_create_left(file_loc, (left, top), surface): # loads in a file the same as above but places based on the top left coordinate
    im = pygame.image.load(file_loc)
    imrect = im.get_rect()
    imrect.left = left
    imrect.top = top
    surface.blit(im, imrect)


def image_create_centre(file_loc, (x, y), surface): # same as above but from centre coord
    im = pygame.image.load(file_loc)
    imrect = im.get_rect()
    imrect.midtop = [x, int(y-imrect[3]/2)]
    surface.blit(im, imrect)


def image_create_centre_surface(pic_surf, (x, y), surface): # displays an already loaded picture from centre coords coords
    imrect = pic_surf.get_rect()
    imrect.midtop = [x, int(y-imrect[3]/2)]
    surface.blit(pic_surf, imrect)


def image_create_midtop_surface(pic_surf, (x, y), surface): # creates an image from the mid top coords
    imrect = pic_surf.get_rect()
    imrect.midtop = [x, y]
    surface.blit(pic_surf, imrect)


def text_create_mid(text, midtop, font, colour, surface): # creates text from the mid top coords
    display = font.render(text, True, colour)
    rect = display.get_rect()
    rect.midtop = midtop
    surface.blit(display, rect)


def text_create_centre_point(text, (x, y), font, colour, surface): # creates text from a centre coord
    display = font.render(text, True, colour)
    rect = display.get_rect()
    rect[0] = x-rect[2]/2
    rect[1] = y-rect[3]/2
    surface.blit(display, rect)


def text_create_left_centre(text, (left, centre), font, colour, surface): # creates text ffrom left, centre coords
    display = font.render(text, True, colour)
    rect = display.get_rect()
    rect.left = left
    rect.top = centre - rect[3]/2
    surface.blit(display, rect)


def text_create_centre(text, (left, top, width, height), font, colour, surface): # creates text in the centre of a given rectangle
    display = font.render(text, True, colour)
    rect = display.get_rect()
    midx = int(left+0.5*width)
    y = int(top+0.5*height-0.5*rect[3])
    rect.midtop = (midx, y)
    surface.blit(display, rect)


def text_create_left(text, (left, top), font, colour, surface): # creates text from the left centre coords
    display = font.render(text, True, colour)
    rect = display.get_rect()
    rect.left = left
    rect.top = top
    surface.blit(display, rect)


def text_create_bleft(text, (left, bot), font, colour, surface): # creates text from bottom left coords
    display = font.render(text, True, colour)
    rect = display.get_rect()
    rect.left = left
    rect.top = bot-rect[3]
    surface.blit(display, rect)


def text_create_bcentre(text, (centre, bot), font, colour, surface): # creates text based on bottom centre coords
    display = font.render(text, True, colour)
    rect = display.get_rect()
    rect.left = centre - rect[2]/2
    rect.top = bot-rect[3]
    surface.blit(display, rect)


def get_text_width(text, font): # gets the width in px of a string in a font
    display = font.render(text, True, (0, 0, 0))
    rect = display.get_rect()
    return rect[2]


def get_text_height(text, font): # gets the width in px of a string in a font
    display = font.render(text, True, (0, 0, 0))
    rect = display.get_rect()
    return rect[3]


def check_mouse_rect((x, y), rect): # checks if a coord is in a rectangle
    if x >= rect[0]: # is it greater than the rect x val, but smaller than x rect + width?
        if x <= rect[0]+rect[2]:
            # same with y values
            if y >= rect[1]:
                if y <= rect[1] + rect[3]:
                    return True


def check_mouse_round_rect((x, y), rect, radius): # checks if a coord is in a rounded rectangle
    if check_mouse_rect((x, y), [rect[0]+radius, rect[1], rect[2]-radius*2, rect[3]]): # check if the val is in the vertical rect
        return True
    elif check_mouse_rect((x, y), [rect[0], rect[1]+radius, rect[2], rect[3]-radius*2]): # check mouse is in horizontal rect
        return True
    elif check_mouse_circ((x, y), [rect[0]+radius, rect[1]+radius], radius):
        return True # checks the 4 corners
    elif check_mouse_circ((x, y), [rect[0]-radius+rect[2], rect[1]+radius], radius):
        return True
    elif check_mouse_circ((x, y), [rect[0]+radius, rect[1]-radius+rect[3]], radius):
        return True
    elif check_mouse_circ((x, y), [rect[0]-radius+rect[2], rect[1]-radius+rect[3]], radius):
        return True


def check_mouse_circ((x, y), centre, rad): # checks if coord is within a circle
    if ((x-centre[0])**2 + (y-centre[1])**2)**0.5 <= rad:
        return True


def check_mouse_qur_rect((x, y), rect, radius, corner): # checks if the coord is in a quarter rounded rectangle
    if corner == 0:
        if check_mouse_rect((x, y), [rect[0]+radius, rect[1], rect[2]-radius, rect[3]]):
            return True
        elif check_mouse_rect((x, y), [rect[0], rect[1]+radius, rect[2], rect[3]-radius]):
            return True
        elif check_mouse_circ((x, y), [rect[0]+radius, rect[1]+radius], radius):
            return True
    elif corner == 1:
        if check_mouse_rect((x, y), [rect[0], rect[1], rect[2]-radius, rect[3]]):
            return True
        elif check_mouse_rect((x, y), [rect[0], rect[1]+radius, rect[2], rect[3]-radius]):
            return True
        elif check_mouse_circ((x, y), [rect[0]+rect[2]-radius, rect[1]+radius], radius):
            return True
    elif corner == 2:
        if check_mouse_rect((x, y), [rect[0], rect[1], rect[2], rect[3]-radius]):
            return True
        elif check_mouse_rect((x, y), [rect[0]+radius, rect[1], rect[2]-radius, rect[3]]):
            return True
        elif check_mouse_circ((x, y), [rect[0]+radius, rect[1]+rect[3]-radius], radius):
            return True
    elif corner == 3:
        if check_mouse_rect((x, y), [rect[0], rect[1], rect[2]-radius, rect[3]]):
            return True
        elif check_mouse_rect((x, y), [rect[0], rect[1], rect[2], rect[3]-radius]):
            return True
        elif check_mouse_circ((x, y), [rect[0]+rect[2]-radius, rect[1]+rect[3]-radius], radius):
            return True


class ListBox: # List of items that can scroll up and down
    def __init__(self, surface, scene, layername, font, items, colour, boxcolour, radius,(x, y, width, height)): # imports variables
        self.scene = scene # assigns all of the imported variables to self variables to save them. Also links itself to  the scene's commands so it can be controlled from there
        self.surface = surface 
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.font = font
        self.items = items
        self.colour = colour
        self.boxColour = boxcolour
        self.rect = [x, y, width, height]
        self.off = False
        self.offSet = 0
        self.radius = radius
        self.layerSurface.add_layer(layername, self.draw, list([]))
        scene.offButtons[layername] = self.toggle

    def draw(self): # draw function that draws the textbox and text
        if self.off:
            return False
        lines = self.items # draws each item on a new line from list
        totalheight = 0
        for i in lines: # for every line it gets the text height and adds the gap of 2 px between each to get total height of text
            totalheight += get_text_height(i, self.font) + 2
        x, y = self.surface.get_width(), self.surface.get_height() # gets width of the surface
        surface1 = pygame.surface.Surface((x, y)) # creates 2 surfaces
        surface2 = pygame.surface.Surface((x, y))
        surface2.fill((0, 255, 0)) # fills one green
        draw_round_rect(self.rect, self.radius, self.boxColour, surface1)
        draw_round_rect(self.rect, self.radius, self.boxColour, surface2) # draws a rectangle onto both surfaces
        height = 0
        lines = lines[::-1] # reverses lines
        for i in lines: # for each line, then creates the text on the left hand side of the box
            text_create_left(i, (self.rect[0]+2, self.rect[1]+height-self.offSet), self.font,
                              self.colour,
                              surface1)
            height += get_text_height(i, self.font) + 2 # increases the the height of the text
        self.height = height # stes the original height
        surface2.set_colorkey(self.boxColour) # sets the transparent colour
        surface1.blit(surface2, (0, 0)) # places the surface ontop so that any text that goes over the edge of the box is cut off
        surface2 = self.surface.copy() 
        surface1.set_colorkey((0, 255, 0))
        surface2.blit(surface1, (0, 0))
        self.surface.blit(surface2, (0, 0)) # places it onto the main surface

    def check(self, event=None): # checks for inputs
        if self.off:
            return False
        if event is None:
            return False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN: # if the mousewheel is being used then offset the text so it looks like it is scrolling up and down
                if event.button == 5:
                    if self.offSet + 4 > self.height - self.rect[3]:
                        pass
                    else:
                        self.offSet += 4
                elif event.button == 4:
                    if self.offSet - 4 < 0:
                        pass
                    else:
                        self.offSet -= 4
        return False

    def toggle(self, onoff=None): # enables/disables the object
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class PercentBar: # shows a bar used for loading/health bars etc
    def __init__(self, surface, scene, layername, font, text_colour, bar_colour, back_colour, border_colour, radius,
                 (x, y, width, height), max_val, init_percent=100):
        self.scene = scene # Assigns all imported variables to self variables and links the scene
        self.surface = surface
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.font = font
        self.text_colour = text_colour
        self.bar_colour = bar_colour
        self.back_colour = back_colour
        self.border_colour = border_colour
        self.radius = radius
        self.rect = [x, y, width, height]
        self.layerSurface.add_layer(layername, self.draw, list([]))
        self.off = False
        self.max_val = max_val
        self.val = int(init_percent*(float(self.max_val)/100))
        scene.offButtons[layername] = self.toggle

    def draw(self): # draws the bar and text
        draw_round_rect(self.rect, self.radius, self.border_colour, self.surface) # draws a round rect for the background
        draw_round_rect((int(self.rect[0]+self.rect[3]*0.05), int(self.rect[1]+self.rect[3]*0.05), # draws a round rect for the missing health sections
                         int(self.rect[2]-self.rect[3]*0.1), int(self.rect[3]*0.9)),
                        int(self.radius*0.8), self.back_colour, self.surface)
        if self.val == self.max_val: # if the val is at maximum then a rounded rectangle is needed
            draw_round_rect((int(self.rect[0]+self.rect[3]*0.05), int(self.rect[1]+self.rect[3]*0.05),
                             int(self.rect[2]-self.rect[3]*0.1), int(self.rect[3]*0.9)),
                            int(self.radius*0.8), self.bar_colour, self.surface)
        else: # else draw a half rounded rectangle
            draw_half_round_rect_sides((int(self.rect[0]+self.rect[3]*0.05), int(self.rect[1]+self.rect[3]*0.05),
                                        int(((self.rect[2]-self.rect[3]*0.1)/100.0)*(float(self.val)/self.max_val)*100), int(self.rect[3]*0.9)),
                                       int(self.radius*0.8), self.bar_colour, self.surface, True)
        text_create_centre_point(str(self.val)+"/"+str(self.max_val),
                                 (self.rect[0]+self.rect[2]/2,self.rect[1]+self.rect[3]/2),
                                 self.font, self.text_colour, self.surface) # create text showing number values

    def check(self, percent=False): # returns current value
        if not percent:
            return self.val
        else:
            return int((float(self.val)/self.max_val)*100)

    def set_val(self, val, percent=False): # sets a value whether that is percent or true val
        if not percent:
            self.val = val
        else:
            self.val = int((val/100.0)*self.max_val)

    def increase_val(self, val, percent=False): # increases val by a cetrain amount or percent
        if not percent:
            self.val += val
        else:
            self.val += int((val/100.0)*self.max_val)
        if self.val < 0:
            self.val = 0
        elif self.val > self.max_val:
            self.val = self.max_val

    def decrease_val(self, val, percent=False): # decreases val by a certain amount or percent
        if not percent:
            self.val -= val
        else:
            self.val -= int((val/100.0)*self.max_val)
        if self.val < 0:
            self.val = 0
        elif self.val > self.max_val:
            self.val = self.max_val

    def toggle(self, onoff=None): # toggles it on or off
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class MultiChoice: # multiple choice object
    def __init__(self, surface, scene, layername, font, values, text_colour, back_colour,
                 highlight_colour, radius, (x, y, width, height), title):
        self.scene = scene # assigns all passed variables and links to the scene
        self.surface = surface
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.font = font
        self.values = values
        self.text_colour = text_colour
        self.back_colour = back_colour
        self.highlight_colour = highlight_colour
        self.radius = radius
        self.rect = [x, y, width, height]
        self.title = title
        self.choice = -1
        self.offsets = [0, 0, 0, 0, 0]
        self.heights = [0, 0, 0, 0, 0]
        self.layerSurface.add_layer(layername, self.draw, list([]))
        self.off = False
        scene.offButtons[layername] = self.toggle
        self.lock = False
        self.diff = 0

    def draw(self): # draw function
        if self.off:
            return 0 # if off return 0
        draw_round_rect(self.rect, self.radius, self.back_colour, self.surface) # draws a rounded rectangle
        self.diff = self.text_draw([self.rect[0], self.rect[1], self.rect[2], self.rect[3]/4], self.title, 0) # the height the title needs and also draws the title 
        if self.choice != -1: # if the user has selected a choice then highlight the chosen answer with a lighter colour
            if self.choice == 0:
                pygame.draw.rect(self.surface, self.highlight_colour,
                                 [self.rect[0], self.rect[1] + self.diff + self.rect[3]/4,
                                  self.rect[2]/2, 3*self.rect[3]/8 - self.diff/2])
            elif self.choice == 1:
                pygame.draw.rect(self.surface, self.highlight_colour,
                                 [self.rect[0] + self.rect[2]/2, self.rect[1] + self.diff + self.rect[3]/4,
                                  self.rect[2]/2, 3*self.rect[3]/8 - self.diff/2])
            elif self.choice == 2:
                draw_qu_round_rect([self.rect[0], self.rect[1] + self.diff/2 + 5*self.rect[3]/8,
                                    self.rect[2]/2, 3*self.rect[3]/8+1 - self.diff/2],
                                   self.radius, self.highlight_colour, self.surface, 2)
            elif self.choice == 3:
                draw_qu_round_rect([self.rect[0] + self.rect[2]/2, self.rect[1] + self.diff/2 + 5*self.rect[3]/8,
                                    self.rect[2]/2, 3*self.rect[3]/8+1 - self.diff/2],
                                   self.radius, self.highlight_colour, self.surface, 3)

        self.text_draw([self.rect[0], self.rect[1] + self.diff + self.rect[3]/4, self.rect[2]/2, 3*self.rect[3]/8 - self.diff/2], self.values[0], 1) # draws on all of the answers into their position

        self.text_draw([self.rect[0] + self.rect[2]/2, self.rect[1] + self.diff + self.rect[3]/4, self.rect[2]/2, 3*self.rect[3]/8 - self.diff/2], self.values[1], 2) # ""

        self.text_draw([self.rect[0], self.rect[1] + self.diff/2 + 5*self.rect[3]/8, self.rect[2]/2, 3*self.rect[3]/8+1 - self.diff/2], self.values[2], 3) # ""

        self.text_draw([self.rect[0] + self.rect[2]/2, self.rect[1] + self.diff/2 + 5*self.rect[3]/8, self.rect[2]/2, 3*self.rect[3]/8+1 - self.diff/2], self.values[3], 4) # ""
        # draws the lines seporating the answers from each other and the title
        pygame.draw.aaline(self.surface, self.text_colour,
                                       (self.rect[0], self.rect[1] + self.diff + self.rect[3]/4),
                                       (self.rect[0] + self.rect[2], self.rect[1] + self.diff + self.rect[3]/4))
        pygame.draw.aaline(self.surface, self.text_colour,
                                       (self.rect[0] + self.rect[2]/2, self.rect[1] + self.diff + self.rect[3]/4),
                                       (self.rect[0] + self.rect[2]/2,
                                        self.rect[1] + self.diff + self.rect[3] - self.diff))
        pygame.draw.aaline(self.surface, self.text_colour,
                                       (self.rect[0], self.rect[1] + self.diff/2 + 5*self.rect[3]/8),
                                       (self.rect[0] + self.rect[2], self.rect[1] + self.diff/2 + 5*self.rect[3]/8))

    def text_draw(self, rect, text, no): # drawing the text so that it starets newlines
        orig = rect[3]
        lines = []
        current = text
        excess = ""
        width = get_text_width(text, self.font) # gets the width of the font
        lines = self.recurse_line(width, lines, current, excess, rect) # calls the recurse lines function
        totalheight = 0
        for i in lines: # gets total height
            totalheight += get_text_height(i, self.font) + 2
        if totalheight <= rect[3]:
            height = 2
            for i in lines: # adds all the lines in the text and draws in the centre
                text_create_centre_point(i, (rect[0]+rect[2]/2, rect[1]+height+rect[3]/2), self.font, self.text_colour, self.surface)
                height += get_text_height(i, self.font) + 2
        else: # if the height of all the lines is larger than the box
            if no -1 == self.choice and self.choice is not -1:
                colour = self.highlight_colour # sets colour of the beckground to what it is in the main draw
            else:
                colour = self.back_colour
            x, y = self.surface.get_width(), self.surface.get_height() # creates 2 new surfaces 
            total_height = (get_text_height(text, self.font)+2) * len(lines)
            rect[3] = total_height+2
            surface1 = pygame.surface.Surface((x, y))
            surface2 = pygame.surface.Surface((x, y))
            surface2.fill(colour)
            surface1.fill(colour)
            draw_round_rect(rect, self.radius, (255, 0, 0), surface2) # draws on the rect that will be transparent so text can be seen under it
            height = 2
            lines = lines[::-1]
            for i in lines:
                text_create_bcentre(i, (rect[0]+rect[2]/2, rect[1]+rect[3]-height+self.offsets[no]),
                                    self.font, self.text_colour, surface1)
                height += get_text_height(i, self.font) + 2 # writes on the text, allowing for it to go over the borders
            self.heights[no] = height
            surface2.set_colorkey((255, 0, 0))
            surface1.blit(surface2, (0, 0))

            # surface2 = self.surface.copy()
            surface1.set_colorkey(colour)
            # surface2.blit(surface1, (0, 0))
            self.surface.blit(surface1, (0, 0)) # pastes on the surfaces so that only the text within the area can be seen, to see the rest the user can scroll
        return rect[3] - orig

    def recurse_line(self, width, lines, current, excess, rect): # splits a string into lines based on the width of a rectangle
        if width < rect[2]-4: # if the width is less than rectangle
            lines.append(current) # adds the current string to the line
            if excess != "": # if there is remaining string then gets its width and recursivly calls itself
                width = get_text_width(excess, self.font)
                lines = self.recurse_line(width, lines, excess, "", rect)
                return lines # after it returns the lines
            return lines
        else: # if the current string is too long it splits it at the next space and tries again
            current = current[::-1]
            pos, current = current.split(" ", 1)
            switch = pos + " "
            switch = switch[::-1]
            current = current[::-1]
            excess = switch + excess
            width = get_text_width(current, self.font)
            lines = self.recurse_line(width, lines, current, excess, rect)
            return lines

    def check(self, event=None): # checks any inputs
        if self.off:
            return False
        mouse_click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        check = False
        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN: # if an event has been passed it checks every answer to see where the user's mouse is and remembers it
                if check_mouse_round_rect(mouse_pos,[self.rect[0], self.rect[1], self.rect[2],
                                                     self.rect[3]/4+self.diff],  self.radius):
                    check = True
                    checkval = 0
                if check_mouse_round_rect(mouse_pos,[self.rect[0], self.rect[1] + self.diff + self.rect[3]/4,
                                                     self.rect[2]/2, 3*self.rect[3]/8 - self.diff/2], self.radius):
                    check = True
                    checkval = 1
                if check_mouse_round_rect(mouse_pos,[self.rect[0] + self.rect[2]/2,
                                                     self.rect[1] + self.diff + self.rect[3]/4,
                                                     self.rect[2]/2, 3*self.rect[3]/8 - self.diff/2], self.radius):
                    check = True
                    checkval = 2
                if check_mouse_round_rect(mouse_pos,[self.rect[0], self.rect[1] + self.diff/2 + 5*self.rect[3]/8,
                                                     self.rect[2]/2, 3*self.rect[3]/8+1 - self.diff/2], self.radius):
                    check = True
                    checkval = 3
                if check_mouse_round_rect(mouse_pos,
                                          [self.rect[0] + self.rect[2]/2, self.rect[1] + self.diff/2 + 5*self.rect[3]/8,
                                           self.rect[2]/2, 3*self.rect[3]/8+1 - self.diff/2], self.radius):
                    check = True
                    checkval = 4
                if check == True: # if the mouse was on a button then it offsets the answer so that it appears to be scrolling
                    if event.button == 4:
                        if self.offsets[checkval] + 4 > self.heights[checkval] - self.rect[3]:
                            pass
                        else:
                            self.offsets[checkval] += 4
                    elif event.button == 5:
                        if self.offsets[checkval] - 4 < 0:
                            pass
                        else:
                            self.offsets[checkval] -= 4
        else:
            if mouse_click[0]: # if an event is not passed it checks to see if any thing has been clicked
                if not self.lock: # lock to stop multiclicking without lifting the mouse
                    self.lock = True
                    # checks to see if any of the answers have been pressed it pick the right choice depending on which answer was pressed
                    if check_mouse_rect(mouse_pos, [self.rect[0], self.rect[1] + self.diff + self.rect[3]/4,
                                                    self.rect[2]/2, 3*self.rect[3]/8 - self.diff/2]): 
                        self.choice = 0
                    elif check_mouse_rect(mouse_pos, [self.rect[0] + self.rect[2]/2,
                                                      self.rect[1] + self.diff + self.rect[3]/4, self.rect[2]/2,
                                                      3*self.rect[3]/8 - self.diff/2]):
                        self.choice = 1
                    elif check_mouse_qur_rect(mouse_pos, [self.rect[0], self.rect[1] + self.diff/2 + 5*self.rect[3]/8,
                                                          self.rect[2]/2,
                                                          3*self.rect[3]/8+1 - self.diff/2], self.radius, 2):
                        self.choice = 2
                    elif check_mouse_qur_rect(mouse_pos, [self.rect[0] + self.rect[2]/2,
                                                          self.rect[1] + self.diff/2 + 5*self.rect[3]/8, self.rect[2]/2,
                                                          3*self.rect[3]/8+1 - self.diff/2], self.radius, 3):
                        self.choice = 3
            else:
                self.lock = False

    def toggle(self, onoff=None): # enables/disables the object
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class DropBox: # drop down box
    def __init__(self, surface, scene, layername, font, values, text_colour, back_colour, button_colour,
                 radius, (x, y, width, height), start_message="", up=False):
        self.scene = scene # assigns passed variables and links to the scene
        self.surface = surface
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.font = font
        self.values = values
        self.text_colour = text_colour
        self.back_colour = back_colour
        self.button_colour = button_colour
        self.radius = radius
        self.rect = [x, y, width, height]
        self.up = up
        self.open = False
        self.lock = False
        self.clicked = False
        self.choice = 0
        self.start_message = start_message
        self.layerSurface.add_layer(layername, self.draw, list([]))
        self.off = False
        scene.offButtons[layername] = self.toggle

    def draw(self): # draws the dropdown box
        if self.open and self.values != []: # if the drop has ben opened
            if self.up: # if the drop down box drops upwards
                draw_half_round_rect(self.rect, self.radius, self.back_colour, self.surface) # draws the bottom as a rect that is flat ontop
                for i in range(len(self.values)-1): # for every item in the list of items apart from the last, it draws a rectangle and places the option text within it
                    pygame.draw.rect(self.surface, self.back_colour, [self.rect[0], self.rect[1] - self.rect[3]*(i+1),
                                                                      self.rect[2], self.rect[3]])
                    text_create_left_centre(self.values[i], (self.rect[0] + self.radius,
                                                             self.rect[1] - self.rect[3]*(i+1) + self.rect[3]/2),
                                            self.font, self.text_colour, self.surface)
                draw_half_round_rect((self.rect[0], # the last is created only half round, so that the entire stack looks like a rounded rectangle
                                      self.rect[1] - self.rect[3] * len(self.values),
                                      self.rect[2],
                                      self.rect[3]), self.radius, self.back_colour, self.surface, True)
                text_create_left_centre(self.values[len(self.values)-1],
                                        (self.rect[0] + self.radius,
                                         self.rect[1] - self.rect[3]*(len(self.values)) + self.rect[3]/2),
                                        self.font, self.text_colour, self.surface)
                # if there is a start message and the dropdown box hasnt already seleced an asnswer previously
                if self.start_message and not self.clicked:
                    text_create_left_centre(self.start_message,
                                            (self.rect[0] + self.radius,
                                             self.rect[1] + self.rect[3]/2),
                                            self.font, self.text_colour, self.surface) # adds the start message to the bottom
                else: # else it adds the current choice to the bottom of the box
                    text_create_left_centre(self.values[self.choice],
                                            (self.rect[0] + self.radius,
                                             self.rect[1] + self.rect[3]/2),
                                            self.font, self.text_colour, self.surface)
                for i in range(len(self.values)-1): # draws lines between each choice
                    pygame.draw.aaline(self.surface, self.button_colour,
                                       (self.rect[0], self.rect[1] - self.rect[3]*i),
                                       (self.rect[0] + self.rect[2], self.rect[1] - self.rect[3]*i))
                pygame.draw.aaline(self.surface, self.button_colour,
                                   (self.rect[0], self.rect[1] - self.rect[3] * (len(self.values)-1)),
                                   (self.rect[0] + self.rect[2], self.rect[1] - self.rect[3] * (len(self.values)-1)))
                # draws the close arrow in a quarter round rectangle in the corner
                draw_qu_round_rect((self.rect[0] + self.rect[2] - self.rect[3], self.rect[1], self.rect[3],
                                    self.rect[3]), self.radius, self.button_colour, self.surface, 3)
                text_create_centre_point("v",
                                         (self.rect[0] + self.rect[2] - self.rect[3]/2, self.rect[1] + self.rect[3]/2),
                                         self.font, self.text_colour, self.surface)
            else: # does the exat same as above but reverses the direction, with each item going below each other
                draw_half_round_rect(self.rect, self.radius, self.back_colour, self.surface, True)
                for i in range(len(self.values)-1):
                    pygame.draw.rect(self.surface, self.back_colour, [self.rect[0], self.rect[1] + self.rect[3]*(i+1),
                                                                      self.rect[2], self.rect[3]])
                    text_create_left_centre(self.values[i], (self.rect[0] + self.radius,
                                                             self.rect[1] + self.rect[3]*(i+1) + self.rect[3]/2),
                                            self.font, self.text_colour, self.surface)
                draw_half_round_rect((self.rect[0],
                                      self.rect[1] + self.rect[3] * len(self.values),
                                      self.rect[2],
                                      self.rect[3]), self.radius, self.back_colour, self.surface)
                text_create_left_centre(self.values[len(self.values)-1],
                                        (self.rect[0] + self.radius,
                                         self.rect[1] + self.rect[3]*(len(self.values)) + self.rect[3]/2),
                                        self.font, self.text_colour, self.surface)
                if self.start_message and not self.clicked:
                    text_create_left_centre(self.start_message,
                                            (self.rect[0] + self.radius,
                                             self.rect[1] + self.rect[3]/2),
                                            self.font, self.text_colour, self.surface)
                else:
                    text_create_left_centre(self.values[self.choice],
                                            (self.rect[0] + self.radius,
                                             self.rect[1] + self.rect[3]/2),
                                            self.font, self.text_colour, self.surface)
                for i in range(len(self.values)-1):
                    pygame.draw.aaline(self.surface, self.button_colour,
                                       (self.rect[0], self.rect[1] + self.rect[3]*(i+1)),
                                       (self.rect[0] + self.rect[2], self.rect[1] + self.rect[3]*(i+1)))
                pygame.draw.aaline(self.surface, self.button_colour,
                                   (self.rect[0], self.rect[1] + self.rect[3] * len(self.values)),
                                   (self.rect[0] + self.rect[2], self.rect[1] + self.rect[3] * len(self.values)))

                draw_qu_round_rect((self.rect[0] + self.rect[2] - self.rect[3], self.rect[1], self.rect[3],
                                    self.rect[3]), self.radius, self.button_colour, self.surface, 1)
                text_create_centre_point("^",
                                         (self.rect[0] + self.rect[2] - self.rect[3]/2, self.rect[1] + self.rect[3]/2),
                                         self.font, self.text_colour, self.surface)
        else: # if the box is closed
            draw_round_rect(self.rect, self.radius, self.back_colour, self.surface) # draws a round rect
            draw_half_round_rect_sides((self.rect[0] + self.rect[2] - self.rect[3], self.rect[1], self.rect[3],
                                        self.rect[3]), self.radius, self.button_colour, self.surface)
            # draws a half round rect to hold the choice text
            if self.up: # if it opens upwards it adds an up arrow, down arrow for down
                text_create_centre_point("^",
                                         (self.rect[0] + self.rect[2] - self.rect[3]/2, self.rect[1] + self.rect[3]/2),
                                         self.font, self.text_colour, self.surface)
            else:
                text_create_centre_point("v",
                                         (self.rect[0] + self.rect[2] - self.rect[3]/2, self.rect[1] + self.rect[3]/2),
                                         self.font, self.text_colour, self.surface)
            # adds the start message if there is one and a value hasnt been chosen
            if (self.start_message and not self.clicked) or self.values == []:
                    text_create_left_centre(self.start_message,
                                            (self.rect[0] + self.radius,
                                             self.rect[1] + self.rect[3]/2),
                                            self.font, self.text_colour, self.surface)
            else: # else it adds the choice to the bottom
                text_create_left_centre(self.values[self.choice],
                                        (self.rect[0] + self.radius,
                                         self.rect[1] + self.rect[3]/2),
                                        self.font, self.text_colour, self.surface)

    def check(self): # checks to see if it has been used
        mouse_click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_click[0]:
            if self.open:
                if not self.lock:
                    if self.up:#if the item opens upwards
                        for i in range(len(self.values)-1):
                            if check_mouse_rect(mouse_pos,
                                                [self.rect[0], self.rect[1] - self.rect[3]*(i+1), self.rect[2],
                                                 self.rect[3]]):
                                self.choice = i
                                self.clicked = True # checks each item in the list to see if its been pressed
                        if check_mouse_round_rect(mouse_pos, (self.rect[0],
                                                              self.rect[1] - self.rect[3] * len(self.values),
                                                              self.rect[2],
                                                              self.radius*2), self.radius) or \
                                check_mouse_rect(mouse_pos, (self.rect[0],
                                                             self.rect[1] - self.rect[3] * len(self.values) +
                                                             self.radius,
                                                             self.rect[2],
                                                             self.rect[3] - self.radius)):
                            # checks last box ontop
                            self.choice = len(self.values)-1
                            self.clicked = True
                    else: # does the same but if the list opens downwards
                        for i in range(len(self.values)-1):
                            if check_mouse_rect(mouse_pos,
                                                [self.rect[0], self.rect[1] + self.rect[3]*(i+1), self.rect[2],
                                                 self.rect[3]]):
                                self.choice = i
                                self.clicked = True
                        if check_mouse_round_rect(mouse_pos, (self.rect[0],
                                                              self.rect[1] + self.rect[3] * (len(self.values)+1) -
                                                              self.radius*2,
                                                              self.rect[2],
                                                              self.radius*2), self.radius) or \
                                check_mouse_rect(mouse_pos, (self.rect[0],
                                                             self.rect[1] + self.rect[3] * len(self.values),
                                                             self.rect[2],
                                                             self.rect[3] - self.radius)):
                            self.choice = len(self.values)-1
                            self.clicked = True

                    self.open = False
                    # when an answer has been selected then it closes the box
            else: # if the box isnt open it checks to see if it can open
                if check_mouse_round_rect(mouse_pos, self.rect, self.radius):
                    if not self.lock:
                        if self.values:
                            self.open = True
            self.lock = True
        else:
            self.lock = False

    def toggle(self, onoff=None): # enables/disables the object
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class Text: # displays text on the screen
    def __init__(self, surface, scene, layername, font, text, colour, (x, y), usemid, usecentre = False):
        self.scene = scene # assigns passed variables and links to the scene
        self.surface = surface
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.font = font
        self.text = text
        self.colour = colour
        self.coords = [x, y]
        self.useMid = usemid
        self.useCentre = usecentre
        self.layerSurface.add_layer(layername, self.draw, list([]))
        self.off = False
        scene.offButtons[layername] = self.toggle

    def draw(self): # draw function
        if self.off:
            return False
        if self.useCentre: # if the text uses the centre poin then creates the text at the centre
            text_create_centre_point(self.text, self.coords, self.font, self.colour, self.surface)
        elif self.useMid: # if it uses mid, top coords then it uses them instead
            text_create_mid(self.text, self.coords, self.font, self.colour, self.surface)
        else: # else uses left top coords
            text_create_left(self.text, self.coords, self.font, self.colour, self.surface)

    def check(self):
        return False # doesnt need to be checked but in there so that any looping wont throw an error

    def toggle(self, onoff=None):
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class TextBox: # user input textbox class
    def __init__(self, surface, scene, layername, font, text, colour, boxcolour,
                 selectcolour, (x, y, width, height), charlimit=None):
        self.scene = scene # saves passed variables and links scene
        self.surface = surface
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.font = font
        self.text = text
        self.colour = colour
        self.boxColour = boxcolour
        self.rect = [x, y, width, height]
        self.innerRect = [x+2, y+2, width-4, height-4]
        self.off = False
        self.typing = False
        self.lock = False
        self.selectColour = selectcolour
        self.offSet = 0
        self.height = 0
        self.charLimit = charlimit
        self.radius = int(((self.rect[2]+self.rect[3])/2)*0.05)
        self.layerSurface.add_layer(layername, self.draw, list([]))
        scene.offButtons[layername] = self.toggle

    def draw(self): # draw function
    #---------------------------------------------------------------
        # Exactly the same function as the text_draw from the multichoice, for explaination visit there
    #---------------------------------------------------------------
        if self.off:
            return False
        lines = []
        current = self.text
        excess = ""
        width = get_text_width(self.text, self.font)
        lines = self.recurse_line(width, lines, current, excess)
        totalheight = 0
        for i in lines:
            totalheight += get_text_height(i, self.font) + 2
        if totalheight <= self.rect[3]:
            if self.typing:
                draw_round_rect(self.rect, self.radius, self.selectColour, self.surface)
                draw_round_rect(self.innerRect, self.radius, self.boxColour, self.surface)
            else:
                draw_round_rect(self.rect, self.radius, self.boxColour, self.surface)
            height = 2
            for i in lines:
                text_create_left(i, (self.rect[0]+2, self.rect[1]+height), self.font, self.colour, self.surface)
                height += get_text_height(i, self.font) + 2
        else:
            x, y = self.surface.get_width(), self.surface.get_height()
            surface1 = pygame.surface.Surface((x, y))
            surface2 = pygame.surface.Surface((x, y))
            surface2.fill((0, 255, 0))
            if self.typing:
                draw_round_rect(self.rect, self.radius, self.selectColour, surface1)
                draw_round_rect(self.innerRect, self.radius, self.boxColour, surface1)
            else:
                draw_round_rect(self.rect, self.radius, self.boxColour, surface1)
            draw_round_rect(self.rect, self.radius, self.boxColour, surface2)
            height = 2
            lines = lines[::-1]
            for i in lines:
                text_create_bleft(i, (self.rect[0]+2, self.rect[1]+self.rect[3]-height+self.offSet), self.font,
                                  self.colour,
                                  surface1)
                height += get_text_height(i, self.font) + 2
            self.height = height
            surface2.set_colorkey(self.boxColour)
            surface1.blit(surface2, (0, 0))

            surface2 = self.surface.copy()
            surface1.set_colorkey((0, 255, 0))
            surface2.blit(surface1, (0, 0))
            self.surface.blit(surface2, (0, 0))

    def recurse_line(self, width, lines, current, excess):
        # Same function as the one in multichoice but wit added error handling
        if width < self.rect[2]-4:
            lines.append(current)
            if excess != "":
                width = get_text_width(excess, self.font)
                lines = self.recurse_line(width, lines, excess, "")
                return lines
            return lines
        else:
            current = current[::-1]
            try: # as the text box can be user for long user names, if it doesnt have a space in it, then it will take the end letter off instead
                pos, current = current.split(" ", 1)
                switch = pos + " "
            except ValueError:
                switch = ""
                while get_text_width(current, self.font) >= self.rect[2]-4:
                    switch += current[0]
                    current = current[1:]

            switch = switch[::-1]
            current = current[::-1]
            excess = switch + excess
            width = get_text_width(current, self.font)
            lines = self.recurse_line(width, lines, current, excess)
            return lines

    def check(self, event=None): # function to scheck and interact with the  user
        if self.off:
            return False
        if event is None: # checking for mouse input
            mousepos = pygame.mouse.get_pos()
            mouseclick = pygame.mouse.get_pressed() # gets button press status and position
            if mouseclick[0]:
                if not self.lock:
                    if check_mouse_round_rect(mousepos, self.rect, self.radius) and mouseclick[0]:
                        self.typing = True # if the user is clicking and inside the box then the user is typing
                    else:
                        self.typing = False # if the user has clicked somewhere else they are no longer typing
                    self.lock = True
            else:
                self.lock = False
        else:
            if not self.typing: # checking keyboard inputs and scroll wheel
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # returns text if enter is pressed
                    return self.text
                elif event.key != pygame.K_BACKSPACE and event.key != 9 and event.key != 27:# if the event.key isnt backspace or a special button (eg ctrl)
                    if event.key < 256: # 
                        if self.charLimit is None or len(self.text) < self.charLimit:
                            self.text += event.unicode.encode('ascii', 'replace') # inupts the character key and converts it to ascii format before adding it to the text in  the box
                elif event.key == pygame.K_BACKSPACE: # if the key was backspace then it deletes the last character
                    self.text = self.text[:len(self.text)-1]
            elif event.type == pygame.MOUSEBUTTONDOWN: # if a button has been pressed and that button is a mousewheel, offset the text so it appears to scroll
                if event.button == 4:
                    if self.offSet + 4 > self.height - self.rect[3]:
                        pass
                    else:
                        self.offSet += 4
                elif event.button == 5:
                    if self.offSet - 4 < 0:
                        pass
                    else:
                        self.offSet -= 4
        return False

    def toggle(self, onoff=None): # enables/disables the object
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class Radio: # radio buttons
    def __init__(self, surface, scene, layername, positions, radius):
        self.scene = scene # initializes all of the variables based on what was passed
        self.surface = surface
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.positions = positions
        self.radius = radius
        self.choice = 0
        self.lock = False
        self.layerSurface.add_layer(layername, self.draw, list([]))
        self.off = False
        scene.offButtons[layername] = self.toggle

    def draw(self): # draw function
        if self.off:
            return False
        for i in self.positions: # draws an aa outline then fills the circle at each location specified
            gfxdraw.aacircle(self.surface, i[0], i[1], self.radius, (255, 255, 255))
            gfxdraw.filled_circle(self.surface, i[0], i[1], self.radius, (255, 255, 255))
        gfxdraw.aacircle(self.surface, self.positions[self.choice][0], self.positions[self.choice][1],
                         int(self.radius*0.7), (0, 0, 0))
        gfxdraw.filled_circle(self.surface, self.positions[self.choice][0], self.positions[self.choice][1],
                              int(self.radius*0.7), (0, 0, 0))
        # draws a smaller aa circle then fills it in black ontop of the choice that has been chosen

    def check(self): # check function
        if self.off:
            return False
        mousepos = pygame.mouse.get_pos()
        count = 0
        for i in self.positions:
            if check_mouse_circ(mousepos, i, self.radius):
                if pygame.mouse.get_pressed()[0] and not self.lock:
                    self.choice = count
                    # checks each circle to see if it has been clicked on, if so it sets the user's choice to that circle
            count += 1
        if not pygame.mouse.get_pressed()[0]:
            self.lock = False
        else:
            self.lock = True
            #locking so that when keepiong mouse held down and passing over the button it doesnt press

    def toggle(self, onoff=None):
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class Button: # button class
    def __init__(self, surface, scene, layername, rect, colour, hovercolour, text, font, radius, fontcolour):
        self.scene = scene # creating variables from passed and linking it to the scene functions
        self.rect = rect
        self.colour = colour
        self.text = text
        self.font = font
        self.radius = radius
        self.surface = surface
        self.layerSurface = scene.layerSurface
        self.layerName = layername
        self.hoverColor = hovercolour
        self.fontColor = fontcolour
        self.lock = False
        self.layerSurface.add_layer(layername, self.draw, list([]))
        self.off = False
        scene.offButtons[layername] = self.toggle

    def draw(self, colour=None): # draws the button
        if self.off:
            return False
        if colour is None: # can draw with a specific colour
            colour = self.colour
        # draws the rounded rect button
        draw_round_rect(self.rect, self.radius, colour, self.surface)
        text_create_centre(self.text, self.rect, self.font, self.fontColor, self.surface) # creates the text in the centre of the button

    def check(self): # check function for the button
        if self.off:
            return False
        mouse = pygame.mouse.get_pos()
        clicks = pygame.mouse.get_pressed()
        checkval = False
        if clicks[0] and not self.lock: # checks if mouse is in the buttons round rect and has been pressed
            if check_mouse_round_rect(mouse, self.rect, radius):
                self.layerSurface.change_para(self.layerName, [self.hoverColor]) # changes colour of button when pressed
                self.lock = True
                return True # returns true
            else:
                self.lock = True
        if not clicks[0]:
            self.layerSurface.change_para(self.layerName, list([]))
            self.lock = False # changes draw parameters back when let go

    def toggle(self, onoff=None): # enables/disables object
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff

class LayerSurface: # Main layersurface object to be used in scenes
    def __init__(self):
        self.layers = {}
        self.off = False # ads a layers dictionary and turns itself off by default

    def add_layer(self, layername, drawfunction, parameters):
        self.layers[layername] = [len(self.layers), drawfunction, parameters] # adds a draw function and saves it in a layer in the dictionary with a draw order

    def delete_layer(self, layername): # deletes the item and moves all layers above it down one
        number = self.layers[layername][0]
        del self.layers[layername]
        for i in self.layers:
            if self.layers[i][0] > number:
                self.layers[i][0] -= 1

    def reorder_layer(self, layername, pos): # re orders a layer, moving it up or down in the draw order
        if pos == self.layers[layername][0]:
            pass # if it is already in the position do nothing
        elif pos < self.layers[layername][0]: # if it is underneith it then move it and any item that was between it's old position and new got moved up one
            for i in self.layers:
                if self.layers[i][0] >= pos:
                    if self.layers[i][0] < self.layers[layername][0]:
                        self.layers[i][0] += 1
        else: # else it moved and between its old and new positions down noe
            for i in self.layers:
                if self.layers[i][0] >= self.layers[layername][0]:
                    if self.layers[i][0] <= pos:
                        self.layers[i][0] -= 1
        self.layers[layername][0] = pos

    def change_para(self, layername, parameters):
        self.layers[layername][2] = parameters # changes the saved parameters to draw something

    def change_func(self, layername, function):
        self.layers[layername][1] = function # changes the draw function but keeps the parameters

    def draw(self, flip=False, goto=None):
        if self.off: # updates after its been drawn with flip, and goto can specify a layer to draw up to then stop
            if flip:
                pygame.display.flip()
            return False 
        if goto is None or goto not in self.layers:
            goto = len(self.layers)-1
        else:
            goto = self.layers[goto][0] # sets goto to either the last item or the item specified
        listtemp = [None for i in range(goto+1)] #saves all draw functions to a list in the correct draw order
        for i in self.layers:
            if self.layers[i][0] > goto:
                pass
            else:
                listtemp[self.layers[i][0]] = [self.layers[i][1], self.layers[i][2]]
        # executes all of the draw functions in order
        for i in listtemp:
            i[0](*i[1])
        if flip:
            pygame.display.flip() # updates if specified

    def toggle(self, onoff=None):# enables/disables the object
        if not self.off:
            self.off = True
        else:
            self.off = False
        if onoff is not None:
            self.off = onoff


class Scene: # Main class scene
    def __init__(self): # creates a new layer surface and a list of all the toggle functions of items
        self.layerSurface = LayerSurface()
        self.offButtons = {}

    def delete_entity(self, name): # deletes an off button
        del self.offButtons[name]

    def build(self, flip=False): # builds all of the items using the layer surface
        self.layerSurface.toggle(False)
        for i in self.offButtons:
            self.offButtons[i](False)
        self.layerSurface.draw(flip)

    def stop(self):# disables all of the objects in the scene
        self.layerSurface.toggle(True)
        for i in self.offButtons:
            self.offButtons[i](True)

    # The following functions just link to the self.layerscene function of the same name

    def draw(self, flip=False, goto=None):
        self.layerSurface.draw(flip, goto)

    def add_layer(self, layername, drawfunction, parameters):
        if layername not in self.layerSurface.layers:
            self.layerSurface.add_layer(layername, drawfunction, parameters)
        else:
            self.change_func(layername, drawfunction)
            self.change_para(layername, parameters)

    def delete_layer(self, layername):
        self.layerSurface.delete_layer(layername)

    def reorder_layer(self, layername, pos):
        self.layerSurface.reorder_layer(layername, pos)

    def change_para(self, layername, parameters):
        self.layerSurface.change_para(layername, parameters)

    def change_func(self, layername, function):
        self.layerSurface.change_func(layername, function)
