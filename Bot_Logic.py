import numpy as np 
import time 

class Game: 

	def __init__(self, detection, controller):
        self.detection = detection
        self.controller = controller
        self.state = 'not started'

    def can_see_Object(self, template, threshold=0.9): 
    	matches = self.detection.find_template(template. threshold=threshold)
    	return np.shape(matches)[1] >= 1
    def click_object(self, template, offset=(0, 0)):
    	matches = self.detection.find_template(template)

    	x = matches [1][0] + offset[0]
    	y = matches [0][0] + offset[1]

    	self.controller.move_mouse(x, y)
    	self.controller.left_mouse_click()

    	time.sleep(0.5)
    	

