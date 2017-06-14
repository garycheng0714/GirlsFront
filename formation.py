import constant
import os
import time
import atx
from image import Image
from operation import use_image


class Formation:
    def __init__(self, need_formation):
        self.mapping_dir = constant.FORMATION_MAPPING_DIR
        self.main_girls = []
        self.candidates = []
        self.skips_girls = []
        self.formation_icon = use_image(constant.FORMATION_IMAGE_DIR, 'formation')
        self.team2_icon = use_image(constant.FORMATION_IMAGE_DIR, 'team2')
        self.add_icon = use_image(constant.FORMATION_IMAGE_DIR, 'formation_add_icon')
        self.return_icon = use_image(constant.FORMATION_IMAGE_DIR, 'return_to_base')
        self.already_change = False
        self.need_formation = need_formation

    def run(self, device):
        self.formation_icon.click(device)
        self.change_team1_members(device)
        self.team2_icon.click(device)
        self.add_girls_to_team2(device)

    def change_team1_members(self, device):
        mapping_dirs = map(lambda x: os.path.join(self.mapping_dir, x), os.listdir(self.mapping_dir))
        for mapping_dir in mapping_dirs:
            self.map_girl(mapping_dir)
            self.add_icon.wait_image(device)
            self.change_girl(self.main_girls, self.candidates, device)

    def add_girls_to_team2(self, device):
        for girl in self.skips_girls:
            self.add_icon.click(device)
            girl.click(device)
            time.sleep(1)
        self.return_icon.click(device)
        self.already_change = True
        self.skips_girls = []

    def map_girl(self, path):
        self.main_girls = map(lambda x: Image(os.path.join(path, x)), delete_extension(os.listdir(path)))
        candidate_file_name = map(lambda x: x.replace('formation_', ''), os.listdir(path))
        self.candidates = map(lambda x: Image(os.path.join(constant.GIRLS_IMAGE_DIR, x))
                              , delete_extension(candidate_file_name))

    def change_girl(self, main, sub, device):
        for girl in main:
            if girl.exists(device):
                girl.click(device)
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

if __name__ == '__main__':
    device = atx.connect('4200c49cf2faa381')
    Formation().run(device)
