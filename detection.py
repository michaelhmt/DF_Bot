import cv2 
from mss import mss 
from pillow import Image
import mumpy as np 
import time 

class vision: 
     def __init__(self):
       self.static_templates = {
       'Char_Select': 'Assets/Char_Select.png',
       'Screen_Transition': 'Assets/Screen_Transition',
       'keep': 'Assets/keep',
       'Close_Loot': 'Assets/Close_Loot',
       'Finish_Qeust': 'Assets/Finish_Qeust',
       '17_Inactive': 'Assets/17_Inactive',
       '16-Inactive': 'Assets/16-Inactive',
       '15-Inactive': 'Assets/15-Inactive',
       '14-Inactive': 'Assets/14-Inactive',
       '13-Inactive': 'Assets/13-Inactive',
       '12-Inactive': 'Assets/12-Inactive',
       '11-Inactive': 'Assets/11-Inactive',
       '10-Inactive': 'Assets/10-Inactive',
       '09-Inactive': 'Assets/09-Inactive',
       '08-Inactive': 'Assets/08-Inactive',
       '07-Inactive': 'Assets/07-Inactive',
       '06-Inactive': 'Assets/06-Inactive',
       '05-Inactive': 'Assets/05-Inactive',
       '04-Inactive': 'Assets/04-Inactive',
       '03-Inactive': 'Assets/03-Inactive',
       '02-Inactive': 'Assets/02-Inactive',
       '01-Inactive': 'Assets/01-Inactive',
       '01-Active': 'Assets/01-Active',
       '02-Active': 'Assets/02-Active',
       '03-Active': 'Assets/03-Active',
       '04-Active': 'Assets/04-Active',
       '05-Active': 'Assets/05-Active',
       '06-Active': 'Assets/06-Active',
       '07-Active': 'Assets/07-Active',
       '08-Active': 'Assets/08-Active',
       '09-Active': 'Assets/09-Active',
       '10-Active': 'Assets/10-Active',
       '11-Active': 'Assets/11-Active',
       '12-Active': 'Assets/12-Active',
       '13-Active': 'Assets/13-Active',
       '14-Active': 'Assets/14-Active',
       '15-Active': 'Assets/15-Active',
       '16-Active': 'Assets/16-Active',
       '17-Active': 'Assets/17-Active',
       'Quest-Enter': 'Assets/Quest-Enter',
       'Quest-Selection': 'Assets/Quest-Selection',
       'Quest-Strat_01': 'Assets/Quest-Strat_01'                 #very image the bot can identify and click on 
       } 

       self.templates = { k: cv2.imread(v, 0) for (k, v) in self.static_templates.items()} # images read by cv2 the 0 reads those images as grey scale

       self.monitor =  {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
       self.screen = mss()

       self.frame = none