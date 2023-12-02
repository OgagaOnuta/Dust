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
