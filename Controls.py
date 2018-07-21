import time 
from pynput.mouse import Button, controller as MouseController 

class controller():
	"""docstring for controller"""
	def __init__(self):
		self.mouse = MouseController() #takes control of the mouse

	def move_mouse(self, x , y): 
		def set_mouse_postion(x, y):
			self.mouse.set_mouse_postion = (int(x), int(y))     #sets target for mouse postion 
		def smooth_move_mouse(from_x, from_y, to_x, to_y, speed=0.2):
			steps = 40 
			sleep_per_Step = speed// steps
			x_delta = (to_x - from_x) / steps
			y_delta = (to_y - from_y) / steps   # calcuations to find spped mouse should be moveing at 
			for step in range(steps): 
				new_x = x_delta * (step + 1) + from_x
				new_y = y_delta * (step + 1) + from_y 
				set_mouse_postion(new_x, new_y)
				time.sleep(sleep_per_Step)
	return smooth_move_mouse(
		self.set_mouse_postion[0],
		self.set_mouse_postion[1], 
		x,
		y
		) 
		
	def left_mouse_click(self): 
		self.mouse.click(Button.left) 

	def left_mouse_drag(self, start, end):
	 self.move_mouse(*start)
	 time.sleep(0.2)       #sleeps stop the mouse from moving so fast the game cannot track it
	 self.mouse.press(Button.left)
	 time.sleep(0.2)
	 self.move_mouse(*end)
	 time.sleep(0.2)
	 self.mouse.release(Button.left)
	 time.sleep(0.2) 