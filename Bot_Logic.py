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
    		return self.can_see_Object('Char_Select')

    	def Menu-Quest(self): 
    		return self.can_see_Object('Quest-Strat_01')

    	def Select_Quest(self): 
    		return self.can_see_Object('Quest-Selection')

    	def Quest-Enter(self): 
    		return self.can_see_Object('Quest-Enter')

    	def Convo_Click-Zone(self): 
    		return self.can_see_Object('Convo_Click-Zone')

    	def Inactive17(self): 
    		return self.can_see_Object('17_Inactive')

    	def Inactive16(self): 
    		return self.can_see_Object('16_Inactive')

    	def Inactive15(self): 
    		return self.can_see_Object('15_Inactive')

    	def Inactive14(self): 
    		return self.can_see_Object('14_Inactive')

    	def Inactive13(self): 
    		return self.can_see_Object('13_Inactive')

    	def Inactive12(self): 
    		return self.can_see_Object('12_Inactive')

    	def Inactive11(self): 
    		return self.can_see_Object('11_Inactive')

    	def Inactive10(self): 
    		return self.can_see_Object('10_Inactive')

    	def Inactive09(self): 
    		return self.can_see_Object('09_Inactive')

    	def Inactive08(self): 
    		return self.can_see_Object('08_Inactive')

    	def Inactive07(self): 
    		return self.can_see_Object('07_Inactive')

    	def Inactive06(self): 
    		return self.can_see_Object('06_Inactive')

    	def Inactive05(self): 
    		return self.can_see_Object('05_Inactive')

    	def Inactive04(self): 
    		return self.can_see_Object('04_Inactive')

    	def Inactive03(self): 
    		return self.can_see_Object('03_Inactive')

    	def Inactive02(self): 
    		return self.can_see_Object('02_Inactive')

    	def Inactive01(self): 
    		return self.can_see_Object('01_Inactive')

    	def Active17(self): 
    		return self.can_see_Object('17-Active')

    	def Active16(self): 
    		return self.can_see_Object('16-Active')

    	def Active15(self): 
    		return self.can_see_Object('15-Active')

    	def Active14(self): 
    		return self.can_see_Object('14-Active')

    	def Active13(self): 
    		return self.can_see_Object('13-Active')

    	def Active12(self): 
    		return self.can_see_Object('12-Active')

    	def Active11(self): 
    		return self.can_see_Object('11-Active')

    	def Active10(self): 
    		return self.can_see_Object('10-Active')

    	def Active09(self): 
    		return self.can_see_Object('09-Active')

    	def Active08(self): 
    		return self.can_see_Object('08-Active')

    	def Active07(self): 
    		return self.can_see_Object('07-Active')

    	def Active06(self): 
    		return self.can_see_Object('06-Active')

    	def Active05(self): 
    		return self.can_see_Object('05-Active')

    	def Active04(self): 
    		return self.can_see_Object('04-Active')

    	def Active03(self): 
    		return self.can_see_Object('03-Active')

    	def Active02(self): 
    		return self.can_see_Object('02-Active')

    	def Active01(self): 
    		return self.can_see_Object('01-Active')

    	def Finish_Qeust(self): 
    		return self.can_see_Object('Finish_Qeust')

    	def Close_Loot(self): 
    		return self.can_see_Object('Close_Loot')

    	def keep(self): 
    		return self.can_see_Object('keep')
    		
    	def Screen_Transition(self): 
    		return self.can_see_Object('Screen_Transition')








