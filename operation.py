import constant
import os
import time
from point import Point
from image import Image
from common_flow import CommonFlow
from random import randrange


class InventoryCommon:
    def order_girls_by_rarity(self, device):
        operation = CommonFlow(constant.INVENTORY_DIR, constant.INVENTORY_IMAGE_DIR, 'order_girls_by_rarity.xlsx')
        operation.run(device)

    def select_one_row(self, x, y, device, offset=130):
        Point('pick_up', x, y).click_no_delay(device)
        for i in range(5):
            x += offset
            Point('pick_up', x, y).click_no_delay(device)

    def optional_select(self, device):
        more = [(70, 410), (200, 410), (330, 410)]
        index = randrange(0, 3)
        for i in range(index):
            x, y = more[i]
            Point('pick_up', x, y).click_no_delay(device)

    def click_button(self, button, device):
        Image(os.path.join(constant.INVENTORY_IMAGE_DIR, 'ok_button')).click(device)
        Image(os.path.join(constant.INVENTORY_IMAGE_DIR, button)).click(device)
        time.sleep(3)

    def check_status(self, device):
        close_button = Image(os.path.join(constant.INVENTORY_IMAGE_DIR, 'close_button'))
        cancel_button = Image(os.path.join(constant.INVENTORY_IMAGE_DIR, 'cancel_button'))
        if close_button.exists(device):
            close_button.click(device)
            time.sleep(3)
            return True
        else:
            cancel_button.click(device)
            return False


def use_image(path, filename):
    return Image(os.path.join(path, filename))
