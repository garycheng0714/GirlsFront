import constant
from image import Image
from point import Point
from random import randrange
from operation import use_image


class ImageForPresetting(Image):
    def __init__(self, name):
        super(ImageForPresetting, self).__init__(name)
        self.image_dir = constant.BATTLE_COMMON_IMAGE_DIR
        self.ok_button = use_image(self.image_dir, 'ok_button')
        self.support_again = use_image(self.image_dir, 'support_again')
        self.back_button = use_image(self.image_dir, 'back_button')
        self.return_button = use_image(self.image_dir, 'return_to_base')

    def click_somewhere_to_wait(self, device):
        while not self.exists(device):
            somewhere = Point("somewhere", randrange(105, 575), randrange(90, 350))
            somewhere.click(device)
            if self.support_again.exists(device):
                self.ok_button.click(device)
                self.wait(3)
            elif self.back_button.exists(device):
                self.back_button.click(device)
                self.wait(3)
            elif self.return_button.exists(device):
                self.return_button.click(device)
                self.wait(3)
