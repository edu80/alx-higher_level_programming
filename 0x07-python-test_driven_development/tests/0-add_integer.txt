``0-add_integer`` module test
=============================

Using ``add_integer`` function
-------------------------------

This text file contains test cases for the function ``add_integer``.
First import function to the varaible add_integer:
    
    >>> add_integer = __import__('0-add_integer').add_integer

Now use it:

Test_1 adding two integers
----------------------
    >>> add_integer(2, 1)
    3

Test_2 adding float with integer cast to the small int value
-------------------------------------------------------------
    >>> add_integer(3.2, 2)
    5

Test_3 adding int with str
--------------------------
    >>> add_integer("3", 4)
    Traceback (most recent call last):
    TypeError: a must be an integer

Test_4 adding str with int
--------------------------
    >>> add_integer(3, "4")
    Traceback (most recent call last):
    TypeError: b must be an integer

Test_5 adding None with int
--------------------------
    >>> add_integer(None, 4)
    Traceback (most recent call last):
    TypeError: a must be an integer

Test_6 adding just first parameter as None
------------------------------------------
    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer

Test_7 adding negative numbers
-------------------------------
    >>> add_integer(-3, -4)
    -7

Test_8 adding negative float numbers
-------------------------------------
    >>> add_integer(-3.4, -4.6)
    -7

Test_9 second argument as None
-------------------------------------
    >>> add_integer(-3.4, None)
    Traceback (most recent call last):
    TypeError: b must be an integer

Test_10 both arguments as strings
-------------------------------------
    >>> add_integer("-3.4", "3")
    Traceback (most recent call last):
    TypeError: a must be an integer

Test_11 more than two arguments
------------------------------------
 >>> add_integer(3, 234, 65)
    Traceback (most recent call last):
    TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given

Test_12 No arguments
--------------------------------
    >>> add_integer()
    Traceback (most recent call last):
    TypeError: add_integer() missing 1 required positional argument: 'a'

Test_13 first argument as string
--------------------------------
   >>> add_integer("heloo")
    Traceback (most recent call last):
    TypeError: a must be an integer
