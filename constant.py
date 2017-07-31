import os

WORKING_DIR = os.path.dirname(__file__)

RESTORE_SIGNAL = 'restore_signal'
RESTORE_ICON = 'need_restore'
RESTORE_XLSX = 'restore.xlsx'
RESTORE_DIR = os.path.join(WORKING_DIR, 'restore')
RESTORE_IMAGE_FOLDER_NAME = os.path.join(RESTORE_DIR, 'image_restore')

BATTLE_STEPS_DIR = os.path.join(WORKING_DIR, 'battle_steps')
BATTLE_STEPS_IMAGE_FOLDER_NAME = os.path.join(BATTLE_STEPS_DIR, 'battle_common')

CLICK_SOMEWHERE_TO_WAIT = 'click_to_wait_image'
CLICK_OPTION_FIRST = 'option_click'
WAIT_SECONDS = 'wait_seconds'
WAIT_IMAGE_GONE = 'wait_image_gone'
WAIT_IMAGE = 'wait_image'
SWIPE = 'swipe'

BATTLE_DIR = os.path.join(WORKING_DIR, 'battle')
BATTLE_COMMON_IMAGE_DIR = os.path.join(BATTLE_DIR, 'common_image')
WARS_DIR = os.path.join(BATTLE_DIR, 'wars')

INVENTORY_DIR = os.path.join(WORKING_DIR, 'inventory')
INVENTORY_IMAGE_DIR = os.path.join(INVENTORY_DIR, 'image')
HIT_LIMIT_ICON = os.path.join(INVENTORY_IMAGE_DIR, 'hit_the_limit')

POWER_UP_DIR = os.path.join(INVENTORY_DIR, 'power_up')
POWER_UP_IMAGE_DIR = os.path.join(POWER_UP_DIR, 'image')
POWER_UP_GIRLS_DIR = os.path.join(POWER_UP_DIR, 'girls_to_power_up')

RETIRE_DIR = os.path.join(INVENTORY_DIR, 'retire')

GIRLS_IMAGE_DIR = os.path.join(POWER_UP_GIRLS_DIR, 'girls_inventory')

FORMATION_DIR = os.path.join(WORKING_DIR, 'formation')
FORMATION_IMAGE_DIR = os.path.join(FORMATION_DIR, 'image')
FORMATION_MAPPING_DIR = os.path.join(FORMATION_DIR, 'mapping')
FORMATION_AR_TYPE = 'AR'
FORMATION_RF_TYPE = 'RF'
