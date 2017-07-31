import constant
import os
import time
from image import Image
from icon import FormationIcon


class Formation:
    def __init__(self, formation_type):
        self.mapping_dir = constant.FORMATION_MAPPING_DIR
        self.main_girls = []
        self.candidates = []
        self.skips_girls = []
        self.already_change = False
        self.formation_type = formation_type

    def run(self, device):
        FormationIcon.FORMATION_ICON.click(device)
        self.change_team1_members(device)
        FormationIcon.TEAM2.click(device)
        self.add_girls_to_team2(device)

    def change_team1_members(self, device):
        mapping_dirs = map(lambda x: os.path.join(self.mapping_dir, x), os.listdir(self.mapping_dir))
        for count, mapping_dir in enumerate(mapping_dirs):
            self.map_girl(mapping_dir)
            FormationIcon.SELECT_GIRLS.wait_image(device)
            self.change_girl(self.main_girls, self.candidates, count, device)

    def add_girls_to_team2(self, device):
        for girl in self.skips_girls:
            FormationIcon.SELECT_GIRLS.click(device)
            girl.click(device)
            time.sleep(1)
        FormationIcon.RETURN_TO_BASE.click(device)
        self.already_change = True
        self.skips_girls = []

    def map_girl(self, path):
        self.main_girls = map(lambda x: Image(os.path.join(path, x)), delete_extension(os.listdir(path)))
        candidate_file_name = map(lambda x: x.replace('formation_', ''), os.listdir(path))
        self.candidates = map(lambda x: Image(os.path.join(constant.GIRLS_IMAGE_DIR, x))
                              , delete_extension(candidate_file_name))

    def select_girls_type(self, device):
        """
                According  "formation_type" type to select type
                ex: "AR" or "RF"
                """
        if not self.formation_type:
            return
        FormationIcon.TYPE.click(device)
        if self.formation_type == constant.FORMATION_AR_TYPE:
            FormationIcon.AR.click(device)
        elif self.formation_type == constant.FORMATION_RF_TYPE:
            FormationIcon.RF.click(device)

    def change_girl(self, main, sub, count, device):
        for girl in main:
            if girl.exists(device):
                girl.click(device)
                if count == 0:
                    self.select_girls_type(device)
                for candidate in sub:
                    if candidate.note not in girl.note:
                        candidate.click(device)
                    else:
                        self.skips_girls.append(candidate)
                return


def delete_extension(files):
    result = []
    for file_name in files:
        result.append(file_name.split('.')[0])
    return result
