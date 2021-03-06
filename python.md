# Python Knowledge
- is vs == - is compares if two variables point to same object in memory while == compares value of two objects
- None vs null - In other programming languages, null is often defined to be 0, but Python used None to define null objects and variables. None is a full-blown object with the type NoneType.
- Errors vs Exceptions - Errors are problems in a program while exceptions are raised when internal events occur which change the normal flow of the program.
  - Exceptions are to be thrown if a method is not able to do the task it is supposed to do.
  - Base classes for other exceptions - BaseException, Exception, ArithmeticError, BufferError, LookupError
  - ZeroDivisionError
  - ArithmeticError, LookupError, NameError, OSError
- Dunder Methods - magic methods to override functionality for built-in functions for custom classes. Preceded and succeeded by double underscores. 
  - init - create instance
  - str - goal is to be human-readable
  - repr - goal is to be unambiguous so an eval call will work (eval(repr(c))==c_
  - str vs repr
    - Implement __repr__ for any class you implement. This should be second nature. Implement __str__ if you think it would be useful to have a string version which errs on the side of readability.
  - len - called when "len" is used - (len(p))
  - contains - called when "in" is used
  - Operations Dunder Methods
    - add/iadd - +, +=
    - sub/isub - -, -=
    - mul/imul - *, *=
    - truediv, itruediv, floordiv, ifloordiv - \, \=, \\, \=
- Python Interpreter - bytecode interpreter (virtual machine) where input is bytecode
  - Interpreter - translates one statement of the program at a time into machine code
    - JIT compiler is a feature of run-time interpreter that compiles bytecode into machine code instructions and then invokes object code (essentially removes interpreter overhead)
  - Compiler - scans entire program and translates all of it into machine code at once.
- Logging Levels
- List Comprehensions
- Decorators
- Generators