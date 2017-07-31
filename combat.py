import os
import constant
from common_flow import CommonFlow
from inventory import Inventory
from formation import Formation
from restore import Restore
from image_for_presetting import ImageForPresetting


class Battle:
    """ handle how to execute battle flow"""
    def __init__(self, name, formation_type):
        self.name = name
        self.common_image_dir = constant.BATTLE_COMMON_IMAGE_DIR
        self.war_dir = os.path.join(constant.WARS_DIR, self.name)
        self.war_image_dir = os.path.join(self.war_dir, 'image')
        self.inventory = Inventory()
        self.restore = Restore()
        self.formation = Formation(formation_type)

    def run(self, device):
        rounds = 0
        presetting = ImageForPresetting(os.path.join(constant.BATTLE_COMMON_IMAGE_DIR, 'combat'))
        while True:
            presetting.click_somewhere_to_wait(device)
            try:
                self.restore.check(device)
                if self.formation.formation_type:
                    self.run_formation(device)
                self.enter_combat(device)
                while self.inventory.hit_limit(device):
                    self.enter_combat(device)
                self.apply_flow(device)
                self.battle_flow(device)
                if self.formation.formation_type:
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

    def enter_combat(self, device):
        enter_combat = CommonFlow(self.war_dir, self.war_image_dir, 'enter.xlsx')
        enter_combat.run(device)

    def apply_flow(self, device):
        apply_team = CommonFlow(self.war_dir, self.war_image_dir, 'apply.xlsx')
        apply_team.run(device)

    def battle_flow(self, device):
        battle = CommonFlow(self.war_dir, self.common_image_dir, self.name + '.xlsx')
        battle.run(device)
