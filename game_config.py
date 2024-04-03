import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

ASSET_DIR = 'assets'
print('directory:')
print(os.listdir(ASSET_DIR))
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3].lower() == 'png'] 
# check if there are all required tiles
assert len(ASSET_FILES) == 8

