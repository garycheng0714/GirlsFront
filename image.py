import os
import atx
from random import randrange
from action import Action
from point import Point


class Image(Action, object):
    """ handle the image operation"""
    def __init__(self, name, option_action=None, option=None):
        """
                name : example@auto.png
                """
        self.name = name + '@auto.png'
        self.note = os.path.basename(name).split('@')[0]
        self.coordinate = None
        self.option_action = option_action
        self.option = option

    def wait_image(self, device):
        """
                        search_info = [{'confidence': 0.9999350309371948,
                                                 'result': (693, 375),
                                                 'rectangle': ((628, 332), (628, 418), (758, 332), (758, 418))}]
                """
        search_info = device.wait(self.name)
        image_rectangle = search_info[0]['rectangle']
        min_x, min_y = min(image_rectangle)
        max_x, max_y = max(image_rectangle)
        self.coordinate = (randrange(min_x, max_x), randrange(min_y, max_y))

    def wait_image_gone(self, device):
        device.wait(self.name)
        device.wait_gone(self.name, timeout=120)

    def click(self, device):
        self.wait_image(device)
        super(Image, self).click(device)

    def exists(self, device):
        return device.exists(self.name)

    def click_somewhere_to_wait(self, device):
        self.wait(3)
        # if self.option:
        #     option_image = Image(os.path.join(os.path.dirname(self.name), self.option))
        while not self.exists(device):
            somewhere = Point("somewhere", randrange(105, 575), randrange(90, 350))
            somewhere.click(device)
            # self.wait(2)
            # if option_image.exists(device):
            #     option_image.click(device)

    def click_option_image_first(self, device):
        try:
            self.click(device)
        except atx.errors.ImageNotFoundError:
            Image(os.path.join(os.path.dirname(self.name), self.option)).click(device)
            self.click(device)

    def __str__(self):
        return "Image({})".format(self.note)
