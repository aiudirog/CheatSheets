####################################################################
# BASIC TYPES
####################################################################
# Immutable types cannot be changed in place.
#  -All methods and functions return a new copy
# Mutable types can be changed in place.
#  -Most methods and functions will edit the existing object
#   and return a number or boolean or something.
# int = Integer, immutable
integer = 5
# bool = Boolean, immutable
boolean = False # Or True
# str = String, immutable
string = "This is a string"
# tuple = Tuple, immutable
tuple_ = (obj1, obj2, etc)
# list = List, mutable
list_ = [obj1, obj2, etc]
# dict = Dictionary , mutable
dict_ = {"obj1": obj1, "obj2": obj2, etc}


####################################################################
# LISTS
####################################################################
# Sorting
# Sort list in place as python sees fit.
list_.sort()
# Return sorted copy but you choose how what to sort by.
new_list = sorted(list_, key=some_funtion_that_takes_an_arg)
# Sort list by last character of string. See Lambda section.
new_list = sorted(list_, key=lamba x: x[-1])

# Generate a list in one line
sqaures = [x**2 for x in range(100)]


####################################################################
# DICTIONARIES
####################################################################
# Dictionaries map keys to values. Keys can be any object who's
#  class implements the __hash__ method (more details on __methods__()
#  in Classes).
# Standard dictionary:
dictionary = {
        # KEY: VALUE,
        "one": 1,
        "two": 2,
        2: "two",
    }
# Essentially, lists are simply dictionaries, only ever mapping integers to
# other values. This implies that I can get the value 1 by executing:
one = dictionary["one"]

# Iterating over dictionaries:
for key, value in dictionary.items():  # .iteritems() in python 2.X
    print(key, value)

for key in dictionary:
    print(key, dictionary[key])

# One can add a new key|value pair to a dictionary as such:
dictionary["three"] = 3

# Generate a dictionary in one line
squares = {x:x**2 for x in range(100)}


####################################################################
# FUNCTIONS
####################################################################
# Basic function
def function(arg1, arg2, etc, kwarg1=kwarg1_default, kwarg2=kwarg2_default, etc):
    # Do some stuff, can access outside variables, but variables
    # defined in here cannot be seen outside.
    pass  # Do nothing
    return optional_value # Return to calling code, bring back optional_value

# Function with list/dict of options
def unlimited_args_function(*args, **kwargs):
    # *args is a list of arguments given without names
    # **kwargs is a dict of given arguments by name
    return
# *list or *tuple unpacks the values into a function call. Must go as last arg.
# **dict unpacks names and values into a function call. Must go as last kwarg.

# Function which specifies types, does NOT make them required.
def typed_function(arg1: str, arg2: object, kwarg1=default: str) -> bool:
    def nested_function():
        # Functions and methods can be defined inside of other 
        # functions and methods.
        return False
    return True


####################################################################
# LAMBDAS
####################################################################
# Lambdas are anonymous functions. 

# This takes one argument and returns the square of it.
lambda x: x**2

# Very useful in places where functions can be passed in, like map and filter.
# Get squares of all values in a list
squares = map(lambda x: x**2, [1, 2, 3, 4])
# Get only even numbers
evens = filter(lambda x: x%2==0, [1, 2, 3, 4])


####################################################################
# CLASSES
####################################################################
class Class(parent1, parent2, etc):
    # Class attributes:
    #  mutable are shared between all class objects and class itself
    #  immutable are specific to each object and class
    class_attr = None

    # init is called when creating the class.
    def __init__(self):
        # self refers to current object.
        # Instance attributes, only accessible to current object.
        # Should only be defined in init.
        self.instance_attr = []

    def instance_method(self):
        # Method that can be called by Class.instance_method() or by
        # instance.instance_method() and has access to all attributes.
        pass

    @classmethod
    def class_method(cls):
        # Method that can be called by Class.class_method() but only
        # has access to class attributes via cls.class_attr.
        pass

    @staticmethod
    def static_method():
        # Method than can be called by Class.static_method() but has 
        # no need to access class or instance attributes.
        pass

    def abstract_method(self):
        # Method that is required to be overloaded by subclass.
        # ~See section on Error Handling.~
        raise NotImplementedError("Subclasses of Class must implement abstract_method()")

    # Cool trick, useful in Django, any functions defined above an attribute
    # are accessible in this scope for being passed to functions:
    some_field = Field(upload_to=instance_function)

    def __getattribute__(self, attr):
        # Function called when trying to access any attribute  or method of an object
        # Super calls the very first function with this name it finds in a parent class.
        # Classes are inherited and overwrite each other from right -> left,
        # so since both parent1 and parent2 have this function, parent1's will be called.
        super(Class, self).__getattribute__(attr)

    def __getattr__(self, attr):
        # Called by __getattribute__() when an attribute error is raised to look for
        # custom implementations.

    # There are many other __methods__() that can be overloaded. 
    # These can change how the class/objects handle being added, indexed[i], destroyed, etc.
    # Documentation here: https://docs.python.org/3/reference/datamodel.html#specialnames

    class NestedClass:
        # Classes can be defined inside of classes and functions also.
        pass

# Creating objects from a class are assigned like so.
# No need for a 'new' keyword like in Java
class_obj = Class()


####################################################################
# DJANGO
####################################################################

