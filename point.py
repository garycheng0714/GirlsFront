from random import randrange
from action import Action


class Point(Action, object):
    """Handle the coordinate on device'"""
    def __init__(self, note, x, y, x1=None, y1=None):
        """  buffer offset for x is 50 pixes, y is 40 pixes in 960 x 540 resolution"""
        self.coordinate = (x + randrange(-5, 5),
                           y + randrange(-5, 5))
        self.position_1 = (x, y)
        self.position_2 = (x1, y1)
        self.note = note
        # self.skip_result = skip

    def click(self, device):
        super(Point, self).click(device)
        self.wait(1)

    def click_no_delay(self, device):
        super(Point, self).click(device)

    def swipe(self, device):
        x, y = self.position_1
        x1, y1 = self.position_2
        for i in range(5):
            device.swipe(x, y, x1, y1, steps=20)
        self.wait(1)

    def __str__(self):
        return "Point({}, {}, {})".format(self.note, *self.coordinate)
