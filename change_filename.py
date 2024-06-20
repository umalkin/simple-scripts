#!/usr/bin/python3

''' Edit the name of the file/s. '''

import os
import string
import re

GIVEN_PATH = ''
POSSIBLE_ANSWERS_TASK = ['1', '2', '3', '4', '5', '6']
POSSIBLE_ANSWERS_MULTIPLE_FOLDERS = ['y', 'n']
ANSWER_TASK = ''
ANSWER_MULTIPLE_FOLDERS = ''
CHARS_REMOVE = ''
CHARS_REPLACE = ''

def get_path():
    global GIVEN_PATH
    given_path = str(input('Path: '))

    if os.path.exists(given_path):
        GIVEN_PATH = given_path
    else:
        print('This folder doesn\'t exist. Try again.')
        get_path()

def ask_if_mulitple_folders():
    global ANSWER_MULTIPLE_FOLDERS
    get_path()
    if_multiple = str(input('Are there multiple folders inside?: '))
    if if_multiple in POSSIBLE_ANSWERS_MULTIPLE_FOLDERS:
        ANSWER_MULTIPLE_FOLDERS = if_multiple
        print(ANSWER_MULTIPLE_FOLDERS)
    else:
        ask_if_mulitple_folders()

def rename_main(path, old_name, new_name):

    os.rename(os.path.join(path, old_name), os.path.join(path, new_name))

def remove_spaces(path):
    for file in os.listdir(path):
        old_name = str(file)
        new_name = ''

        if file.find('.py') != -1:
            pass
        else:
            for char in old_name:
                if char != ' ':
                    new_name += char

        print(f'Will change the name from {old_name} to {new_name}.')

        os.rename(f'{path}/{old_name}', f'{path}/{new_name}')

def remove_chars(path, filename): # Will only leave letters, digits, and dot
    strr = str(string.ascii_letters + '.' + string.digits)
    new_name = ''

    for char in str(filename):
        if char in strr:
            new_name += char

    print(f'Will change the name from {filename} to {new_name}.')
    os.rename(os.path.join(path, filename), os.path.join(path, new_name))

def change_chars(path, filename, chars_to_remove, chars_to_replace):
    if filename.find(chars_to_remove) != -1:
        new_name = filename.replace(chars_to_remove, chars_to_replace)
        print(f'Will change the name from {filename} to {new_name}.')

        os.rename(f'{path}/{filename}', f'{path}/{new_name}')
        print(new_name)

def remove_unnecessary_chars_beginning(path):
    for file in os.listdir(path):
        old_name = str(file)
        to_remove_chars = re.search('[a-z0-9]+_[0-9]+_', old_name)
        new_name = ''

        if file.find('.py') != -1:
            pass
        else:
            if to_remove_chars:
                new_name = old_name.replace(to_remove_chars.group(0), '')

                print(f'Will change the name from {old_name} to {new_name}.')
                os.rename(f'{path}/{old_name}', f'{path}/{new_name}')

def remove_unnecessary_chars_ending(path):
    for file in os.listdir(path):
        old_name = str(file)
        to_remove_chars = re.search('-[a-z0-9]+', old_name)
        new_name = ''

        if file.find('.py') != -1:
            pass
        else:
            if to_remove_chars:
                new_name = old_name.replace(to_remove_chars.group(0), '')
                
                print(f'Will change the name from {old_name} to {new_name}.')
                os.rename(f'{path}/{old_name}', f'{path}/{new_name}')

def rename_to_ascending(path, filename):
    temp = filename.split('-')

    if temp[-1].find('.') != 0: # Get file extension
        temp[-1] = f".{temp[-1].split('.')[1]}"

    if len(temp[0]) == 1:
        temp[0] = f'0{temp[0]}'
            
    new_name = f'{temp[0]}{temp[-1]}'
                
    print(f'Will change the name from {filename} to {new_name}.')

    os.rename(f'{path}/{filename}', f'{path}/{new_name}')

def ask_question():   
    global ANSWER, CHARS_REMOVE, CHARS_REPLACE
    answer = input(str('''What do you want to do?
    1 - Remove the characters, excluding English letters and dot
    2 - Change the character/s
    3 - Remove the unnecessary character/s BEFORE the no. order
    4 - Remove the unnecessary character/s AFTER the no. order, excluding order number and file ext.
    5 - Remove spaces
    6 - Trim the names from '1-xx' into '1' :\n'''))

    if answer not in POSSIBLE_ANSWERS_TASK:
        print('Your answer is not included in the choices. Try again.\n')
        ask_question()
    else:
        ANSWER = answer
        if ANSWER == '2':
            CHARS_REMOVE = input(str('Character/s want to remove: '))
            CHARS_REPLACE = input(str('Character/s want to replace: '))
        
def final(path):
    list_paths = {} # {path:[files]}

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if ANSWER_MULTIPLE_FOLDERS == 'y':
            for child_folder in os.listdir(full_path):                
                if full_path in list_paths:
                    list_paths[full_path].append(child_folder)
                else:
                    list_paths[full_path] = []
                    list_paths[full_path].append(child_folder)
        else:
            if path in list_paths:
                list_paths[path].append(item)
            else:
                list_paths[path] = []
                list_paths[path].append(item)

    return list_paths

# 1 and 3 to 5 needs modification similar to 2 and 6.

if __name__ == "__main__":
    ask_if_mulitple_folders()
    ask_question()
    
    for key in final(GIVEN_PATH):
        for item in final(GIVEN_PATH)[key]:
            # print(f'{os.path.join(key, item)}')
            key = fr'{key}'
            print(key)
            if ANSWER == '5':
                remove_spaces(GIVEN_PATH)
            elif ANSWER == '4':
                remove_unnecessary_chars_ending(GIVEN_PATH)
            elif ANSWER == '3':
                remove_unnecessary_chars_beginning(GIVEN_PATH)
            elif ANSWER == '2':
                change_chars(key, item, CHARS_REMOVE, CHARS_REPLACE)
            elif ANSWER == '1':
                remove_chars(key, item)
            elif ANSWER == '6':
                rename_to_ascending(key, item)
