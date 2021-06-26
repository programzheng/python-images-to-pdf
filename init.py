import os

OUTPUT_FOLDER = 'output'

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print('created folder: ', OUTPUT_FOLDER)