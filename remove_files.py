#!/usr/bin/python3

import os
import pathlib
import subprocess

PATH_INPUT = ''
MULTIPLE_FOLDERS_INPUT = ''
REMOVE_ALL_CSS = ''
REMOVE_ALL_JS = ''
REMOVE_CERTAIN_FILES = ''
certain_files = ['rosspos', 'thor-', 'ad-modal','a.html', 'jail.', 'eskto', 'pando', 'listin', 'popup', 'pixel.', 'videop', '.js', '.svg']
yes_no = ['y', 'n']

def ask_path():
    global PATH_INPUT

    PATH_INPUT = input(str('Path: '))

    try:
        os.listdir(PATH_INPUT)
    except FileNotFoundError:
        print('Folder not found.')
        ask_path()

def ask_question(question):
    temp = input(str(f'{question}: '))

    if temp not in yes_no:
        ask_question(question)
    
    return temp

# def edit_names(path, filename):
#     new_path = pathlib.Path(
#         str((os.path.join(path, filename)).replace(' ', '\\ ')))

#     return new_path

def delete_js_files(path, filename):
    if file[-3:] == '.js':
        os.remove(f'{path}{filename}')

def delete_css_files(path, filename):
    if file[-4:] == '.css':
        os.remove(f'{path}{filename}')


def delete_certain_files(text, path, filename):
    if filename.find(text) != -1:
        print(f'{path}{filename}')
        subprocess.call(['rm', f'{path}{filename}'])
        # os.remove(f'{path}{filename}')

if __name__ == "__main__":
    ask_path()
    MULTIPLE_FOLDERS_INPUT = ask_question('Are there multiple folders inside?')
    REMOVE_ALL_CSS = ask_question('Do you want to remove all CSS files?')
    REMOVE_ALL_JS =  ask_question('Do you want to remove all JS files?')
    REMOVE_CERTAIN_FILES = ask_question('Do you want to remove certain files?')
    
    
    for file in PATH_INPUT:
        if MULTIPLE_FOLDERS_INPUT == 'n':
            os.chdir(f'{PATH_INPUT}')
            if REMOVE_ALL_JS == 'y':
                delete_js_files(f'{PATH_INPUT}/', file)
        else:
           main_path = f'{PATH_INPUT}{file}'
           try:
               for folder in os.listdir(main_path):
                   if os.path.isdir(f'{main_path}{folder}'):
                       for file in os.listdir(f'{main_path}{folder}'):
                        #    print(f'{main_path}{folder}/{file}')
                           for item in certain_files:
                               if REMOVE_ALL_JS == 'y':
                                   delete_js_files(f'{main_path}{folder}/', file)
                               if REMOVE_ALL_CSS == 'y':
                                   delete_css_files(f'{main_path}{folder}/', file)
                               if REMOVE_CERTAIN_FILES == 'y':
                                   delete_certain_files(item, f'{main_path}{folder}/', file)
           except FileNotFoundError:
               continue
            # if os.path.isdir(f'{PATH_INPUT}/{file}'):
            #     os.chdir(f'{PATH_INPUT}/{file}')
            #     for folder in os.listdir():
            #             if os.path.isdir(f'{PATH_INPUT}/{file}/{folder}'):
            #                 for file in os.listdir(folder):
            #                     print(f'{PATH_INPUT}/{folder}/{file}')
            #                     if REMOVE_ALL_JS == 'y':
            #                         delete_js_files(f'{PATH_INPUT}/{folder}', file)

            #                     if REMOVE_CERTAIN_FILES == 'y':
            #                         for item in certain_files:
            #                             delete_certain_files(item, f'{PATH_INPUT}/{folder}', file)
                                # print(os.curdir())
                                # delete_js_files(path=f'{PATH_INPUT}/{folder}')