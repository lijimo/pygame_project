import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

ASSET_DIR = 'assets'
print('directory:')
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png'] 
print(ASSET_FILES)
# check if there are all required tiles
print(len(ASSET_FILES))
assert len(ASSET_FILES) == 8

