import time
import os
import constant
from common_flow import CommonFlow
from inventory import Inventory
from formation import Formation
from restore import Restore
from image_for_presetting import ImageForPresetting


class Battle:
    """ handle how to execute battle flow"""
    def __init__(self, name, need_formation):
        self.name = name
        self.common_image_dir = constant.BATTLE_COMMON_IMAGE_DIR
        self.war_dir = os.path.join(constant.WARS_DIR, self.name)
        self.war_image_dir = os.path.join(self.war_dir, 'image')
        self.enter_combat = CommonFlow(self.war_dir, self.war_image_dir, 'enter.xlsx')
        self.apply_flow = CommonFlow(self.war_dir, self.war_image_dir, 'apply.xlsx')
        self.battle_flow = CommonFlow(self.war_dir, self.common_image_dir, self.name + '.xlsx')
        self.inventory = Inventory()
        self.restore = Restore()
        if need_formation:
            self.formation = Formation()

    def run(self, device):
        rounds = 0
        presetting = ImageForPresetting(os.path.join(constant.BATTLE_COMMON_IMAGE_DIR, 'combat'))
        while True:
            presetting.click_somewhere_to_wait(device)
            try:
                self.restore.check(device)
                self.run_formation(device)
                self.enter_combat.run(device)
                while self.inventory.hit_limit(device):
                    self.enter_combat.run(device)
                self.apply_flow.run(device)
                self.battle_flow.run(device)
                self.formation.already_change = False
            except Exception as error:
                print(error)
                continue
            rounds += 1
            print("The round :" + str(rounds))

    def run_formation(self, device):
        if self.formation and not self.formation.already_change:
            self.formation.run(device)
            self.formation.already_change = True

if __name__ == '__main__':
    start = time.clock()
    # test = Battle("battles", "4-3e.xlsx")
    # test.get_steps()
    # test.show_steps()
    # test.execute()
    # print(__file__)
    print("abspath: " + os.path.abspath(__file__))
    print("basename: " + os.path.basename(__file__))
    print("dirname: " + os.path.dirname(__file__))
    end = time.clock()
    print(end - start)
