import constant
import os
from image import Image
from point import Point
from common_flow import CommonFlow
from operation import InventoryCommon


class PowerUp(InventoryCommon):
    def __init__(self):
        self.power_up_dir = constant.POWER_UP_DIR
        self.image_dir = constant.INVENTORY_IMAGE_DIR
        self.girls_dir = constant.POWER_UP_GIRLS_DIR
        self.already_power_up = False
        self.enter_power_up_page = CommonFlow(self.power_up_dir, self.image_dir, 'enter_power_up_page.xlsx')

    def run(self, device):
        if not self.already_power_up:
            self.enter_power_up_page.run(device)
            self.power_up(device)

    def power_up(self, device):
        girls_be_powered_up = filter(lambda x: x.endswith('.png'), os.listdir(self.girls_dir))
        girls_num = len(girls_be_powered_up)
        cancel_button = Image(image_path('cancel_button2'))
        for index, girl in enumerate(girls_be_powered_up):
            girl = girl.split('.')[0]
            girl_image = Image(os.path.join(self.girls_dir, girl))
            if girl_image.exists(device):
                girl_image.click(device)
                self.pick_up_and_power(device)
                if not self.check_status(device):
                    break
                if index < girls_num:
                    Point('select_girl_be_powered_up', 238, 226).click(device)
        self.already_power_up = True
        if cancel_button.exists(device):
            cancel_button.click(device)
        Image(image_path('return_to_base')).click(device)

    def pick_up_and_power(self, device):
        """first row (1-1 to 1-6) and 2-1, location for 1-1 is (70, 180)
                    90 is offset, use device.click due to do not want to wait"""
        self.order_girls_by_rarity(device)
        self.select_one_row(70, 180, device)
        self.optional_select(device)
        self.click_button('power_up', device)

def image_path(filename):
    return os.path.join(constant.INVENTORY_IMAGE_DIR, filename)

if __name__ == '__main__':
    import atx
    device = atx.connect('4200c49cf2faa381')
    PowerUp().run(device)