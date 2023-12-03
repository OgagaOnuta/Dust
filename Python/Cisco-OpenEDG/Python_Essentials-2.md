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

### Section 4 - Python Package Installer (PIP)

## Module 2. STRINGS, STRING AND LIST METHODS, EXCEPTIONS

### Section 1 - Characters and Strings vs. Computers

### Section 2 - The nature of strings in Python

### Section 3 - String Methods

### Section 4 - String in action

### Section 5 - Four simple programs

### Section 6 - Errors, the programmer's daily bread

### Section 7 - The anatomy of exceptions

### Section 8 - Useful exceptions

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
