import os
import constant
from image import Image


def use_image(path, filename):
    return Image(os.path.join(path, filename))


class FormationIcon:

    path = constant.FORMATION_IMAGE_DIR

    FORMATION_ICON = use_image(path, 'formation')
    SELECT_GIRLS = use_image(path, 'formation_add_icon')
    RETURN_TO_BASE = use_image(path, 'return_to_base')
    TEAM2 = use_image(path, 'team2')
    TYPE = use_image(path, 'type')
    AR = use_image(path, 'AR')
    RF = use_image(path, 'RF')
