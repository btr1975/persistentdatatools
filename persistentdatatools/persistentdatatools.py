#!/usr/bin/env python3
"""

Updated By: Benjamin P. Trachtenberg
Date Written 9/17/2015

Description:
Some quick tools to make persistent data quicker

"""
import logging
import csv as __csv
import os as __os
import re as __re
import random as __random
import string as __string
import zipfile as __zipfile

LOGGER = logging.getLogger(__name__)


def verify_file_exists(file_name, file_location):
    """
    Function to verify if a file exists

    :type file_name: String
    :param file_name: The name of file to check
    :type file_location: String
    :param file_location: The location of the file, derive from the os module

    :rtype: Boolean
    :return: returns boolean True or False

    """
    return __os.path.isfile(__os.path.join(file_location, file_name))


def file_name_increase(file_name, file_location):
    """
    Function to increase a filename by a number 1

    :type file_name: String
    :param file_name: The name of file to check
    :type file_location: String
    :param file_location: The location of the file, derive from the os module

    :rtype: String
    :return: a good filename.

    :raises Exception: If any errors happen

    """
    add_one = 1
    file_name_temp = file_name
    while verify_file_exists(file_name_temp, file_location):
        try:
            name, file_extension = file_name.split('.')
            file_name_temp = '%s-%i.%s' % (name, add_one, file_extension)
        except Exception as e:
            LOGGER.critical('Function file_name_increase Error {error} ignoring any errors'.format(error=e))
            name = file_name
            file_name_temp = '%s-%i' % (name, add_one)
        add_one += 1
    file_name = file_name_temp
    return file_name


def verify_directory(directory_name, directory_location, directory_create=False):
    """
    Function to verify if a directory exists

    :type directory_name: String
    :param directory_name: The name of directory to check
    :type directory_location: String
    :param directory_location: The location of the directory, derive from the os module
    :type directory_create: Boolean
    :param directory_create: If you want to create the directory

    :rtype: Boolean
    :return: Boolean True or False, but if you set directory_create to True it will create the directory

    """
    if not directory_create:
        return __os.path.exists(__os.path.join(directory_location, directory_name))
    elif directory_create:
        good = __os.path.exists(__os.path.join(directory_location, directory_name))
        if not good:
            __os.mkdir(__os.path.join(directory_location, directory_name))


def list_to_file(orig_list, file_name, file_location):
    """
    Function to export a list to a text file

    :type orig_list: List
    :param orig_list: The list you want exported
    :type file_name: String
    :param file_name: The name of the exported file
    :type file_location: String
    :param file_location: The location of the file, derive from the os module

    :rtype: String
    :return: Filename info

    """
    file = __os.path.join(file_location, file_name)

    def add_line_break(list_line):
        """
        Create a line break at the end of a string
        :param list_line: string

        :return:
            A string with a line break

        """
        list_line = ('%s\n' % (list_line,))
        return list_line
    write_file = open(file, "a")
    for orig_list_line in orig_list:
        write_file.write(add_line_break(str(orig_list_line)))
    write_file.close()
    return file_name


def file_to_list(file_name, file_location):
    """
    Function to import a text file to a list

    :type file_name: String
    :param file_name: The name of file to be import
    :type file_location: String
    :param file_location: The location of the file, derive from the os module

    :rtype: List
    :return: A list created from file data

    """
    file = __os.path.join(file_location, file_name)
    read_file = open(file, "r")
    temp_list = read_file.read().splitlines()
    read_file.close()
    return temp_list


def csv_to_dict(file_name, file_location):
    """
    Function to import a csv as a dictionary

    :type file_name: String
    :param file_name: The name of file to be import
    :type file_location: String
    :param file_location: The location of the file, derive from the os module

    :rtype: Dict
    :return: A dictionary

    """
    file = __os.path.join(file_location, file_name)
    try:
        csv_read = open(file, "r")
    except Exception as e:
        LOGGER.critical('Function csv_to_dict Error {error} ignoring any errors'.format(error=e))
        print('Error {error} ignoring any errors'.format(error=e))
        csv_read = open(file, "r", errors='ignore')
    data_row = __csv.DictReader(csv_read, dialect="excel")
    dict_key = 1
    temp_dict = dict()
    for row in data_row:
        temp_dict[dict_key] = row
        dict_key += 1
    csv_read.close()
    return temp_dict


def dict_to_csv(orig_dict, file_name, field_names_tuple, file_location):
    """
    Function to export a dictionary to a csv file

    :type orig_dict: Dict
    :param orig_dict: The dictionary you want exported
    :type file_name: String
    :param file_name: The name of the exported file
    :type field_names_tuple: Tuple
    :param field_names_tuple: The fieldnames in a tuple
    :type file_location: String
    :param file_location: The location of the file, derive from the os module

    :rtype: String
    :return: Filename info

    """
    file = __os.path.join(file_location, file_name)
    csv_write = open(file, 'a')
    writer = __csv.DictWriter(csv_write, fieldnames=field_names_tuple, lineterminator='\n')
    headers = dict((n, n) for n in field_names_tuple)
    writer.writerow(headers)
    for dict_key, a in list(orig_dict.items()):
        writer.writerow(orig_dict[dict_key])
    csv_write.close()
    return file_name


def remove_spaces(string_item):
    """
    Remove all spaces from a string

    :type string_item: String
    :param string_item: String that you want to remove spaces from

    :rtype: String
    :return: Corrected string without any spaces

    """
    string_item = ''.join(string_item.split())
    return string_item


def remove_spaces_add_hyphen(string_item):
    """
    Remove all spaces from a string and replace them with a hyphen

    :type string_item: String
    :param string_item: String that you want to remove hyphens from

    :rtype: String
    :return: Corrected string without any hyphens

    """
    string_item = '-'.join(string_item.split())
    return string_item


def remove_extra_spaces(string_item):
    """
    Remove all extra spaces from a string leaving single spaces

    :type string_item: String
    :param string_item: String that you want to remove spaces from

    :rtype: String
    :return: Corrected string without any extra spaces

    """
    string_item = ' '.join(string_item.split())
    return string_item


def remove_symbol_add_symbol(string_item, remove_symbol, add_symbol):
    """
    Remove a symbol from a string, and replace it with a different one

    :type string_item: String
    :param string_item: String that you want to replace symbols in
    :type remove_symbol: String
    :param remove_symbol: Symbol to remove
    :type add_symbol: String
    :param add_symbol: Symbol to add

    :rtype: String
    :return: Corrected string with symbols swapped

    """
    string_item = add_symbol.join(string_item.split(remove_symbol))
    return string_item


def list_files_in_directory(full_directory_path):
    """
    List the files in a specified directory

    :type full_directory_path: String
    :param full_directory_path: The full directory path to check, derive from the os module

    :rtype: List
    :return: A list of files

    """
    files = list()
    for file_name in __os.listdir(full_directory_path):
        if __os.path.isfile(__os.path.join(full_directory_path, file_name)):
            files.append(file_name)
    return files


def list_directories_in_directory(full_directory_path):
    """
    List the directories in a specified directory

    :type full_directory_path: String
    :param full_directory_path: The full directory path to check, derive from the os module

    :rtype: List
    :return: A list of directories

    """
    directories = list()
    for directory_name in __os.listdir(full_directory_path):
        if __os.path.isdir(__os.path.join(full_directory_path, directory_name)):
            directories.append(directory_name)
    return directories


def split_string_retain_spaces(string):
    """
    Function to split a string, and retain spaces to rejoin

    :type string: String
    :param string: A String

    :rtype: List
    :return: A split string

    """
    return __re.split(r'(\s+)', string)


def join_split_string(split_string):
    """
    Function to join a split string

    :type split_string: List
    :param split_string: A Split String

    :rtype: String
    :return: A joined string

    """
    return ''.join(split_string)


def split_strings_in_list_retain_spaces(orig_list):
    """
    Function to split every line in a list, and retain spaces for a rejoin

    :type orig_list: List
    :param orig_list: Original list

    :rtype: List
    :return: A List with split lines

    """
    temp_list = list()
    for line in orig_list:
        line_split = __re.split(r'(\s+)', line)
        temp_list.append(line_split)

    return temp_list


def random_line_data(chars_per_line=80):
    """
    Function to create a line of a random string

    :type chars_per_line: Integer
    :param chars_per_line: An integer that says how many characters to return

    :rtype: String
    :return: A String

    """
    return ''.join(__random.choice(__string.ascii_letters) for x in range(chars_per_line))


def random_data(line_count=1, chars_per_line=80):
    """
    Function to creates lines of random string data

    :type line_count: Integer
    :param line_count: An integer that says how many lines to return
    :type chars_per_line: Integer
    :param chars_per_line: An integer that says how many characters per line to return

    :rtype: String
    :return: A String

    """
    divide_lines = chars_per_line * line_count
    return '\n'.join(random_line_data(chars_per_line) for x in range(int(divide_lines / chars_per_line)))


def collect_and_zip_files(dir_list, output_dir, zip_file_name, file_extension_list=None, file_name_list=None):
    """
    Function to collect files and make a zip file

    :type dir_list: List
    :param dir_list: A list of directories
    :type output_dir: String
    :param output_dir: The output directory
    :type zip_file_name: String
    :param zip_file_name: Zip file name
    :type file_extension_list: List
    :param file_extension_list: A list of extensions of files to find
    :type file_name_list: List
    :param file_name_list: A list of file names to find

    :rtype: None
    :return: None Outputs a zip file

    Note: If no file_extension_list and file_name_list are provided it will zip the entire directory.

    """
    temp_list = list()

    if isinstance(dir_list, list):
        for dir_name in dir_list:
            if not __os.path.isdir(dir_name):
                error = 'Function collect_and_zip_files received an item that is not a directory {}'.format(dir_name)
                LOGGER.critical(error)
                raise Exception(error)

    else:
        error = 'Function collect_and_zip_files expected dir_list to be a list but received a {}'.format(type(dir_list))
        LOGGER.critical(error)
        raise TypeError(error)

    if not file_extension_list and not file_name_list:
        for dir_name in dir_list:
            temp_files_list = list_files_in_directory(dir_name)
            for file_name in temp_files_list:
                temp_list.append(__os.path.join(dir_name, file_name))

    if file_extension_list:
        if isinstance(file_extension_list, list):
            for dir_name in dir_list:
                temp_files_list = list_files_in_directory(dir_name)
                for file_name in temp_files_list:
                    garbage, extension = file_name.split('.')
                    if extension in file_extension_list:
                        temp_list.append(__os.path.join(dir_name, file_name))

        else:
            error = 'Function collect_and_zip_files expected file_extension_list to be a ' \
                    'list but received a {}'.format(type(file_extension_list))
            LOGGER.critical(error)
            raise TypeError(error)

    if file_name_list:
        if isinstance(file_name_list, list):
            for dir_name in dir_list:
                temp_files_list = list_files_in_directory(dir_name)
                for file_name in temp_files_list:
                    if file_name in file_name_list:
                        temp_list.append(__os.path.join(dir_name, file_name))

        else:
            error = 'Function collect_and_zip_files expected file_name_list to be a list but ' \
                    'received a {}'.format(type(file_name_list))
            LOGGER.critical(error)
            raise TypeError(error)

    if len(zip_file_name.split('.')) == 2:
        name, ext = zip_file_name.split('.')
        if ext != 'zip':
            LOGGER.warning('Changed the extension of zip_file_name={} to be zip'.format(zip_file_name))
            zip_file_name = '{}.{}'.format(name, 'zip')

    else:
        error = 'Function collect_and_zip_files expected zip_file_name to only contain one . ' \
                'but received {}'.format(zip_file_name)
        LOGGER.critical(error)
        raise NameError(error)

    with __zipfile.ZipFile(__os.path.join(output_dir, zip_file_name), 'a') as the_zip_file:
        for file in temp_list:
            the_zip_file.write(file)

    the_zip_file.close()
