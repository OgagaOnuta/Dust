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
_interpreter_. The file needs to be distributed with the interpreter.
Each line is executed separately, _read-check-execute_.

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
_Subexpressions in parentheses_ are always calculated first.

The Hierarchy of Priorities (from highest to lowest)

1. +, - (unary)
2. **
3. *, /, //, %
4. +, - (binary)
5. <, <=, >, >=
6. ==, !=

### Section 4 - Variables

A _variable_ is a named location reserved to store values in the memory.
Python _variables_ have a _name_ and a _value_.

Rules for naming variables in Python:

* the name _must_ be composed of _uppercase or lowercase letters_, _digits_,
  and _underscore_
* the name _must_ begin with a _letter_ or _underscore_
* the name is _case-sensitive_
* the name _must not_ be a _Python keyword_The above-listed rules also apply to _function names_.

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

The loop body should be able to change the condition's value bacause doing
a thing usually decreases the number of things to do, and also prevent an
_infinite loop_.

**REMEMBER**
Don't feel obliged to code your programs in the shortest and most compact way.
_Readability_ may be a more important factor.
Keep your code ready for a new programmer.

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
| - | - | - |
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

The `or` (_disjunction operator_)  is a _binary operator_ with a
_lower priority than `and`_.

| Argument `A` | Argument `B` | `A or B` |
| - | - | - |
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

The `not` (_negation operator_) is a _unary operator_ performing a
_logical negation_. Its _priority is very high_, the same as the unary
`+` and `-`.

| Argument | `not` Argument |
| - | - |
| False | True |
| True | False |

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
* `~` (tilde) - _bitwise negation_
* `^` (caret) - _bitwise exclusive or (xor)_
  * requires exactly one `1` to provide `1` as the result

| Argument `A` | Argument `B` | `A & B` | `A \| B` | `A ^ B` |
| - | - | - | - | - |
| `0` | `0` | `0` | `0` | `0` |
| `0` | `1` | `0` | `1` | `1` |
| `1` | `0` | `0` | `1` | `1` |
| `1` | `1` | `1` | `1` | `0` |

| Argument | `~` Argument |
| - | - |
| `0` | `1` |
| `1` | `0` |

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
