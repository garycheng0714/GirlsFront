import atx
import os
import constant
from common_flow import CommonFlow
from image import Image


class Restore:
    def __init__(self):
        self.working_dir = constant.RESTORE_DIR
        self.image_dir = constant.RESTORE_IMAGE_FOLDER_NAME

    def check(self, device):
        Image(os.path.join(self.image_dir, constant.RESTORE_ICON)).wait_image(device)

        coordinate_range = (740, 120, 780, 150)
        signal = Image(os.path.join(self.image_dir, constant.RESTORE_SIGNAL))
        check_region = device.region(atx.Bounds(*coordinate_range))
        result = check_region.match(signal.name)

        if result and result.matched:
            restore_flow = CommonFlow(self.working_dir, self.image_dir, constant.RESTORE_XLSX)
            restore_flow.run(device)
        else:
            print("No need to restore")
