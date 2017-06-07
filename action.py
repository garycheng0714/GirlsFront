import datetime
from time import sleep
from random import randrange


class Action:
    def click(self, device):
        """ click point(x, y) on device """
        x, y = self.coordinate
        print(str(datetime.datetime.now().strftime("%m-%d %H:%M:%S")) +
              "\t position(%d, %d)\t description: %s" % (x, y, self.note))
        device.click(x, y)

    def wait(self, time):
        random_buffer = randrange(0, 4) / 10.0
        sleep(int(time) + random_buffer)
