import pygame

from LCARS.Controls import Drawable
from pkg_resources import resource_filename

FONT_SEARCH = "swiss911"
FONT_NAME = "Swiss911ExtraCompressed.ttf"

def getHeight(text, size):
	(w, h) = pygame.font.SysFont(font, size).size(text)
	return w

class TextAlign:
	XALIGN_CENTRE = 0
	XALIGN_LEFT = 1
	XALIGN_RIGHT = 2

class Text(Drawable):
	def __init__(self, alignpoint, text, size, xalign, fg, bg):
		(x, y) = alignpoint
		self.alignpoint = alignpoint
		self.text_string = text
		self.fontsize = size
		self.xalign = xalign

		font_list = pygame.font.get_fonts()
		font_list = [font for font in font_list if (font.find(FONT_SEARCH) > -1)]
		font_file = resource_filename(__name__, "../data/fonts/%s" % FONT_NAME)

		if len(font_list)>0:
			font_file = font_list[0]

		self.font = pygame.font.Font(font_file, size)
		self.text = self.font.render(text, 1, fg, bg)

		# Define enclosing rectangle based on alignment point and align choice
		top = y - (self.text.get_height() / 2)
		if (xalign == TextAlign.XALIGN_CENTRE):
			left = x - (self.text.get_width() / 2)
		elif (xalign == TextAlign.XALIGN_RIGHT):
			left = x - self.text.get_width()
		elif (xalign == TextAlign.XALIGN_LEFT):
			left = x

		rect = pygame.Rect(left, top, self.text.get_width(), self.text.get_height())

		Drawable.__init__(self, rect, fg, bg)

	def draw(self, window):
		window.blit(self.text, self.rect)
