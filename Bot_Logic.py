import numpy as np 
import time 

#AppendSCache = open('sequence_cache.txt','a')
#ClearSCache = open('sequence_cache.txt','w' )
#ReadSCache  = open('sequence_cache.txt','r' ).readlines
#activerefresh = 01
#CaptureTBufferlimt = 06
#CaptureTBuffer = 0
#game enter = 0

class Game: 

AppendSCache = open('sequence_cache.py','a')
ClearSCache = open('sequence_cache.py','w' )
ReadSCache  = open('sequence_cache.py','r' ).readlines()
activerefresh = 01
CaptureTBufferlimt = 06
CaptureTBuffer = 0
NewPuzzle = True

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

    	def findChar(self): 
    		matches =  self.detection.find_template('Char_Select')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+40, y+60)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def MenuQuest(self): 
    		matches =  self.detection.find_template('Quest-Strat_01')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+60, y+10)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def SelectQuest(self): 
    		matches =  self.detection.find_template('Quest-Selection')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+40, y+60)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def QuestEnter(self): 
    		matches =  self.detection.find_template('Quest-Enter')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+40, y+60)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def ConvoClickZone(self): 
    		matches =  self.detection.find_template('Convo_Click-Zone')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+30, y+30)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive17(self): 
    		matches =  self.detection.find_template('17_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive16(self): 
    		matches =  self.detection.find_template('16_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive15(self): 
    		matches =  self.detection.find_template('15_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive14(self): 
    		matches =  self.detection.find_template('14_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive13(self): 
    		matches =  self.detection.find_template('13_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive12(self): 
    		matches =  self.detection.find_template('12_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive11(self): 
    		matches =  self.detection.find_template('11_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive10(self): 
    		matches =  self.detection.find_template('10_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive09(self): 
    		matches =  self.detection.find_template('09_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive08(self): 
    		matches =  self.detection.find_template('08_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive07(self): 
    		matches =  self.detection.find_template('07_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive06(self): 
    		matches =  self.detection.find_template('06_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive05(self): 
    		matches =  self.detection.find_template('05_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive04(self): 
    		matches =  self.detection.find_template('04_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive03(self): 
    		matches =  self.detection.find_template('03_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive02(self): 
    		matches =  self.detection.find_template('02_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Inactive01(self): 
    		matches =  self.detection.find_template('01_Inactive')
            x = matches[1][0]
            y = matches[0][0]
            self.controller.move_mouse(x+30, y+30)
            self.controller.left_mouse_click()
            time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def Active17(self): 
    		matches =  self.detection.find_template('17-Active') 
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive17() \n Inactive17()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active16(self): 
    		matches =  self.detection.find_template('16-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive16() \n Inactive16()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active15(self): 
    		matches =  self.detection.find_template('15-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive15() \n Inactive15()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active14(self): 
    		matches =  self.detection.find_template('14-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive14() \n Inactive14()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active13(self): 
    		matches =  self.detection.find_template('13-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive13() \n Inactive13()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active12(self): 
    		matches =  self.detection.find_template('12-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive12() \n Inactive12()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active11(self): 
    		matches =  self.detection.find_template('11-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive11() \n Inactive11()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active10(self): 
    		matches =  self.detection.find_template('10-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive10() \n Inactive10()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active09(self): 
    		matches =  self.detection.find_template('09-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive09() \n Inactive09()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active08(self): 
    		matches =  self.detection.find_template('08-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive08() \n Inactive08()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active07(self): 
    		matches =  self.detection.find_template('07-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive07() \n Inactive07()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active06(self): 
    		matches =  self.detection.find_template('06-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive06() \n Inactive06()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active05(self): 
    		matches =  self.detection.find_template('05-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive05() \n Inactive05()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active04(self): 
    		matches =  self.detection.find_template('04-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive04() \n Inactive04()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active03(self): 
    		matches =  self.detection.find_template('03-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive03() \n Inactive03()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active02(self): 
    		matches =  self.detection.find_template('02-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive02() \n Inactive02()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def Active01(self): 
    		matches =  self.detection.find_template('01-Active')
    		AppendSCache.write('\nfrom Bot_Logic.y import Inactive01() \n Inactive01()') 
    		AppendSCache.close()
    		time.sleep(activerefresh)
    		return np.shape(matches)[1] >= 1

    	def FinishQeust(self): 
    		matches =  self.detection.find_template('Finish_Qeust')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+100, y+30)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def CloseLoot(self): 
    		matches =  self.detection.find_template('Close_Loot')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+70, y+20)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def keep(self): 
    		matches =  self.detection.find_template('keep')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+60, y+20)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1

    	def ScreenTransition(self): 
    		matches =  self.detection.find_template('Screen_Transition')
    		x = matches[1][0]
    		y = matches[0][0]
    		self.controller.move_mouse(x+00, y+40)
    		self.controller.left_mouse_click()
    		time.sleep(0.5)
    		return np.shape(matches)[1] >= 1
    	def GameTrigger(self): 
    		matches =  self.detection.find_template('GameTrigger')
    		x = matches[1][0]
    		y = matches[0][0]
    		return np.shape(matches)[1] >= 1

    	def capture(self):
            ClearSCache.write('class Sequence')
    		self.detection.refresh_frame()
    		if self.Active01('01-Active'):
    			self.log('01 Active')
    			self.Active01()
    		elif self.Active02('02-Active'):
    			self.log('02 Active')
    			self.Active02()
    		elif self.Active03('03-Active'):
    			self.log('03 Active')
    			self.Active03()
    		elif self.Active04('04-Active'):
    			self.log('04 Active')
    			self.Active04()
    		elif self.Active05('05-Active'):
    			self.log('05 Active')
    			self.Active05()
    		elif self.Active06('06-Active'):
    			self.log('06 Active')
    			self.Active06()
    		elif self.Active07('07-Active'):
    			self.log('07 Active')
    			self.Active07()
    		elif self.Active08('08-Active'):
    			self.log('08 Active')
    			self.Active08()
    		elif self.Active09('09-Active'):
    			self.log('09 Active')
    			self.Active09()
    		elif self.Active10('10-Active'):
    			self.log('10 Active')
    			self.Active10()
    		elif self.Active11('11-Active'):
    			self.log('11 Active')
    			self.Active11()
    		elif self.Active12('12-Active'):
    			self.log('12 Active')
    			self.Active12()
    		elif self.Active13('13-Active'):
    			self.log('13 Active')
    			self.Active13()
    		elif self.Active14('14-Active'):
    			self.log('14 Active')
    			self.Active14()
    		elif self.Active15('15-Active'):
    			self.log('15 Active')
    			self.Active15()
    		elif self.Active16('16-Active'):
    			self.log('16 Active')
    			self.Active16()
    		elif self.Active17('17-Active'):
    			self.log('17 Active')
    			self.Active17()
    		else CaptureTBuffer + 1 if CaptureTBuffer == CaptureTBufferlimt:
    		     self.state == ('Puzzle complete')
    		     self.log('Puzzle complete properly')  




    def run(self): 
    	while True:
    		self.detection.refresh_frame()
    		if self.findChar('Char_Select'):
    			self.log('can see qeust giver')
    			self.find_Char()
    			self.state = 'started'
    		elif self.state == 'started' and self.MenuQuest('Quest-Strat_01'):
    			self.log('Found Qeust enter')
    			self.MenuQuest() 
    			self.state = 'in menu' 
    		elif self.state == 'in menu' and self.SelectQuest('Quest-Selection'):
    			self.log('found qeust selection')
    			self.SelectQuest() 
    			self.state = 'in menu'
    		elif self.state == 'in menu' and self.QuestEnter('Quest-Enter'):
    			self.log('found qeust selection')
    			self.QuestEnter() 
    			self.state = 'in Dialogue'
    		elif self.state == 'in Dialogue' and self.ConvoClickZone('Convo_Click-Zone'):
    			self.log('clicking through convo')
    			self.ConvoClickZone() 
    			self.state = 'in Dialogue'
    		elif self.state == 'in Dialogue' and self.GameTrigger('GameTrigger') and NewPuzzle = True:
    			self.log('game in progress')
    			self.capture()
    			self.state('In Capture mode') 
    			NewPuzzle = False
            elif self.state == 'Puzzle complete'
    			self.log('loading and solvling Sequence')
                from sequence_cache import Sequence
                Sequence.run()
                time.sleep(0.2)
                NewPuzzle = True 
            elif self.FinishQeust('Finish_Qeust'):
                self.log('Quest finished')
                self.FinishQeust() 
                self.state ='in Qeust complete menu'
            elif self.state == 'in Qeust complete menu' and self.CloseLoot('Close_Loot'):
                self.log('closing qeust menu')
                self.Close_Loot() 
                self.state = 'in Loot menu'
            elif self.state == 'in Loot menu' and self.keep('keep'):
                self.log('keeping loot')
                self.keep() 
                self.state = 'In game world'
            elif self.state == 'In game world' and self.ScreenTransition('Screen_Transition'):
                self.log('Moving back to start')
                self.ScreenTransition() 
                self.state = 'In game world'
            













