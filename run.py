import cv2 
import numpy as np 

from detection import DetectionC 
from Controls import controller
from Bot_Logic import Game 

detection = DetectionC()
Controls = controller()
game = Game(detection, controller)

game.run