import xlrd, os, time, constant
from point import Point
from image import Image


class CommonFlow:
    def __init__(self, working_directory, image_directory, steps_filename):
        self.steps = StepList()
        self.working_directory = working_directory
        self.image_directory = image_directory
        self.steps_filename = os.path.join(self.working_directory, steps_filename)
        self.get_steps()

    def get_steps(self):
        first_sheet_index = 0
        with xlrd.open_workbook(self.steps_filename) as workbook:
            sheet = workbook.sheet_by_index(first_sheet_index)
            for row_idx in range(1, sheet.nrows):
                row_info = sheet.row_values(row_idx, start_colx=0, end_colx=sheet.ncols)
                self.add_step(row_info)

    def add_step(self, step_info):
        """
                step_info : [ 'combat', 'description'] or [ '35, 15', description] or ['step', 'note', 'option']
                step_container : self.prepare_steps or self.battle_steps
                
                get info from rows of excel file, store the info into list
                """
        if len(step_info) > 2:
            step, note, option_action, option = step_info
        else:
            step, note = step_info

        if ', ' in step:
            coordinate = map(int, step.split(', '))
            self.steps.append(Point(note, *coordinate))
        else:
            step = os.path.join(self.image_directory, step)
            if option_action:
                self.steps.append(Image(step, option_action, option))
            else:
                self.steps.append(Image(step))

    def run(self, device):
        cancel_button = Image(os.path.join(constant.BATTLE_COMMON_IMAGE_DIR, 'cancel_button'))
        for step in self.steps:
            if isinstance(step, Image):
                if step.option_action == constant.CLICK_SOMEWHERE_TO_WAIT:
                    step.click_somewhere_to_wait(device)
                elif step.option_action == constant.CLICK_OPTION_FIRST:
                    step.click_option_image_first(device)
                elif step.option_action == constant.WAIT_SECONDS:
                    step.click(device)
                    step.wait(step.option)
                elif step.option_action == constant.WAIT_IMAGE_GONE:
                    step.wait_image_gone(device)
                elif step.option_action == constant.WAIT_IMAGE:
                    step.wait_image(device)
                else:
                    step.click(device)
            else:
                if step.note == constant.SWIPE:
                    step.swipe(device)
                else:
                    step.click(device)
                    if 'location' in step.note and cancel_button.exists(device):
                        cancel_button.click(device)
            time.sleep(1)

    def show_steps(self):
        self.steps.show_steps()


class StepList(list):
    def show_steps(self):
        start_war_flag = 'start_war'
        for step in self:
            print(step)
            if start_war_flag in step.note:
                print("\nBattle")

if __name__ == '__main__':
    import atx
    device = atx.connect('4200c49cf2faa381')
    point = Point('location4', 534, 122)
    cancel_button = Image(os.path.join(constant.BATTLE_COMMON_IMAGE_DIR, 'cancel_button'))
    point.click(device)
    if 'location' in point.note and cancel_button.exists(device):
        cancel_button.click(device)
