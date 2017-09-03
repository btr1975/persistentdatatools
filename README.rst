Python Script: persistentdatatools
==================================

Written By: Benjamin P. Trachtenberg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have any questions e-mail me
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contact Information: e\_ben\_75-python@yahoo.com
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LinkedIn: `Ben Trachtenberg <https://www.linkedin.com/in/ben-trachtenberg-3a78496>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker Hub: `Docker Hub <https://hub.docker.com/r/btr1975>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requirements
~~~~~~~~~~~~

-  Nothing Specific besides Python 3

Languages
~~~~~~~~~

-  Python

About
~~~~~

This is a library used to manipulate, and save data quickly. It is just
a bunch of shortcuts I use quite a bit to manipulate saved data.

Functions included in v2.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  list\_to\_file(orig\_list, file\_name, file\_location)
-  file\_to\_list(file\_name, file\_location)
-  csv\_to\_dict(file\_name, file\_location)
-  store\_object(file\_name, save\_key, file\_location,
   object\_to\_store=None)
-  retrieve\_object\_from\_file(file\_name, save\_key, file\_location)
-  delete\_object\_from\_file(file\_name, save\_key, file\_location)
-  verify\_key\_in\_shelve(file\_name, save\_key, file\_location)
-  remove\_spaces(string\_item)
-  remove\_spaces\_add\_hyphen(string\_item)
-  remove\_extra\_spaces(string\_item)
-  verify\_file\_exists(file\_name, file\_location)
-  verify\_directory(directory\_name, directory\_location,
   directory\_create=False)
-  file\_name\_increase(file\_name, file\_location)
-  dict\_to\_csv(orig\_dict, file\_name, field\_names\_tuple,
   file\_location)
-  remove\_symbol\_add\_symbol(string\_item, remove\_symbol,
   add\_symbol)
-  list\_files\_in\_directory(full\_directory\_path)

Functions added in v2.2.2
~~~~~~~~~~~~~~~~~~~~~~~~~

-  get\_keys\_from\_shelve(file\_name, file\_location)

Update to Functions in v2.2.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  retrieve\_object\_from\_file: Uses get to retrieve key now, will not
   throw exception if it doesn't exist

-  verify\_key\_in\_shelve: Uses get to retreive key now, will still
   return True, or False

Functions added in v2.2.5
~~~~~~~~~~~~~~~~~~~~~~~~~

-  split\_string\_retain\_spaces(string)
-  split\_strings\_in\_list\_retain\_spaces(orig\_list)
-  join\_split\_string(split\_string)

Functions added in v2.2.6
~~~~~~~~~~~~~~~~~~~~~~~~~

-  random\_line\_data(chars\_per\_line=80)
-  random\_data(line\_count=1, chars\_per\_line=80)
