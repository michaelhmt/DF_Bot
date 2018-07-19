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

    	def find_Char(self): 
    		matches =  self.detection.find_template('Char_Select')
    		return np.shape(matches)[1] >= 1

    	def Menu-Quest(self): 
    		matches =  self.detection.find_template('Quest-Strat_01')
    		return np.shape(matches)[1] >= 1

    	def Select_Quest(self): 
    		matches =  self.detection.find_template('Quest-Selection')
    		return np.shape(matches)[1] >= 1

    	def Quest-Enter(self): 
    		matches =  self.detection.find_template('Quest-Enter')
    		return np.shape(matches)[1] >= 1

    	def Convo_Click-Zone(self): 
    		matches =  self.detection.find_template('Convo_Click-Zone')
    		return np.shape(matches)[1] >= 1

    	def Inactive17(self): 
    		matches =  self.detection.find_template('17_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive16(self): 
    		matches =  self.detection.find_template('16_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive15(self): 
    		matches =  self.detection.find_template('15_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive14(self): 
    		matches =  self.detection.find_template('14_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive13(self): 
    		matches =  self.detection.find_template('13_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive12(self): 
    		matches =  self.detection.find_template('12_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive11(self): 
    		matches =  self.detection.find_template('11_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive10(self): 
    		matches =  self.detection.find_template('10_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive09(self): 
    		matches =  self.detection.find_template('09_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive08(self): 
    		matches =  self.detection.find_template('08_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive07(self): 
    		matches =  self.detection.find_template('07_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive06(self): 
    		matches =  self.detection.find_template('06_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive05(self): 
    		matches =  self.detection.find_template('05_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive04(self): 
    		matches =  self.detection.find_template('04_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive03(self): 
    		matches =  self.detection.find_template('03_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive02(self): 
    		matches =  self.detection.find_template('02_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Inactive01(self): 
    		matches =  self.detection.find_template('01_Inactive')
    		return np.shape(matches)[1] >= 1

    	def Active17(self): 
    		matches =  self.detection.find_template('17-Active')
    		return np.shape(matches)[1] >= 1

    	def Active16(self): 
    		matches =  self.detection.find_template('16-Active')
    		return np.shape(matches)[1] >= 1

    	def Active15(self): 
    		matches =  self.detection.find_template('15-Active')
    		return np.shape(matches)[1] >= 1

    	def Active14(self): 
    		matches =  self.detection.find_template('14-Active')
    		return np.shape(matches)[1] >= 1

    	def Active13(self): 
    		matches =  self.detection.find_template('13-Active')
    		return np.shape(matches)[1] >= 1

    	def Active12(self): 
    		matches =  self.detection.find_template('12-Active')
    		return np.shape(matches)[1] >= 1

    	def Active11(self): 
    		matches =  self.detection.find_template('11-Active')
    		return np.shape(matches)[1] >= 1

    	def Active10(self): 
    		matches =  self.detection.find_template('10-Active')
    		return np.shape(matches)[1] >= 1

    	def Active09(self): 
    		matches =  self.detection.find_template('09-Active')
    		return np.shape(matches)[1] >= 1

    	def Active08(self): 
    		matches =  self.detection.find_template('08-Active')
    		return np.shape(matches)[1] >= 1

    	def Active07(self): 
    		matches =  self.detection.find_template('07-Active')
    		return np.shape(matches)[1] >= 1

    	def Active06(self): 
    		matches =  self.detection.find_template('06-Active')
    		return np.shape(matches)[1] >= 1

    	def Active05(self): 
    		matches =  self.detection.find_template('05-Active')
    		return np.shape(matches)[1] >= 1

    	def Active04(self): 
    		matches =  self.detection.find_template('04-Active')
    		return np.shape(matches)[1] >= 1

    	def Active03(self): 
    		matches =  self.detection.find_template('03-Active')
    		return np.shape(matches)[1] >= 1

    	def Active02(self): 
    		matches =  self.detection.find_template('02-Active')
    		return np.shape(matches)[1] >= 1

    	def Active01(self): 
    		matches =  self.detection.find_template('01-Active')
    		return np.shape(matches)[1] >= 1

    	def Finish_Qeust(self): 
    		matches =  self.detection.find_template('Finish_Qeust')
    		return np.shape(matches)[1] >= 1

    	def Close_Loot(self): 
    		matches =  self.detection.find_template('Close_Loot')
    		return np.shape(matches)[1] >= 1

    	def keep(self): 
    		matches =  self.detection.find_template('keep')
    		return np.shape(matches)[1] >= 1

    	def Screen_Transition(self): 
    		matches =  self.detection.find_template('Screen_Transition')
    		return np.shape(matches)[1] >= 1








