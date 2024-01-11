# PYTHON ESSENTIALS 1

## Module 1. INTRODUCTION TO PYTHON AND COMPUTER PROGRAMMING

### Section 1 - Introduction to Programming

A **program** makes a computer usable.
A complete set of known commands is called an **INSTRUCTION LIST (IL)**.

We can say that each language consists of:

* an _alphabet_ (set of symbols)
* a _lexis_ (set of words AKA dictionary)
* a _syntax_ (set of rules)
* _semantics_ (set of rules determining if a certain phrase makes sense)

A program written in a high-level programming language is called a
**source code**. The file containing the source code is called the
**source file**.

There are two different ways of transforming a program from a high-level
programming language into a machine language:

1. _Compilation_ - the source program is translated once by getting a file
   containing the machine code. The program that performs this translation is
   called a _compiler_ or _translator_. The file can then be distributed as is.
2. _Interpretation_ - the source program can be translated each time it has
   to be run. The program performing this kind of transformation is called an
   _interpreter_. The file needs to be distributed with the interpreter. Each
   line is executed separately, _read-check-execute_.

**Python** is an _interpreted_ language.
Interpreted languages are often called _scripting languages_, while the source
programs encoded using them are called _scripts_.

### Section 2 - Introduction to Python

**Python** is named after an old BBC television comedy sketch series called
_Monty Python's Flying Circus_.
Python was created by _Guido van Rossum_.

_CPython_ is the traditional implementation of Python. An implementation of
Python refers to "a program or environment, which provides support for the
execution of programs written in the Python language, as represented by the
CPython reference implementation."

**PSF _(Python Software Foundation)_** is a community that aims to develop,
improve, expand, and popularize Python and its environment.
The _PSF's_ president is _Guido van Rossum_.

Python alternative implementations:

* CPython
* JPython
* PyPy
* MicroPython

### Section 3 - Downloading and Installing Python

Python 3 standard installation contains a very simple but extremely useful
application named IDLE (Integrated Development and Learning Environment).

## Module 2. PYTHON DATA TYPES, VARIABLES, OPERATORS, AND BASIC 1/O OPERATIONS

### Section 1 - The "Hello, World!" Program

The _function_ name along with the parentheses and argument(s) forms the
**function invocation** (`function_name(argument)`).
The process of calling a function is known as _function invocation/call_.
A function invocation is one of many possible kinds of _Python instruction_.

Computer programs are collections of instructions. An instruction is a command
to perform a specific task when executed.
Python requires that there cannot be more than one instruction in a line.

The backslash `\` is called the _escape character_ and has a very special
meaning when used inside strings. It is used to give a different meaning
to the character after it.

_Positional arguments_ are outputted based on their _position_.
_Keyword arguments_ are outputted based on the _keyword_ used to identify them
and _any keyword argument has to be put after the last positional argument_.
Arguments are separated with a comma `,`.

### Section 2 - Python literals

**Literals** are notations for representing some fixed values in code.
You use literals to encode data and to put them into your code.

_Integers_ are numbers without a decimal point. As of _Python 3.6_,
`11111111 == 11_111_111` OR `-11111111 == -11_111_111` for readability sake.

_Octal_ numbers are prefixed by _0O_/_0o_ (zero-o).
_Hexadecimal_ numbers are prefixed by _0X_/_0x_ (zero-x).
The `print()` function does the conversion from octal/hexadecimal to decimal
automatically.

_Floating-point_ numbers or _Floats_ are numbers with the decimal point.

For very large or very small numbers, you can use the _scientific notation_.
`300000000 == 3 * (10 ^ 8) == 3E8 == 3e8` where _e_ refers to exponent.
The _exponent_ (value after the _e_) has to be an integer.
The _base_ (value before the _e_) may be either an integer or a float.

_Strings_ are used to represent texts.
They need to be enclosed by either a quote (") or an apostrophe ('), but you
must be consistent. If you open a string with a quote, you must close with a
quote, if you start with an apostrophe, you must end with an apostrophe.
A string can be empty (`''` OR `""`).

_Boolean_ makes use of only two distinct values; `True` and `False`
(_case sensitive_), denoted as `1` and `0`.

The _None_ literal is used to represent the absence of a value.

### Section 3 - Operators - data manipulation tools

An _operator_ is a symbol that can operate on values.
_Data_ and _operators_ when connected form _expressions_.
A _unary_ operator is an operator with only one operand.
A _binary_ operator is an operator with two operands.

Below is a list of operators in Python:

* \+ => Addition
* \- => Subtraction
* \* => Multiplication
* / => Division (produces a float)
* // => Floor Division (produces an integer rounded down)
* % => Modulo
* ** => Exponentiation

Most of Python's operators have left-sided binding meaning that calculations
are conducted from left to right.
An exception is _the exponentiation operator which uses right-sided binding_.
_Sub-expressions in parentheses_ are always calculated first.

The Hierarchy of Priorities (from highest to lowest)

| Priority | Operator |     |
| :------: | :------: | :-: |
| 1 | `~`, `+`, `-` | unary |
| 2 | `**` | |
| 3 | `*`, `/`, `//`, `%` | |
| 4 | `+`, `-` | binary |
| 5 | `<<`, `>>` | |
| 6 | `<`, `<=`, `>`, `>=` | |
| 7 | `==`, `!=` | |
| 8 | `&` | |
| 9 | `\|` | |
| 10 | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, `\|=`, `<<=`, `>>=` | |

### Section 4 - Variables

A _variable_ is a named location reserved to store values in the memory.
Python _variables_ have a _name_ and a _value_.

Rules for naming variables in Python:

* the name _must_ be composed of _uppercase or lowercase letters_, _digits_,
  and _underscore_
* the name _must_ begin with a _letter_ or _underscore_
* the name is _case-sensitive_
* the name _must not_ be a _Python keyword_

The above-listed rules also apply to _function names_.

**PEP 8 -- Style Guide for Python Code** naming convention for variables and
functions:

* names should be _lowercase with words separated by underscores_
* camelCase names should be used only in contexts where that's already the
  prevailing style to retain backward compatibility

`var = value`
The assignment operator `=` assigns the value of its right argument to the
left.

_Shortcut operators / Compound assignment operators_
=> `x = x * 2` is the same as `x *= 2`

### Section 5 - Comments

A _comment_ is a remark inserted into the program which is omitted at runtime.
In Python, a comment is a piece of text that begins with a `#` (hash) sign
and extends to the end of the line.
If you want to place a comment that spans multiple lines, you need to place
`#` in front of all the lines.
Good, responsible developers describe each important piece of code.
Variable names should be _self-commenting_, meaning they should be named
unambiguously.

### Section 6 - Interaction with the user

The `+` (plus) sign when applied to two strings becomes a _concatenation_
operator (`"string" + "string"`).
The `*` (asterisk) sign when applied to a string and number becomes a
_replication_ operator (`8 * "string"` OR `"string" * 3`). A number less than
or equal to zero produces an _empty string_.

## Module 3. BOOLEAN VALUES, CONDITIONAL EXECUTION, LOOPS, LISTS AND LIST PROCESSING, LOGICAL AND BITWISE OPERATIONS

### Section 1 - Making decisions in Python

Computers only know two kinds of answers to questions:

1. yes, this is true (`True` in Python)
2. no, this is false (`False` in Python)

**Comparison/Relational Operators**
_Comparison: equality operator_ `==` => Are two values equal?
_Equality: the equal to operator_ `==`
_Inequality: the not equal to operator_ `!=`
_Comparison Operator: greater than_ `>`
_Comparison Operator: greater than or equal to_ `>=`
_Comparison Operator: less than_ `<`
_Comparison Operator: less than or equal to_ `<=`

_Conditional Statements_ consists of:

* the `if` keyword
* one or more whitespace
* an expression evaluating to `True` or `False`
* a colon (:) followed by a newline
* an _indented_ set of instructions

The `if` conditional statement can have:

* an `elif` statement denoting _else if_ to represent another condition
* an _optional_ `else` statement to be executed if the initial condition(s) are
  not met
* nested `if`, `elif`, or `else` statement(s) to check other condition(s)
  within initial condition(s)

**Pseudocode** is a kind of notation that is not an actual programming language
but is formalized, concise, and readable.

Performing a certain part of the code more than once is called a _loop_.

### Section 2 - Loops in Python

The `while` loop:

while there is something to do
    do it

```py
while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    .
    .
    .
    instruction_n

```

The loop body should be able to change the condition's value because doing
a thing usually decreases the number of things to do, and also prevent an
_infinite loop_.

> **REMEMBER:** Don't feel obliged to code your programs in the shortest and
> most compact way. _Readability_ may be a more important factor. Keep your
> code ready for a new programmer.

You can use _triple quotes (''' OR """) to print strings on multiple lines in
order to make text easier to read, or create a special text-based design.

The `for` loop:

sometimes, it's more important to _count the "turns" of the loop_ than to check
the conditions.

```py
for i in range(100):
    # do_something()
    pass  # an empty instruction

```

Some things to note:

* the `for` keyword
* a control variable to count loop turns automatically
* the `in` keyword introducing a range of possible values being assigned
  to the control variable

The `range()` function syntax:

* `range(stop)`
    * stop: up to but not including the stop value
* `range(start, stop)`
    * start: the starting value with the default value of `0`
* `range(start, stop, step)`
    * step: the value added after every iteration with the default of `1`
* The set generated has to be sorted in ascending order.

Additions which don't improve the language's expressive power, but only
simplify the developer's work, are sometimes called
_syntactic candy_ or _syntactic sugar_.

`break`:

* exits the loop immediately
* unconditionally ends the loop's operation
* the program begins to execute the nearest instruction after the loop's body

`continue`:

* behaves as if the program has suddenly reached the end of the body
* the next turn is started and the condition expression is tested immediately

Loops may have the `else` branch too, like `if`s.
The loop's `else` branch is _always executed once_, regardless of whether the
loop has entered its body or not, or it has not been terminated by `break`.

### Section 3 - Logic and bit operations in Python

In the language of logic, a _conjunction_ (`and`) is a connection of conditions.
The fulfilment of the task depends on the conditions.
_Disjunction_ (`or`) depends on the fulfilment of at least one condition.

The `and` (_conjunction operator_) is a _binary operator_ with a
_priority that is lower_ than the one expressed by the _comparison operators_.

| Argument `A` | Argument `B` | `A and B` |
| :----------: | :----------: | :-------: |
| False        | False        | False     |
| False        | True         | False     |
| True         | False        | False     |
| True         | True         | True      |

The `or` (_disjunction operator_)  is a _binary operator_ with a
_lower priority than `and`_.

| Argument `A` | Argument `B` | `A or B` |
| :----------: | :----------: | :------: |
| False        | False        | False    |
| False        | True         | True     |
| True         | False        | True     |
| True         | True         | True     |

The `not` (_negation operator_) is a _unary operator_ performing a
_logical negation_. Its _priority is very high_, the same as the unary
`+` and `-`.

| Argument | `not` Argument |
| :------: | :------------: |
| False    | True           |
| True     | False          |

`and`, `or`, and `not` are called _logical operators_.

**De Morgan's laws**:

* _The **negation** of a **conjunction** is the **disjunction of the negations**._
    * `not (p and q) == (not p) or (not q)`
* _The **negation** of a **disjunction** is the **conjunction of the negations**._
    * `not (p or q) == (not p) and (not q)`

_None_ of these _logical operators_ can be used as _compound assignment operators_.

Logical operators take their arguments as a whole regardless of how many bits
they contain. The operators are aware only of the value:

* zero (when all the bits are reset) means `False`.
* not zero (when at least one bit is set) means `True`.

The result of their operations is one of these values: `False` or `True`.

_Bitwise operators_ allow you to _manipulate single bits of data_.
The arguments of these operators _must be integers_.

* `&` (ampersand) - _bitwise conjunction_
    * requires exactly two `1`s to provide `1` as the result
* `|` (bar) - _bitwise disjunction_
    * requires at least one `1` to provide `1` as the result
* `~` (tilde) - _bitwise negation_ (`~x` is usually `-x - 1` for _signed numbers_)
* `^` (caret) - _bitwise exclusive or (xor)_
    * requires exactly one `1` to provide `1` as the result

| Argument `A` | Argument `B` | `A & B` | `A \| B` | `A ^ B` |
| :----------: | :----------: | :-----: | :------: | :-----: |
| `0`          | `0`          | `0`     | `0`      | `0`     |
| `0`          | `1`          | `0`     | `1`      | `1`     |
| `1`          | `0`          | `0`     | `1`      | `1`     |
| `1`          | `1`          | `1`     | `1`      | `0`     |

| Argument | `~` Argument |
| :------: | :----------: |
| `0`      | `1`          |
| `1`      | `0`          |

Each of these _two-argument bitwise operators_ can be used as _compound operators_.

* `x = x & y` => `x &= y`
* `x = x | y` => `x |= y`
* `x = x ^ y` => `x ^= y`

A **bit mask** is a sequence of _zeros_ and _ones_, whose task is to grab the
value or to change the selected bits.

`flag_register = 0000000000000000000000000000x000`

1. Check the state of your bit

    ```py
    x & 1 = x
    x & 0 = 0

    flag_register = 00000000000000000000000000001000

    # 3 represents the location of the bit
    2**3 = 8
    the_mask = 8

    if flag_register & the_mask:
        # My bit is set.
    else:
        # My bit is reset.

    ```

2. Reset your bit: you assign a `0` to your bit

    ```py
    flag_register &= ~the_mask
    
    ```

3. Set your bit: you assign a `1` to your bit

    ```py
    x | 1 = 1
    x | 0 = x

    flag_register |= the_mask
    
    ```

4. Negate your bit

    ```py
    x ^ 1 = ~x
    x ^ 0 = x

    flag_register ^= the_mask
    
    ```

_Shifting_ applies to only _integer_ values.

* _Shifting_ a value one bit to the left corresponds to multiplying it by two.
    * `<<` represents _left shift_ (`value << bits`).
* _Shifting_ a value one bit to the right corresponds to dividing it by two.
    * `>>` represents _right shift_ (`value >> bits`).

The left argument is an integer value whose bits are shifted.
The right argument determines the size of the shift.
The priority of these operators is very high.

> Note:
>
> * `17 << 2`
>     * -> `17 * 4` (`17` multiplied by `2` to the power of `2`)
>     * -> `68` (shifting to the left by `2` bits is the same as integer
>     multiplication by `4`)
> * `17 >> 1`
>     * -> `17 // 2` (`17` floor-divided by `2` to the power of `1`)
>     * -> `8` (shifting to the right by `1` bit is the same as integer
>     division by `2`)

### Section 4 - Lists

Variables that are able to store exactly one given value are sometimes called
_scalars_ by analogy with mathematics.

The **List** is a _type of data_ in Python used to store multiple objects.
It is _ordered_ and _mutable_. Lists _begin with an open square bracket `[`_,
and _end with a closed square bracket `]`_, and the values in the brackets are
separated by _commas `,`_ (`numbers = [1, 2, 3, 4, 5]`).

You can also create a list using a Python built-in function called `list()`.

The _elements_ (values) inside a list may have different types including lists.
The elements in a list are always numbered starting from zero (0).

The _value_ inside the brackets `numbers[0]` which selects one element of the
list is called an _index_, while the _operation_ of selecting an element from
the list is known as _indexing_.

The `len()` function is used to check the _length_ of the list, that is how
many elements are present in the list.

```py
print(len(numbers))  # Outputs the number of elements in the list

```

The `del` instruction is used to remove/delete elements from a list, or even
the entire list.

```py
del numbers[1]  # Deletes the specified element from the list
del numbers  # Deletes the entire list

```

Negative indices are legal.

```py
numbers[-1]  # The last element
numbers[-2]  # The element before the last

```

A _method_ is a specific kind of function. It behaves like a function and looks
like a function, but differs in the way in which it acts, and its invocation
style. A method is able to change the state of a selected entity.

A function doesn't belong to any data. It gets data, it may create new data and
it (generally) produces a result.

A method is owned by the data it works for, while a function is owned by the
whole code.
This means that invoking a method requires some specification of the data from
which the method is invoked.

```py
result = function(arg)
result = data.method(arg)

```

The `append()` method takes an argument and puts it at the end of the list.

```py
list.append(value)

```

The `insert()` method can add a new element at any place in the list.

```py
list.insert(location, values)

```

You can start a list's life by making it empty. This is done with an empty pair
of square brackets.

```py
my_list = []

```

### Section 5 - Sorting simple lists: the bubble sort algorithm

The _bubble sort algorithm_ compares two adjacent elements, and swaps them if
the previous element is greater than the next element, thereby pushing
(bubbling) the higher elements to the top.

Python also has sufficient number of ready-to-use tools for sorting, one of
them being the `sort()` method.

```py
my_list = [8, 10, 6, 2, 4]
my_list.sort()

print(my_list)

```

The method `reverse()` can reverse the elements of a list.

```py
my_list = [5, 3, 1, 2, 4]
print(my_list)

my_list.reverse()
print(my_list)

```

### Section 6 - Operations on lists

The name of an ordinary variable is the _name of its content_.
The name of a list is the name of a _memory location where the list is stored_.

```py
list_1 = [1]

#  The two names below identify the same location in the computer memory
list_2 = list_1  # Copies the name of the array, not its contents
list_1[0] = 2  # Modifying one affects the other, and vice versa

print(list_2)  # Prints [2]

```

A _slice_ is an element of Python syntax that allows you to
_make a brand new copy of a list, or parts of a list_.
It copies the list's contents, not the list's name.

```py
list_1 = [1]
list_2 = list_1[:]  # Copies all the contents of list_1
list_1[0] = 2  # Modifying one doesn't affect the other

print(list_2)  # Prints [1]

```

One of the most general forms of the slice looks like `my_list[start:end]`.

* `start` is the index of the first element _included_ in the slice.
* `end` is the index of the first element _not included_ in the slice.
nnn
This creates a new list, taking elements from the `start` index to the
`end - 1` index, not including the `end` index.
_Negative values_ can also be used for both start and end index.

If the `start` specifies an element lying further than the one described by the
`end` (from the lists's beginning), the slice will be _empty_.

If you omit the `start` in your slice, it is assumed that you want to get a
slice beginning at the element with index `0`.

`my_list[:end]` is equivalent to `my_list[0:end]`.

If you omit the `end` in your slice, it is assumed that you want the slice to
end at the element with the index `len(my_list)`.

`my_list[start:]` is equivalent to `my_list[start:len(my_list)]`.

The `del` instruction can delete slices too.

The `in` operator checks if a given element (its left argument) is currently
stored somewhere inside the list (the right argument), and returns `True` if
that's the case.
The `not in` operator checks if a given element (its left argument) is absent
in a list (the right argument), and returns `True` if that's the case.

### Section 7 - Lists in advanced applications

**List Comprehension** is the special syntax used by Python in order to fill
massive lists. It is created on-the-fly during program execution, and is not
described statically.

```py
# List Comprehension syntax
[expression for element in list if conditional]

```

```py
# Filling the second row of the chessboard
row = [WHITE_PAWN for i in range(8)]

```

The part of the code placed inside the square brackets specifies:

* the data to be used to fill the list (`WHITE_PAWN`)
* the clause specifying how many times the data occurs inside the list
  (`for i in range(8)`)

**Two-dimensional arrays _(matrices)_**: If we want to create a list of lists
representing the whole chessboard, it may be done in the following way:

```py
# Creating an empty array
board = []

# EMPTY designates an empty field on the chessboard
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

```

As list comprehensions can be _nested_, we can shorten the board creation in
the following way:

```py
board = [[EMPTY for i in range(8)] for j in range(8)]

```

Access to the selected field of the board requires two indices;

* the first selects the row
* the second selects the field number inside the row (a column number)

To find any element of a two-dimensional list, you have to use two coordinates:

* a vertical one _(row number)_
* a horizontal one _(column number)_

For a _three-dimensional array_:

```py
'''
A hotel consisting of 3 buildings, 15 floors each with 20 rooms on each floor
'''

rooms = [[[False for rooms in range(20)] for floors in range(15)] for buildings in range(3)]

```

## Module 4. FUNCTIONS, TUPLES, DICTIONARIES, EXCEPTIONS, AND DATA PROCESSING

### Section 1 - Functions

A _function_ is a _block of code_ that performs a specific task when the
function is called (invoked).
Functions can have parameters and return values.

When to write your own functions:

* if a particular fragment of the code begins to appear in more than one place,
  consider the possibility of isolating it in the form of a function
* if a piece of code becomes so large that reading and understanding it may
  cause a problem, consider dividing it into separate smaller problems, and
  implementing each of them in the form of a separate function
* if you're going to divide the work among multiple programmers, decompose the
  problem to allow the product to be implemented as a set of separately written
  functions packed together in different modules.

Some say that a well-written function should be viewed entirely in one glance.

A good, attentive developer _divides the problem_ into well-isolated pieces,
and _encodes each of them in the form of a function_.

_Decomposition_ describes encoding and testing each piece of code separately.
Decomposition continues until you get a set of short functions, easy to
understand and test.

_Decomposition_ also involves _sharing the work and responsibility_ among
_a team of developers_.

In general, functions come from at least four places:

* from Python itself _(built-in functions)_
* from Python's _pre-installed modules_
* directly from your code _(user-defined functions)_
* the `lambda` functions

You need to _define_ functions

```py
def function_name(optional_parameters):
    function_body

```

* it always starts with the keyword `def` _(for define)_
* next after `def` goes the _name of the function_ (the rules for naming
  functions are exactly the same as for naming variables)
* after the function name, there's a pair of _parentheses_ `()`
* the line has to be ended with a _colon_ `:`
* the line directly after `def` begins the _function body_ - a couple (at least
  one) of necessarily _nested instructions_, which will be executed every time
  the function is invoked (_NOTE_: the function ends where the nesting ends)

```py
print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())

```

The repeated code in the above snippet can be converted to a function as below:

```py
def message():
    print("Enter a value: ")

message()
a = int(input())

message()
b = int(input())

message()
c = int(input())

```

Python reads the function's definitions and remembers them, but won't launch
any of them without your permission.

How functions work:

* when you _invoke_ a function, Python remembers the place where it happened
  and jumps into the invoked function
* the body of the function is then _executed_
* reaching the end of the function forces Python to _return_ to the place after
  the point of invocation

There are two, very important, catches:

* You mustn't invoke a function which is not known at the moment of invocation.
* You mustn't have a function and a variable of the same name.

You're free to _mix your code with functions_, you're not obliged to put all
your functions at the top of your source file.

### Section 2 - How functions communicate with their environment

A _parameter_ is a _variable_, but there are two important factors that make
parameters different and special:

* _parameters exist only inside functions in which they have been defined_,
  and the only place where the parameter can be defined is a space between a
  pair of parentheses in the `def` statement
* _assigning a value to the parameter is done at the time of the function's_
  _invocation_, by specifying the corresponding argument

```py
def function(parameter):
    pass
    
```

Don't forget:

* _**parameters** live inside functions_ (this is their natural environment)
* _**arguments** exist outside functions_, and are carriers of values passed to
  corresponding parameters

A value for the parameter will arrive from the function's environment.

> **Remember:** _specifying one or more parameters in a function's definition_
> is also a requirement, and you have to fulfil it during invocation.You must
> _provide as many arguments as there are defined parameters_.

It's legal, and possible, to have a _variable named the same as a function's_
_parameter_.

Shadowing:

* parameter `x` shadows any variable of the same name, but...
* ... only inside the function defining the parameter.

A function can have _as many parameters as you want_, but the more parameters
you have, the harder it is to memorize their roles and purposes.

A technique which assigns the _ith_ (first, second, and so on) argument to the
_ith_ (first, second, and so on) function parameter is called
**positional parameter passing**, while arguments passed in this way are named
**positional arguments**.

```py
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("David", "Onuta")

```

**Keyword argument passing** is where _the meaning of the argument is dictated_
_by its name_, not by its position.

```py
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

# The two statements below both outputs: Hello, my name is David Onuta
introduction(first_name = "David", last_name = "Onuta")
introduction(last_name = "Onuta", first_name = "David")

```

You _mustn't use a non-existent parameter name_.

You can mix both positional and keyword arguments, but you have to
_put positional arguments before keyword arguments_.

Parameters whose values are in use more often than others have their
_default (predefined) values_ taken into consideration when their corresponding
arguments have been omitted.

```py
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction("John", "Doe")  # Output: Hello, my name is John Doe
introduction("Henry")  # Output: Hello, my name is Henry Smith
introduction(first_name="William")  # Output: Hello, my name is William Smith

```

```py
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Valid invocations
introduction()  # Output: Hello, my name is John Smith
introduction(last_name="Hopkins")  # Output: Hello, my name is John Hopkins

```

### Section 3 - Returning a result from a function

To get _functions to return a value_ (but not only for this purpose) you use
the `return` instruction.
The `return` instruction has _two different variants_.

* `return` without an expression

    ```py
    def happy_new_year(wishes = True):
        print("Three...")
        print("Two...")
        print("One...")

        if (not wishes):
            return

        print("Happy New Year!")

  ```

  If the `return` instruction is encountered, it will cause the termination
  of the function.

* `return` with an expression

    ```py
    def function():
        return expression
        
    ```

    ```py
    def boring_function():
        return 123

    x = boring_function()

    print("The boring_function has returned its result. It's:", x)

    ```

    There are two consequences of using it:

    * it causes the _immediate termination of the function's execution_
    * the function will _evaluate the expression's value and will return it_
    _as the function's result_

> Don't forget:
>
> * you are always _allowed to ignore the function's result_, and be satisfied
>   with the function's effect (if any)
> * if a function is intended to return a useful result, it must contain the
>   second variant

`None`: its data doesn't represent any reasonable value, it's not a value at
all; hence, it _mustn't take part in any expressions_.
`None` is a **keyword**.

There are only two kinds of circumstances when `None` can be safely used:

* when you _assign it to a variable_ (or return it as a _function's result_)
* when you _compare it with a variable_ to diagnose its internal state.

```py
value = None

if (value is None):
    print("Sorry, you don't carry any value")

```

If a function doesn't return a certain value using a `return` expression
clause, it is assumed that it _implicitly returns `None`_.

```py
def strange_function(n):
    if (n % 2 == 0):
        return (True)

print(strange_function(2))  # returns: True
print(strange_function(1))  # returns: None

```

Any entity recognizable by Python can play the role of a _function argument_,
although it has to be assured that the function is able to cope with it.
Any entity recognizable by Python can be a _function result_.

### Section 4 - Scopes in Python

_The **scope of a name** (e.g., a variable name) is the part of a code where_
_the name is properly recognizable_.

```py
def scope_test():
    x = 123
    
    
scope_test()
print(x)

# Output:
# ERROR

```

```py
def my_function():
    print("Do I know that variable?", var)
    
    
var = 1

my_function()
print(var)

# Output:
# Do I know that variable? 1
# 1

```

A variable _existing inside_ a function has _scope_ inside the function body.
A variable _existing outside_ a function has _scope_ inside the function's
body, _excluding_ those which define a _variable of the same name_.
It also means that the _scope of a variable existing outside a function is_
_supported only when getting its value (reading)_.

Assigning a value forces the creation of the function's own variable.

```py
def my_function():
    var = 2

    print("Do I know that variable?", var)
    
    
var = 1

my_function()
print(var)

# Output:
# Do I know that variable? 2
# 1

```

There's a special Python method which can _extend a variable's scope in a way_
_which includes the function's body_ (even if you want not only to read the
values, but also to modify them).
Such an effect is caused by a keyword named `global`.

```py
global name
global name1, name2, ...

```

Using this keyword inside a function with the name (or names separated with
commas) of a variable (or variables), forces Python to refrain from creating
a new variable inside the function - the one accessible from outside will be
used instead.

In other words, this name becomes _global_ (it has _global scope_, and it
doesn't matter whether it's the subject of read or assign).

```py
def my_function():
    global var
    var = 2
    
    print("Do I know that variable?", var)


var = 1

my_function()
print(var)

# Output:
# Do I know that variable? 2
# 2

```

_Changing the parameter's value doesn't extend outside the function_.

A function receives the _argument's value_, not the argument itself (for
scalars).

If the argument is a list, then changing the value of the corresponding
parameter doesn't affect the list, but if you change a list identified by the
parameter, the list will reflect the change.

### Section 5 - Creating multi-parameter functions

It's worth checking if our parameters are always meaningful.

_Recursion_ is a technique where a function invokes itself.

A _Recursive Function_ is a function which calls itself and contains a
specified termination condition (i.e., _the base case_).

> **NOTE:** If you forget to consider the conditions which can stop the chain
> of recursive invocations, the program may enter an infinite loop.

Recursive calls consume a lot of memory, and may sometimes be inefficient.

### Section 6 - Tuples and dictionaries

A _**Sequence Type** is a type of data in Python which is able to store more_
_than one value (or less than one, as a sequence may be empty) and these_
_values can be sequentially (hence the name) browsed, element by element._

A _sequence_ is data which can be scanned by the `for` loop.

_**Mutability** is a property of any Python data that describes its readiness_
_to be freely changed during program execution._

There are two kinds of Python data:

* mutable _(data can be freely updated at any time)_
* immutable _(data cannot be modified)_

> _In situ_ is a _Latin phrase_ that translates as _literally in position_.

A _Tuple_ is an _immutable sequence type_. It can behave like a list, but it
can't be modified in situ. Tuples are _ordered and unchangeable_ collections
of data.

Tuples use _parenthesis_ in creation, whereas a List uses _square brackets_.
It is also possible to _create a tuple just from a set of values separated by_
_commas_.

You can also create a tuple using a Python built-in function called `tuple()`.

Tuples can be unpacked into variables using the assignment operator.

```py
tup = 1, 2, 3
a, b, c = tup
# a = 1, b = 2, c = 3

```

```py
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
tuple_3 = tuple([2, 4, 6])

print(tuple_1)
print(tuple_2)
print(tuple_3)

```

> **Note:** each tuple element may be of a different type, including variables.

It is possible to create an empty tuple using only parentheses.

```py
empty_tuple = ()

```

If you want to create a _one-element tuple_, you must end the value with a
comma.

```py
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

```

You cannot change Tuple elements, but you can delete a tuple as a whole.

```py
my_tuple = (1, 2.0, "string", [3, 4], (5,), True)

del my_tuple
print(my_tuple)  # ERROR

```

You can access tuple elements the same way you would read lists, using
_indices_, _slices_, and even the _`for` loop_.

What else can tuples do?

* the `len()` function accepts tuples and returns the number of elements
* the `+` operator can join tuples together
* the `*` operator can multiply tuples, just like lists
* the `in` and `not in` operators work in the same way as in lists

```py
my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))  # 9
print(t1)  # (1, 10, 100, 1000, 10000)
print(t2)  # (1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple)  # True
print(-10 not in my_tuple)  # True

```

One of the most useful tuple properties is their ability to _appear on the_
_left side of the assignment operator_.

```py
var = 123
t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)  # Output: (2,) (3, 123) (1,)

```

The _dictionary_ is another Python data structure. It's _not a sequence type_
(but can be easily adapted to sequence processing), and it is _mutable_.

A _dictionary_ is a set of _key:value_ pairs.

> **Note:**
>
> * each _key_ must be unique
> * a _key_ may be _any immutable type of object_
> * a _dictionary_ is not a list - a list contains a set of numbered values,
>   while a dictionary holds pairs of values
> * the `len()` function works for dictionaries, too - it returns the number of
>   key:value elements in the dictionary
> * a _dictionary_ is a _one-way tool_ - if you have an English-French
>   dictionary, you can look for French equivalents of English terms, but not
>   vice versa

The list of pairs is _surrounded by curly braces {}_, while the pairs
themselves are _separated by commas_, and the _keys and values by colons_.

You can also create a dictionary using a Python built-in function called
`dict()` (used with tuples).

The dictionary as a whole can be printed with a single `print()` invocation.

```py
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

```

The _key:value_ pairs can also be _number:string_, as well as _number:number_.
A dictionary value can be a tuple.

If you want to get any of the values, you have to deliver a valid key value.
You _must not use a non-existing key_.

```py
print(dictionary['cat'])  # chat
print(phone_numbers.get("Suzy"))  # 22657854310
print(phone_numbers['president'])  # ERROR

```

_Keys are case-sensitive_.

> **NOTE:** When you write a big or lengthy expression, it may be a good idea
> to keep it vertically aligned.

The formatting below is called a _hanging indent_.

```py
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse", "cheval"
}

```

The dictionary `keys()` method _returns an iterable object consisting of all_
_the keys gathered within the dictionary_.

```py
for key in dictionary.keys():
    print(key, "->", dictionary[key])

```

The dictionary `values()` method works similarly to `keys()`, but _returns_
_values_.
As the dictionary is not able to automatically find a key for a given value,
the role of this method is rather limited.

```py
for french in dictionary.values():
    print(french)

```

The dictionary `items()` method _returns tuples where each tuple is a_
_key:value pair_.

```py
for english, french in dictionary.items():
    print(english, "->", french)

```

To _add a new key:value pair_ to a dictionary, you only have to assign a value
to a new, _previously non-existing key_.

```py
dictionary["swan"] = "cygne"

```

You can also _insert_ an item to a dictionary by using the `update()` method.

```py
dictionary.update({"duck": "canard"})

```

_Removing a key_ from a dictionary will always cause the _removal of the_
_associated value_. Values cannot exist without their keys. This is done with
the `del` instruction. You can also delete a dictionary with this instruction.

_Note: removing a non-existing key causes an error._

```py
del dictionary["dog"]
del dictionary

```

To _remove the last item_ in a dictionary, you can use the `popitem()` method.
In the older versions of Python, i.e., before _3.6.7_, the `popitem()` method
removes a random item from a dictionary.

```py
dictionary.popitem()

```

To _remove all the dictionary's items_, you can use the `clear()` method.

```py
dictionary.clear()

```

To _copy_ a dictionary, use the `copy()` method.

```py
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse", "cheval"
}

french_eng_dict = dictionary.copy()

```

### Section 7 - Exceptions

> To err is human.
>
> It's only those who do nothing that make no mistakes.

Dealing with programming errors has (at least) two sides:

* bad data
* bug in code

In Python, there is a distinction between two kinds of errors:

* _syntax errors (parsing errors)_: occurs when the parser comes across an
  incorrect statement
* _exceptions_: detected during execution, and occurs even when a statement
  / expression is syntactically correct

The `try-except` branch:

```py
try:
    # It's a place where
    # you can do something
    # without asking for permission.
except:
    # It's a spot dedicated to
    # solemnly begging for forgiveness.

```

First, starting with the `try` keyword - this is the place where you put the
code you suspect is risky and may be terminated in case of error (exception).

Second, starting with the `except` keyword - this is designed to handle the
exception.

```py
try:
    value = int(input("Enter a natural number: "))
    print("The reciprocal of", value, "is", (1/value))
except:  # except (Exception)
    print("I do not know what to do.")

```

The code in the `except` branch is activated only when an exception has been
encountered (_raised_) inside the `try` block. There is no way to get there by
any other means.

When either the `try` or `except` block is executed successfully, the control
returns to the normal path of execution, and any code located beyond in the
source file is executed as if nothing happened.

To deal with more than one exception, we include another `except` branch. The
number of `except` branches is not limited - you can specify as many or as few
of them as you need, but don't forget that _none of the exceptions can be_
_specified more then once_.

```py
try:
    value = int(input("Enter a natural number: "))
    print("The reciprocal of", value, "is", (1/value))
except (ValueError):
    print("I do not know what to do.")
except (ZeroDivisionError):
    print("Division by zero is not allowed in our Universe.")

```

_If one of the `except` branches is executed, all the other branches remain_
_idle._

When an exception is raised and there is no `except` branch dedicated to this
exception, it will be handled by the _default branch (no exception name_
_specified)_. The default `except` branch _must_ be the last `except` branch.

```py
try:
    value = int(input("Enter a natural number: "))
    print("The reciprocal of", value, "is", (1/value))
except (ValueError):
    print("I do not know what to do.")
except (ZeroDivisionError):
    print("Division by zero is not allowed in our Universe.")
except:  # except (Exception)
    print("Something strange has happened here... Sorry!")

```

You can also specify and handle multiple built-in exceptions within a single
`except` clause:

```py
try:
    value = int(input("Enter a natural number: "))
    print("The reciprocal of", value, "is", (1/value))
except (ValueError, ZeroDivisionError):
    print("Wrong value or No division by zero rule broken.")
except:  # except (Exception)
    print("Something strange has happened here... Sorry!")

```

It is a bad idea to handle the _SyntaxError_ exception in your programs, as you
should produce code that is free of syntax errors, instead of masking it.

As you are not able to avoid making bugs in your code, you must always be ready
to seek out and destroy them. Don't bury your head in the sand - _ignoring_
_errors won't make them disappear_.

An important duty for developers is to test the newly created code. Another
important aspect of software testing is strictly psychological, that authors
_aren't able to objectively evaluate and verify their works_.

This is why each _novelist_ needs an _editor_ and each _programmer_ needs a
_tester_.

Your primary duty is to _ensure that you've checked all execution paths_ your
code can go through.

You need to accept that, firstly, _testers_ are the _developer's_ best
friends - don't treat the bugs they discover as an offence or a malignancy;
and, secondly, each bug the testers find is a bug that won't affect the users.

A _debugger_ is the basic measure a developer can use against bugs.

_Debugging_ is the process during which bugs are removed from the code.

A _debugger_ is a specialized piece of software that can control how your
program is executed.

_print_ debugging involves inserting several additional `print()` invocations
inside your code to output data which illustrates the path your code is
currently negotiating.
Please don't use obscene or indecent words for this purpose.
After the bugs are found and removed, the additional printouts may be
commented out or removed. Don't let them be executed in the final code.

Don't believe yourself - check everything twice. Here are some useful tips:

1. Try to tell someone (or a _rubber duck_) what your code is expected to do
   and how it actually behaves.
2. Try to isolate the problem.
3. Analyze all the changes you've introduced into your code (if it didn't show
   up earlier)
4. Take a break.
5. Be optimistic.
