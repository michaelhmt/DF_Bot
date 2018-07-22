import cv2
from mss import mss
from PIL import Image
import numpy as np
import time

class DetectionC:
    def __init__(self):
        self.static_templates = {
            'Char_Select': 'Assets/Char_Select.png',
            'Screen_Transition': 'Assets/Screen_Transition.png',
            'keep': 'Assets/keep.png',
            'Close_Loot': 'Assets/Close_Loot.png',
            'Finish_Qeust': 'Assets/FinishQeustImg.png',
            '17_Inactive': 'Assets/17_Inactive.png',
            '16-Inactive': 'Assets/16-Inactive.png',
            '15-Inactive': 'Assets/15-Inactive.png',
            '14-Inactive': 'Assets/14-Inactive.png',
            '13-Inactive': 'Assets/13-Inactive.png',
            '12-Inactive': 'Assets/12-Inactive.png',
            '11-Inactive': 'Assets/11-Inactive.png',
            '10-Inactive': 'Assets/10-Inactive.png',
            '09-Inactive': 'Assets/09-Inactive.png',
            '08-Inactive': 'Assets/08-Inactive.png',
            '07-Inactive': 'Assets/07-Inactive.png',
            '06-Inactive': 'Assets/06-Inactive.png',
            '05-Inactive': 'Assets/05-Inactive.png',
            '04-Inactive': 'Assets/04-Inactive.png',
            '03-Inactive': 'Assets/03-Inactive.png',
            '02-Inactive': 'Assets/02-Inactive.png',
            '01-Inactive': 'Assets/01-Inactive.png',
            '01-Active': 'Assets/01-Active.png',
            '02-Active': 'Assets/02-Active.png',
            '03-Active': 'Assets/03-Active.png',
            '04-Active': 'Assets/04-Active.png',
            '05-Active': 'Assets/05-Active.png',
            '06-Active': 'Assets/06-Active.png',
            '07-Active': 'Assets/07-Active.png',
            '08-Active': 'Assets/08-Active.png',
            '09-Active': 'Assets/09-Active.png',
            '10-Active': 'Assets/10-Active.png',
            '11-Active': 'Assets/11-Active.png',
            '12-Active': 'Assets/12-Active.png',
            '13-Active': 'Assets/13-Active.png',
            '14-Active': 'Assets/14-Active.png',
            '15-Active': 'Assets/15-Active.png',
            '16-Active': 'Assets/16-Active.png',
            '17-Active': 'Assets/17-Active.png',
            'Quest-Enter': 'Assets/Quest-Enter',
            'Quest-Selection': 'Assets/Quest-Selection.png',
            'Quest-Strat_01': 'Assets/Quest-Strat_01.png', 
            'Convo_Click-Zone': 'Assets/Convo_Click-Zone.png'
        }

        self.templates = { k: cv2.imread(v, 0) for (k, v) in self.static_templates.items() }

        self.monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
        self.screen = mss()

        self.frame = None

    def take_screenshot(self):
        sct_img = self.screen.grab(self.monitor)
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        img = np.array(img)
        img = self.convert_rgb_to_bgr(img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img_gray

    def get_image(self, path):
        return cv2.imread(path, 0)

    def bgr_to_rgb(self, img):
        b,g,r = cv2.split(img)
        return cv2.merge([r,g,b])

    def convert_rgb_to_bgr(self, img):
        return img[:, :, ::-1]

    def match_template(self, img_grayscale, template, threshold=0.9):
        """
        Matches template image in a target grayscaled image
        """

        res = cv2.matchTemplate(img_grayscale, template, cv2.TM_CCOEFF_NORMED)
        matches = np.where(res >= threshold)
        return matches

    def find_template(self, name, image=None, threshold=0.9):
        if image is None:
            if self.frame is None:
                self.refresh_frame()

            image = self.frame

        return self.match_template(
            image,
            self.templates[name],
            threshold
        )

    def scaled_find_template(self, name, image=None, threshold=0.9, scales=[1.0, 0.9, 1.1]):
        if image is None:
            if self.frame is None:
                self.refresh_frame()

            image = self.frame

        initial_template = self.templates[name]
        for scale in scales:
            scaled_template = cv2.resize(initial_template, (0,0), fx=scale, fy=scale)
            matches = self.match_template(
                image,
                scaled_template,
                threshold
            )
            if np.shape(matches)[1] >= 1:
                return matches
        return matches

    def refresh_frame(self):
        self.frame = self.take_screenshot()
