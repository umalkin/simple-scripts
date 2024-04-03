#!/usr/bin/python3

''' To convert files using ffmpeg. '''
import os
import pathlib
# import subprocess

PATH_INPUT = ''
MULTIPLE_FOLDERS_INPUT = ''
desired_multiple_folders_input = ['y', 'n']
# convert_to = str(input('Desired file extension : '))
convert_to = 'jpg'


def ask_path():
    global PATH_INPUT

    PATH_INPUT = input(str('Path: '))

    try:
        os.listdir(PATH_INPUT)
    except FileNotFoundError:
        print('Folder not found.')
        ask_path()


def ask_multiple_folders():
    global MULTIPLE_FOLDERS_INPUT

    MULTIPLE_FOLDERS_INPUT = input(str('Are there multiple folders inside?: '))

    if MULTIPLE_FOLDERS_INPUT not in desired_multiple_folders_input:
        ask_multiple_folders()

    print(MULTIPLE_FOLDERS_INPUT)


def convert_file(path, filename, filename_no_ext):
    old_path = pathlib.Path(
        str((os.path.join(path, filename)).replace(' ', '\\ ')))
    new_path = pathlib.Path(
        str((os.path.join(path, filename_no_ext)).replace(' ', '\\ ')))
    filename_ext = str(file[file.find('.'):])

    if filename_ext != convert_to:
        change_name = f"ffmpeg -y -i {old_path} {new_path}.{convert_to}"

    # print(f'Converting {filename} to {filename_no_ext} from {path} folder.')

    os.system(change_name)

# def convert_job():
#     ask_path()
#     ask_multiple_folders()

#     for file in os.listdir(PATH_INPUT):
#         if MULTIPLE_FOLDERS_INPUT == 'n':
#             os.chdir(f"{PATH_INPUT}")
#             filename = str(file[:file.find('.')])

#             convert_file(PATH_INPUT, file, filename)
#         else:
#             os.chdir(f"{PATH_INPUT}/{file}")
#             for image in os.listdir():
#                 path = str(PATH_INPUT) + '/' + file + '/'
#                 filename = str(image[:image.find('.')])

#                 convert_file(path, image, filename)


if __name__ == "__main__":
    ask_path()
    ask_multiple_folders()

    for file in os.listdir(PATH_INPUT):
        if MULTIPLE_FOLDERS_INPUT == 'n':
            os.chdir(f"{PATH_INPUT}")
            filename = str(file[:file.find('.')])

            convert_file(PATH_INPUT, file, filename)
        else:
            os.chdir(f"{PATH_INPUT}/{file}")
            for image in os.listdir():
                path = str(PATH_INPUT) + '/' + file + '/'
                filename = str(image[:image.find('.')])

                convert_file(path, image, filename)
