import cv2 
import numpy as np 

from detection import DetectionC 
from Controls import controller
from Bot_Logic import BotAction 

detection = DetectionC()
Controls = controller()
Bot_Logic = BotAction(detection, Controls)

Bot_Logic.activate()
print("is now running")