#!/usr/bin/python3

import os
from PIL import Image

target_folder_name = str(input('Target folder name : '))
ask_if_with_taksbar = str(input('Does the images have taskabr? (y/n, default - y): '))
# dest_folder_name = str(input('Destined folder name : '))
with_taksbar = 'y'
images = os.listdir(target_folder_name)

def crop_images():
    counter = 0

    if 'cropped' not in os.listdir(target_folder_name):
        os.mkdir(f'{target_folder_name}/cropped')
    
    if ask_if_with_taksbar == 'y' or ask_if_with_taksbar == '':
        with_taksbar = 'y'
    else:
        with_taksbar = 'n'  

    for image in images:
        target_image = f'{target_folder_name}/{image}'
        img = Image.open(target_image)
        
        # name = f'cropped-{image}'
        name = f'{image}'
        height, width = img.size
            
            # For Images with Taskbar (YouTube SC Full Screen)
            
            # left = 70
            # top = 160
            # right = width*1.2
            # bottom = height-260
        cropped = ''
            
        print(f'Cropping {target_image}.')
            
        if with_taksbar == 'y':
            #cropped = img.crop((0, 50, width*1.3, height-255)) # For YouTube
            #cropped = img.crop((0, 50, width*1.3, height-355)) # For YouTube with max-width
            cropped = img.crop((0, 50, width*1.3, 525)) # For YouTube and this will also cut the bottom part
            # cropped = img.crop((70, 160, width*1.2, height-260)) # For Coursera
            cropped.save(f'{target_folder_name}/cropped/{name}')
            
        else:
            cropped = img.crop((0, 80, width*1.2, height-255))
            cropped.save(f'{target_folder_name}/cropped/{name}')
            
            #cropped = img.crop((70, 160, width*1.2, height-260)) # For Images with Taskbar.
            # cropped = img.crop((0, 80, width*1.2, height-255))
        cropped.save(f'{target_folder_name}/cropped/{name}')
            
        counter += 1
            
    print(f'Cropped {counter} images.')


if __name__ == "__main__":
    crop_images()
