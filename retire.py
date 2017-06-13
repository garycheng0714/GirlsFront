import constant
import os
import time
from common_flow import CommonFlow
from operation import InventoryCommon
from point import Point
from image import Image


class Retire(InventoryCommon):
    def __init__(self):
        self.retire_dir = constant.RETIRE_DIR

    def run(self, device):
        enter_retire_page = CommonFlow(self.retire_dir, constant.INVENTORY_IMAGE_DIR, 'enter_retire_page.xlsx')
        enter_retire_page.run(device)
        self.retire_girl(device)

    def check_status(self, device):
        warning = Image(os.path.join(constant.INVENTORY_IMAGE_DIR, 'retire_warning'))
        cancel_button = Image(os.path.join(constant.INVENTORY_IMAGE_DIR, 'cancel_button'))
        if warning.exists(device):
            cancel_button.click(device)
            return False
        return True

    def retire_girl(self, device):
        need_retire = True
        self.order_girls_by_rarity(device)
        time.sleep(2)
        Point('swipe', 400, 428, 400, 160).swipe(device)
        time.sleep(1)
        while need_retire:
            self.select_one_row(70, 410, device)
            self.click_button('retire', device)
            need_retire = self.check_status(device)
            if need_retire:
                Image(os.path.join(constant.INVENTORY_IMAGE_DIR, 'select_be_added')).click(device)
                time.sleep(1)
        Image(os.path.join(constant.INVENTORY_IMAGE_DIR, 'return_to_base')).click(device)
