#!/usr/bin/python3

''' Make a PDF using images. '''

import os
from fpdf import FPDF

images_loc = str(input('Path of the target folder: '))
CONVERT = ''
MULTIPLE_FOLDERS = ''
desired_name_pdf = str(input('Desired name of the PDF file: '))
list_subfolders = []
LIST_IMAGES = []
desired_answers = ['y', 'n']

def chdir():
    os.chdir(images_loc)

def need_to_convert():
    global CONVERT
    prompt = str(input('Do you need to convert the images? (y/n): '))
    if prompt not in desired_answers:
        print('Please only type y or n.\n')
        need_to_convert()
    else:
        CONVERT = prompt
        convert_images()

def if_multiple_folders():
    global MULTIPLE_FOLDERS
    prompt = str(input('Are there multiple folders inside the given path? (y/n): '))
    if prompt not in desired_answers:
        print('Please only type y or n.\n')
        if_multiple_folders()
    else:
        MULTIPLE_FOLDERS = prompt

def convert_images():
    if CONVERT == 'y':
        global MULTIPLE_FOLDERS
        for folder in os.listdir():
            if MULTIPLE_FOLDERS != 'n':
                os.chdir(f'{images_loc}/{folder}')
                for image in os.listdir():
                    path = f'ffmpeg -y -i {os.path.join(images_loc, folder, image)} {os.path.join(images_loc, folder, image[:-4])}.jpg'
                    print(f'Converting {image}')
                    os.system(f'{path} >/dev/null 2>&1') # >/dev/null 2>&1 is to hide shell.
            else:
                path = f'ffmpeg -y -i {os.path.join(images_loc, folder)} {os.path.join(images_loc, folder[:-4])}.jpg' 
                print(f'Converting {folder}')
                os.system(f'{path} >/dev/null 2>&1',)
    chdir()

def append_path():
    global LIST_IMAGES
    for folder in os.listdir():
        if MULTIPLE_FOLDERS == 'y':
            os.chdir(f'{images_loc}/{folder}')
            for image in os.listdir():
                if image.find('jpg') != -1:
                    LIST_IMAGES.append(f'{os.getcwd()}/{image}')
        else:
            if folder.find('jpg') != -1:
                LIST_IMAGES.append(f'{os.getcwd()}/{folder}')

    chdir()

    LIST_IMAGES = sorted(LIST_IMAGES)

def make_pdf():
    pdf = FPDF()

    for image in LIST_IMAGES:
        page = pdf.add_page()
        pdf.image(image, 0,0,210,297) # A4 size page
        
    print('Working...')
        
    pdf.output(f'{images_loc}/{desired_name_pdf}.pdf')
    
    print('The PDF file has been generated successfully.')

def ask_questions():
    if_multiple_folders()
    need_to_convert()

if __name__ == "__main__":
    chdir()
    ask_questions()
    append_path()
    make_pdf()
