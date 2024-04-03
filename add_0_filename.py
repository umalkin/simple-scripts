#!/usr/bin/python3

''' Add 0 at the beginning of each filename/s if the filename/s starts with 1-9. '''

import os

GIVEN_PATH = ''
ANSWER = ''
desired_answers = ['y', 'n']

def get_path():
    global GIVEN_PATH
    input_path = str(input('Path: '))

    if os.path.exists(input_path):
        GIVEN_PATH = input_path
    else:
        print('This folder doesn\'t exist. Try again.')
        get_path()

def ask():
    global ANSWER
    if_multiple_folders = str(input('Are there multiple folders inside?: '))

    if if_multiple_folders in desired_answers:
        # print(if_multiple_folders in desired_answers)
        ANSWER = if_multiple_folders
    else:
        print('Just answer y or n.')
        ask()

# def add_zero_job():
#     get_path()
#     ask()

#     for file in os.listdir(GIVEN_PATH):
#         if ANSWER == 'n':
#             temp = file
#             if len(file[:file.find('.')]) == 1:
#                 temp = f'0{file}'

#                 os.system(f'mv {os.path.join(GIVEN_PATH, file)} {os.path.join(GIVEN_PATH, temp)}')
#         else:
#             os.chdir(f'{GIVEN_PATH}/{file}')
#             for image in os.listdir():
#                 # print(image)
#                 full_path = f'{GIVEN_PATH}/{file}/{image}'
#                 path_without_name_image = f'{GIVEN_PATH}/{file}/'
#                 if len(image[:image.find('.')]) == 1:
#                     new_name = f'{path_without_name_image}0{image}'
#                     print(new_name)

#                     os.system(f'mv {full_path} {new_name}')

if __name__ == "__main__":
    get_path()
    ask()

for file in os.listdir(GIVEN_PATH):
    if ANSWER == 'n':
        temp = file
        if len(file[:file.find('.')]) == 1:
            temp = f'0{file}'

            os.system(f'mv {os.path.join(GIVEN_PATH, file)} {os.path.join(GIVEN_PATH, temp)}')
    else:
        os.chdir(f'{GIVEN_PATH}/{file}')
        for image in os.listdir():
            # print(image)
            full_path = f'{GIVEN_PATH}/{file}/{image}'
            path_without_name_image = f'{GIVEN_PATH}/{file}/'
            if len(image[:image.find('.')]) == 1:
                new_name = f'{path_without_name_image}0{image}'
                print(new_name)

                os.system(f'mv {full_path} {new_name}')
