import cv2 
import numpy as np 

from detection import detection 
from Controls import controller
from Bot_Logic import Game 

detection = Detection()
Controls = Controller()
game = Game(detection, controller)

game.run