import pyglet
import os, sys, importlib
from pyglet import window
from pyglet import font
   
class OutputWindow(window.Window):
		
	def __init__(self, *args, **kwargs):

		self.win = window.Window.__init__(self, *args, **kwargs)
		font_loaded = font.load('Tahoma', 20)
		self.fpstext = font.Text(font_loaded, y=10)
		self.flip()
	
def size(height, width):
	global win
	win.set_size(height, width)
	win.flip()

# Test program begins here

def setup():
	size(500, 500)

# Test program ends here

if __name__  == '__main__':
	
	global win
	win = OutputWindow(height = 480, width = 640, caption = "This was a triumph")
	
	setup()

	pyglet.app.run()