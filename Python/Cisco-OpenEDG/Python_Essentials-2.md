# PYTHON ESSENTIALS 2

## Module 1. MODULES, PACKAGES, AND PIP

### Section 1 - Introduction to modules in Python

A real, wanted, and widely used code develops continuously, as both users'
demands and users' expectations develop in their own rhythms.

A **Module** is a file containing Python definitions and statements. This can
be later imported and used when necessary.

The handling of modules consists of two different issues:

* when you want to use an already existing module (the module's _user_)
* when you want to create a brand new module (the module's _supplier_)

A module is identified by its _name_.

A number of modules is delivered together with Python. All these modules, along
with the built-in functions, form the **Python standard library**. A special
sort of library where modules play the roles of books (we can even say that
folders play the roles of shelves).

Each module consists of entities (like a book consists of chapters). These
entities can be functions, variables, constants, classes, and objects.

To make a module usable, you must **import** it (like taking a book out of the
shelf). This is done by an instruction named `import`.

> **Note:** `import` is also a keyword.

The simplest way to import a particular module is to use the `import`
instruction as follow:

```py
import math

```

The clause contains:

* the `import` keyword
* the _name of the module_ which is subject to import

The instruction may be located anywhere in your code, but it must be placed
before the first use of any of the module's entities.

If you want to import more than one module, you can do it by repeating the
`import` clause _(preferred)_:

```py
import math
import sys

```

or by listing the modules after the `import` keyword:

```py
import math, sys

```

A **namespace** is a space (a non-physical context) in which some names exist
and the names don't conflict with each other (i.e., there are not two
different objects of the same name).

Inside a certain namespace, each name must remain unique.

If the module of a specified name _exists and is accessible_, Python imports
its contents, i.e., _all the names defined in the module become known_, but
they don't enter your code's namespace. This means that you can have your own
entities with the same names and they won't be affected by the import in any
way.

```py
import math

print(math.sin(math.pi/2))

```

To **qualify** an entity with the name of its original module, you put:

* the _name of the module_
* a _dot_
* the _name of the entity_

This form clearly indicates the namespace in which the name exists.

> **Note:** using this qualification is **compulsory** if a module has been
> imported by the `import` module instruction. It doesn't matter if any of the
> names from your code and from the module's namespace are in conflict or not.

In the second method, the `import`'s syntax precisely points out which module's
entity (or entities) are acceptable in the code:

```py
from math import pi

```

The instruction consists of the following elements:

* the `from` keyword
* the _name of the module_ to be (selectively) imported
* the `import` keyword
* the _name or list of names of the entity/entities_ which are being imported
  into the namespace

The instruction has this effect:

* the listed entities (and only those ones) are _imported from the indicated_
  _module_
* the names of the imported entities are _accessible without qualification_

> **Note:** no other entities are imported. Moreover, you cannot import
> additional entities using a qualification.

```py
from math import sin, pi

print(sin(pi/2))

```

> **Note:** using this selective import, the location of the statement in the
> source code determines which supersedes between entities in your code and
> imported entities.

```py
from math import sin, pi

print(sin(pi/2))  # OUTPUTS: 1.0

pi = 3.14


def sin(x):
    if (2 * x == pi):
        return (0.99999999)
    else:
        return (None)


print(sin(pi/2))  # OUTPUTS: 0.99999999

```

```py
pi = 3.14


def sin(x):
	if (2 * x == pi):
		return (0.99999999)
	else:
		return (None)


print(sin(pi/2))  # OUTPUTS: 0.99999999

from math import sin, pi

print(sin(pi/2))  # OUTPUTS: 1.0

```

In the third method, the `import`'s syntax is a more aggressive form of the
previously presented one:

```py
from module import *

```

Such an instruction _imports all entities from the indicated module_.

> Is it unsafe? Yes, it is - unless you know all the names provided by the
> module, _you may not be able to avoid name conflicts_.
>
> Try not to use it in regular code

If you use the `import` module variant, you can give it any name you like -
this is called **aliasing**.

Aliasing causes the module to be identified under a different name than the
original. Creating an alias is done together with importing the module, and
demands the following form of the `import` instruction:

```py
import module as alias

```

```py
import math as m

print(m.sin(m.pi/2))

```

> **Note:** after successful execution of an aliased import, the _original_
> _module name becomes inaccessible_ and must not be used.

In turn, you can make an alias for an entity when you use the
`from module import name` variant. As previously, the original (unaliased)
name becomes inaccessible.

```py
from module import name as alias

```

The phrase `name as alias` can be repeated, separated by commas:

```py
from math import pi as PI, sin as sine

print(sine(PI/2))

```

### Section 2 - Selected Python modules (math, random, platform)

The `dir()` function is able to reveal all the names provided through a
particular module. One condition to using this is that the module has to have
been imported as a whole (i.e., using the `import module` instruction -
`from module` is not enough).

The function returns an _alphabetically sorted list_ containing all entities'
names available in the module identified by a name passed to the function as an
 argument.

```py
dir(module)

```

> **Note:** if the module's name has been aliased, you must use the alias, not
> the original name.

```py
'''
Doesn't make much sense using dir() in a script
'''

import math

for name in dir(math):
    print(name, end="\t")

```

You can execute the function directly in the Python console to know the
entities it contains.

```py
>>> import math
>>> dir(math)

```

The `random` module delivers some mechanisms allowing you to operate with
_pseudorandom numbers_. Data produced by deterministic computers cannot be
random in any way.

A random number generator takes a value called a _seed_, treats it as an input
value, calculates a "random" number based on it and produces a
_new seed value_.

The most general function named `random()` _produces a float number `x` coming
from the range `(0.0, 1.0)`.

```py
from random import random

for i in range(5):
    print(random())
    
```

The `seed()` function is able to directly _set the generator's seed_.

* `seed()` - sets the seed with the current time
* `seed(int_value)` - sets the seed with the integer value `int_value`

```py
from random import random, seed

seed(0)

for i in range(5):
    print(random())

```

If you want integer random values, one of the following functions would fit
better:

* `randrange(stop)`
* `randrange(start, stop)`
* `randrange(start, stop, step)`
* `randint(left, right)` - `right` inclusive

These functions may produce repeating values even if the number of subsequent
invocations is not greater than the width of the specified range.

To check for uniqueness of drawn numbers:

* `choice(sequence)` - chooses a "random" element from the input sequence and
  returns it
* `sample(sequence, elements_to_choose)` - builds a list (a sample) consisting
  of the `elements_to_choose` element(s) "drawn" from the input sequence

> **Note:** the `elements_to_choose` must not be greater than the length of the
> input sequence.

```py
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

```

The `platform` module lets you access the underlying platform's data, i.e.,
hardware, operating system, and interpreter version information.

How to invoke the `platform()` function:
`platform(aliased = False, terse = False)`

* `aliased` -> when set to `True` (or any non-zero value), it may cause the
  function to present the alternative underlying names instead of the common
  ones
* `terse` -> when set to `True` (or any non-zero value), it may cause the
  function to present a briefer form of the result (if possible)

```py
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

```

The `machine()` function returns a string with the generic name of the
processor which runs your OS together with Python and your code.

```py
from platform import machine

print(machine())

```

The `processor()` function returns a string filled with the real processor name
(if possible).

```py
from platform import processor

print(processor())

```

The `system()` function returns the generic OS name as a string.

```py
from platform import system

print(system())

```

The `version()` function returns a string with the OS version.

```py
from platform import version

print(version())

```

If you need to know what version of Python is running your code, you can check
it using a number of dedicated functions - here are two of them:

* `python_implementation()` -> returns a string denoting the Python
  implementation (expect `CPython` here, unless you decide to use any
  non-canonical Python branch)
* `python_version_tuple()` -> returns a three-element tuple filled with:
    * the _major_ part of Python's version
    * the _minor_ part
    * the _patch_ level number

```py
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

```

### Section 3 - Modules and Packages

A module is a _kind of container filled with functions_. It's generally a good
idea not to mix functions with different application areas within one module.

A **package** is a way to group your _modules_. In the world of modules, a
package plays a similar role to a folder/directory in the world of files.

Upon import, a new subfolder is created named `__pycache__`. Inside the folder
is a file named `module.cpython-xy.pyc`, where `module` is the module's name,
`cpython` is the python implementation used to create the file, `xy` is the
python version, and `pyc` comes from the word _Python_ and _compiled_.

When Python imports a module for the first time, it _translates its contents_
_into a somewhat compiled shape_. Python is able to check if the module's
source file has been modified (the `pyc` file will be rebuilt) or not (the
`pyc` file may be run at once).

When a module is imported, its contents are _implicitly executed by Python_.

> **Note:** the _initialization takes place only once_, when the first import
> occurs, so the assignments done by the module aren't repeated unnecessarily.

Python also creates a variable called `__name__`. Each source file uses its
own, separate version of the variable - it isn't shared between modules.

We can say that:

* when you run a file directly, its `__name__` variable is set to`__main__`
* when a file is imported as a module, its `__name__` variable is set to the
  file's name (excluding `.py`)

If you write a module filled with a number of complex functions, you can use
the `__name__` variable to place a series of tests to check if the functions
work properly. These tests will be omitted when the code is imported as a
module.

A _convention_ used to name a variable as _personal/private_ is by preceding
the variable's name with `_` (one underscore) or `__` (two underscores).

The line starting with `#!` _instructs the OS how to execute the contents of_
_the file_ for _Unix_ and _Unix-like_ OSs (including _MacOS_).

A _string_ placed before any module instructions (including imports) is called
the _doc-string_, and should briefly explain the purpose and contents of the
module.

How Python searches for modules:

* There's a special variable (a list) storing all locations (directories)
  that are searched in order to find a module which has been requested by the
  `import` instruction.
* Python browses these folders in the order in which they are stored in the
  list - if the module cannot be found in any of these directories, the import
  fails.
* Otherwise, the first folder containing a module with the desired name will be
  taken into consideration (if any of the remaining directories contains a
  module of that name, it will be ignored).
* The variable is named `path`, and it's accessible through the `sys` module.

```py
import sys

for p in  sys.path:
    print(p)
    
```

If you want to convince Python to take into account a non-standard package's
directory, its name needs to be inserted/appended into/to the import directory
list stored in the `path` variable contained in the `sys` module.

Using a _relative path_ for the directory will work only if you run the file
from its home folder.

**Packages**, like _modules_, may require _initialization_. Python expects
there to be a file with a very unique name inside the package's folder:
`__init__.py`. The contents of the file are executed when any of the package's
modules is imported. If you don't want any special initializations, you can
leave the file empty, but you can't omit it.

> **Remember:** The presence of the `__init__.py` file finally makes up the
> package.
>
> **Note:** it's not only the _root_ directory that can contain the
> `__init__.py` file - you can put it inside any of its subdirectories
> (subpackages) too, if they need some special kind of initialization.

We can also use a _zipped directory_ as a package.

```py
path.append("..\\packages\\extrapack.zip")

```

### Section 4 - Python Package Installer (PIP)

Python was created as open-source software. To make the model work and evolve,
some additional tools should be provided, tools that help the creators to
publish, maintain, and take care of their code. These same tools should help
users to make use of the code.

To make this world go round, two basic entities have been established and kept
in motion:

* a centralized repository of all available software packages; and
* a tool allowing users to access the repository.

The repository is named **PyPI** _(Python Package Index)_, and it's maintained
by a workgroup named **Packaging Working Group**, a part of the Python
Software Foundation, whose main task is to support Python developers in
efficient code dissemination.

PWG website: <https://wiki.python.org/psf/PackagingWG>  
PyPI website: <https://pypi.org/>

PyPI is not the only existing Python repository, it's the most important
Python repo in the world. The PyPI repo is sometimes referred to as the
_Cheese Shop_. It's a reference to an old Monty Python's sketch of the same
name.

The tool used to access this repository is called **pip** _(pip installs_
_packages)_. It's a recursive acronym.

How to install pip:

* on MS Windows

    The MS Windows Python installer already contains _pip_. If the _PATH_
    variable is misconfigured, it may be unavailable. The easiest way to
    reconfigure the _PATH_ variable is to reinstall Python, instructing the
    installer to set it for you. Run the command below to confirm:

    ```sh-session
    pip --version
    ```

* on Linux

    Run the below to command to check if available:

    ```sh-session
    pip3 --version
    ```

    Run the below command to install (depending on your distribution):

    ```sh-session
    sudo apt install python3-pip
    ```

* On Mac

    If you installed Python 3 using the _brew_ installer, _pip_ is already
    present in your system. Run the below command to confirm:

    ```sh-session
    pip3 --version
    ```

**Dependency** is a phenomenon that appears every time you're going to use a
piece of software that relies on other software.

> Note that dependency may include (and generally does include) more than one
> level of software development.

_pip_ can discover, identify, and resolve all dependencies.

`pip help` or `pip3 help` tells us what _pip_ can do for us. If you want to
know more about any of the listed operations, you can run the
`pip help operation` command, e.g., `pip help install`.

To know what Python packages have been installed, run the `pip list` command.
To know more about any of the installed packages, run the command
`pip show package_name`, e.g., `pip show pip`.

_pip_ is not able to store all PyPI content locally, you would have to have a
network connection whenever you're going to ask _pip_ for anything that may
involve direct interactions with the PyPI infrastructure.

Run `pip search anystring` to browse PyPI content via the console.  
Check <https://pypi.org/search> to browse PyPI content on the web.

`pip install package` installs the package system-wide.  
`pip install --user package` installs the package for only the specified
user.  
`pip install -U package_name` to update a package. You can also make use of the
`--user` option.  
`pip install package_name==package_version` to install a user-selected
version.  
`pip uninstall package_name` to uninstall a package.

Some sa that one of the most important programming virtues is _laziness_. A
_lazy programmer_ is a programmer who looks for existing solutions and
analyses the available code before they start to develop their own software
from scratch.

This is why _PyPI_ and _pip_ exist - use them!

## Module 2. STRINGS, STRING AND LIST METHODS, EXCEPTIONS

### Section 1 - Characters and Strings vs. Computers

Computers store characters as numbers. Every character used by a computer
corresponds to a unique number, and vice versa.

**ASCII** _(American Standard Code for Information Interchange)_  
**I18N** _(Internationalization, i.e., an I, 18 letters, then an N)_

A classic form of ASCII code uses eight bits for each sign. Eight bits mean
256 different characters. The first 128 are used for standard Latin alphabet.

A _code point_ is a number which corresponds to a character.  
A _code page_ is a standard for using the upper 128 code points to store
national characters.

To determine the meaning of a specific code point, you have to know the target
code page. The code points derived from the code page concept are ambiguous.

Code pages helped the computer industry to solve I18N issues for some time, but
was not a permanent solution. The concept that solved the problem in the long
term was _Unicode_.

**Unicode** assigns unique (unambiguous) characters to more than a million code
points.

The first 128 Unicode code points are identical to ASCII, and the first 256
Unicode code points are identical to the ISO/IEC 8859-1 code page (Western
European languages code page).

The Unicode standard says nothing about how to code and store the characters in
the memory and files. It only names all available characters and assigns them
to planes (a group of characters of similar origin, application, or nature).

There is more than one standard describing the techniques used to implement
Unicode in actual computers and computer storage systems. The most general of
them is **UCS-4** _(Universal Character Set)_.

UCS-4 uses 32 bits (four bytes) to store each character, and the code is just
the Unicode code points' unique number. UCS-4 increases a text's size by four
times compared to standard ASCII.

> 8 bits = 1 byte

A smarter form of encoding Unicode texts is **UTF-8** _(Unicode Transformation_
_Format)_. UTF-8 uses as many bits for each of the code points as it really
needs to represent them.

**BOM** _(Byte Order Mark)_ is a special combination of bits announcing
encoding used by a file's content.

Python 3 fully supports Unicode and UTF-8

* you can use Unicode/UTF-8 encoded characters to name variable and other
  entities;
* you can use them during all input and output.

This means that Python 3 is completely I18Ned.

### Section 2 - The nature of strings in Python

**Strings** are immutable sequences.

Strings can be represented on a line by starting and ending with a _single_
_apostrophe/quote_, and on multiple lines by starting and ending with
_three apostrophes/quotes_.

```py
single_line1 = 'string'
single_line2 = "string"

multi_line1 = '''Line #1
Line #2'''

multi_line2 = """Line #1
Line #2"""

```

Strings can be:

* concatenated (joined), using the `+` operator
* replicated, using the `*` operator

```py
str1 = "a"
str2 = "b"

print(str1 + str2)  # "ab"
print(str2 + str1)  # "ba"
print(5 * "a")  # "aaaaa"
print("b" * 4)  # "bbbb"

```

_Shortcut variants_ of the above operators are applicable for strings
(`+=` and `*=`).

The ability to use the same operator against completely different kinds of data
is called **overloading**.

To know a specific character's _ASCII/UNICODE code point value_, you use the
`ord()` function (as in _ordinal_).

To know the corresponding character of a _code point_, you use the `chr()`
function.

* To access any character in a string, you can do it using _indexing_.
* You can _iterate_ through strings.
* Strings can be sliced _i.e._, `sequence[start:stop:step]`.
* The `in` and `not in` operators works on strings.
* Characters in a string cannot be removed using the `del` instruction as it is
  an immutable sequence, but the list can be removed as a whole.
* The `index()` method searches the sequence from the beginning, and returns
  the _index of the first occurrence_ of the argument.
* The `count()` method counts all occurrences of the element inside the
  sequence.

### Section 3 - String Methods

Methods don't have to be invoked from within variables only. They can be
invoked directly from within string literals.

### Section 4 - String in action

Python strings can be compared using the same set of operators which are in use
in relation to numbers (`==`, `!=`, `>`, `>=`, `<`, `<=`). It compares the code
point values, character by character.

Two strings are equal when they consist of the same characters in the same
order. The final relation between strings is determined by comparing the first
different character in both strings.

String comparison is always case-sensitive (upper-case letters are taken as
lesser than lower-case ones).

Even if a string contains digits only, it's still not a number.

Comparing strings against numbers is generally a bad idea. The only comparisons
you can perform with impunity are these symbolized by the `==` and `!=`
operators. The former always gives `False`, while the latter always produces
`True`. Using any of the remaining comparison operators will raise a
`TypeError` exception.

Lists can be sorted in two ways. This also applies to lists containing strings.

* The function `sorted()` returns a new list with the elements sorted.
* The method `sort()` modifies the list itself.

Numbers can be converted to strings using the `str()` function. The reverse
transformation is possible only when the string represents a valid number, else
a `ValueError` exception is raised. The `int()` function converts to an integer
and the `float()` function converts to a float.

```py
s1 = "12.8"
i = int(s1)  # ValueError

s2 = "12"
f = float(s2)  # 12.0

```

### Section 5 - Four simple programs

```py
'''
Caesar Cipher (encryption)
Caesar Cipher (decryption)
Numbers Processor
IBAN Validator
'''

```

### Section 6 - Errors, the programmer's daily bread

You have to protect yourself from errors in order to be considered a good
programmer.

Each time your code tries to do something wrong/unenforceable, Python does two
things:

* it stops your program;
* it creates a special kind of data, called an _exception_.

Both of these activities are called _raising an exception_. Python always
raises an exception when it has no idea what to do with your code.

Python provides effective tools that allow you to _observe exceptions,_
_identify them and handle them_ efficiently. Potential exceptions have their
unambiguous names, so you can categorize them and react appropriately.

The word _try_ is the key to handling exceptions. It's a keyword.

The recipe for success is as follows:

* first, you have to _try to do something_;
* next, you have to _check whether everything went well_.

```py
# The code that always runs smoothly

try:
    # do something (risky code)
except (Exception_1):
    # fix an error
except (Exception_2):
    # fix another error
except (...):
    # ...
except (Exception):
    # fix any other error

# Back to normal

```

Note that:

* the `except` branches are searched in the same order in which they appear in
  the code
* you must not use more than one `except` branch with a certain exception name
* the number of different `except` branches is arbitrary - if you use `try`,
  you must put at lease one `except` branch after it
* the `except` keyword must no be used without a preceding `try`
* if any of the `except` branches is executed, no other branches will be
  visited
* if none of the specified `except` branches matches the raised exception, the
  exception remains unhandled
* if an unnamed `except` branch exists, it has to be specified as the last
* you cannot add more than one unnamed `except` branch after the named ones.

### Section 7 - The anatomy of exceptions

Python 3 defines 63 _built-in exceptions_, and all of them form a
_tree-shaped hierarchy_.

In summary:

* each exception raised falls into the first matching branch
* the matching branch doesn't have to specify the same exception - it's enough
  that the exception is more general (abstract) than the raised exception.

> **Remember:** don't put more general exceptions before more concrete ones,
> it will make the concrete ones unreachable and useless.

If you want to handle two or more exceptions in the same way, you can use the
following syntax, putting all the engaged exception names into a
comma-separated list and not forget the parentheses:

```py
try:
    pass
except (Exception_1, Exception_2):
    pass

```

If an exception is raised inside a function, it can be handled:

* inside the function
* outside the function

> **Note:** the _exception raised can cross function and module boundaries_,
> and travel through the invocation chain looking for a matching `except`
> clause able to handle it.

The `raise` instruction raises the specified exception named as if it was
raised in a normal (natural) way.

```py
raise exception

```

The instruction enables you to:

* simulate raising actual exceptions
* partially handle an exception and make another part of the code responsible
  for completing the handling.

You can use this instruction to test your exception handling routine without
forcing the code to do stupid things.

The `raise` instruction may also be utilized with the absence of the
exception's name:

```py
raise

```

There is one serious restriction: this kind of `raise` instruction may be used
_inside the `except` branch only_; using it in any other context causes an
error. The instruction will immediately re-raise the same exception as
currently handled.

How does `assert` work?

```py
assert expression

```

* it evaluates the expression
* if the expression evaluates to `True`, or a non-zero numerical value, or a
  non-empty string, or any other value different than `None`, it won't do
  anything else
* otherwise, it automatically and immediately raises an exception named
  `AssertionError` (in this case, we say that the assertion has failed)

Assertions don't supersede exceptions or validate the data, they are their
supplements.

### Section 8 - Useful exceptions

* `ArithmeticError`

    BaseException <- Exception <- ArithmeticError

* `AssertionError`

    BaseException <- Exception <- AssertionError

* `BaseException`

* `IndexError`

    BaseException <- Exception <- LookupError <- IndexError

* `KeyboardInterrupt`

    BaseException <- KeyboardInterrupt

* `LookupError`

    BaseException <- Exception <- LookupError

* `MemoryError`

    BaseException <- Exception <- MemoryError

* `OverflowError`

    BaseException <- Exception <- ArithmeticError <- OverflowError

* `ImportError`

    BaseException <- Exception <- StandardError <- ImportError

* `KeyError`

    BaseException <- Exception <- LookupError <- KeyError

## Module 3. OBJECT-ORIENTED PROGRAMMING

### Section 1 - The foundations of OOP

### Section 2 - A short journey from procedural to object approach

### Section 3 - OOP: Properties

### Section 4 - OOP: Methods

### Section 5 - OOP Fundamentals: Inheritance

### Section 6 - Exceptions once again

## Module 4. MISCELLANEOUS

### Section 1 - Generators, iterators, and closures

### Section 2 - Files (file streams, file processing, diagnosing stream problems)

### Section 3 - Working with real files

### Section 4 - The os module - interacting with the operating system

### Section 5 - The datetime module - working with time- and date-related functions

### Section 6 - the calendar module - working with calendar-related functions
