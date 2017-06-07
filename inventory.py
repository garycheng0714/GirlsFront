from power_up import PowerUp
from retire import Retire
from image import Image
import constant


class Inventory:
    def __init__(self):
        self.power_up_system = PowerUp()
        self.retire_system = Retire()

    def hit_limit(self, device):
        """check whether hit the limit of inventory"""
        limit_warning = Image(constant.HIT_LIMIT_ICON)
        check_result = limit_warning.exists(device)
        if check_result:
            if not self.power_up_system.already_power_up:
                self.power_up_system.run(device)
            else:
                self.retire_system.run(device)
                self.power_up_system.already_power_up = False
            return True
        else:
            return False
