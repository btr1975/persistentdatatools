Python Script: persistentdatatools
==================================

Current Version: 2.2.10
~~~~~~~~~~~~~~~~~~~~~~~

`Documentation <https://persistentdatatools.readthedocs.io/>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Written By: Benjamin P. Trachtenberg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have any questions e-mail me
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contact Information: e_ben_75-python@yahoo.com
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LinkedIn: `Ben Trachtenberg <https://www.linkedin.com/in/ben-trachtenberg-3a78496>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker Hub: `Docker Hub <https://hub.docker.com/r/btr1975>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyPi Page for `persistentdatatools <https://pypi.python.org/pypi/persistentdatatools>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requirements
~~~~~~~~~~~~

-  Nothing Specific besides Python 3

Installation
~~~~~~~~~~~~

-  From source “setup.py install”
-  From pip “pip install persistentdatatools”

Languages
~~~~~~~~~

-  Python

About
~~~~~

This is a library used to manipulate, and save data quickly. It is just
a bunch of shortcuts I use quite a bit to manipulate saved data.

Functions included in v2.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  list_to_file(orig_list, file_name, file_location)
-  file_to_list(file_name, file_location)
-  csv_to_dict(file_name, file_location)
-  store_object(file_name, save_key, file_location,
   object_to_store=None)
-  retrieve_object_from_file(file_name, save_key, file_location)
-  delete_object_from_file(file_name, save_key, file_location)
-  verify_key_in_shelve(file_name, save_key, file_location)
-  remove_spaces(string_item)
-  remove_spaces_add_hyphen(string_item)
-  remove_extra_spaces(string_item)
-  verify_file_exists(file_name, file_location)
-  verify_directory(directory_name, directory_location,
   directory_create=False)
-  file_name_increase(file_name, file_location)
-  dict_to_csv(orig_dict, file_name, field_names_tuple, file_location)
-  remove_symbol_add_symbol(string_item, remove_symbol, add_symbol)
-  list_files_in_directory(full_directory_path)

Functions added in v2.2.2
~~~~~~~~~~~~~~~~~~~~~~~~~

-  get_keys_from_shelve(file_name, file_location)

Update to Functions in v2.2.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  retrieve_object_from_file: Uses get to retrieve key now, will not
   throw exception if it doesn’t exist

-  verify_key_in_shelve: Uses get to retreive key now, will still return
   True, or False

Functions added in v2.2.5
~~~~~~~~~~~~~~~~~~~~~~~~~

-  split_string_retain_spaces(string)
-  split_strings_in_list_retain_spaces(orig_list)
-  join_split_string(split_string)

Functions added in v2.2.6
~~~~~~~~~~~~~~~~~~~~~~~~~

-  random_line_data(chars_per_line=80)
-  random_data(line_count=1, chars_per_line=80)
