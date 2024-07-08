# PyRu_Example Syntax..
//

# Define a function
def greet(name):
    print("Hello, " + name)

# Define a class
class MyClass:
    def __init__(self, value):
        @value = value

    def display(self):
        print("Value:", @value)

# Use the function
greet("World")

# Create an instance of MyClass
obj = MyClass.new(10)
obj.display()

Let's outline the syntax tokens, lexer, parser, and compiler components for Pyru based on the provided requirements:

### Syntax Tokens:
1. **Keywords**:
   - `if`, `elif`, `else`
   - `for`, `while`
   - `def`, `class`, `lambda`
   - `return`, `break`, `continue`
   - `try`, `except`, `finally`, `rescue`
   - `public`, `private`, `protected`
   - `import`, `require`
   - `end`

2. **Identifiers**:
   - Variable names, function names, class names, module names, etc.

3. **Literals**:
   - Integers, floats, strings, booleans, None/null, etc.

4. **Operators**:
   - Arithmetic operators (+, -, *, /, %, etc.)
   - Comparison operators (==, !=, <, >, <=, >=, etc.)
   - Logical operators (and, or, not)
   - Assignment operators (=, +=, -=, *=, /=, etc.)

5. **Punctuation**:
   - Parentheses `()`, Brackets `[]`, Braces `{}`, Colons `:`, Commas `,`, Period `.`

### Lexer:
The lexer is responsible for tokenizing the input code into tokens.

### Parser:
The parser parses the tokenized code and builds an abstract syntax tree (AST) based on the grammar rules.

### Compiler:
The compiler translates the AST into executable code, either machine code or bytecode.

### Pyru Grammar Rules:
1. **Conditional Statements**:
   - `if` condition `:` suite
   - `elif` condition `:` suite
   - `else` `:` suite

2. **Looping Constructs**:
   - `for` var `in` iterable `:` suite
   - `while` condition `:` suite

3. **Function and Method Definitions**:
   - `def` func_name `(` params `)` `:` suite
   - `def` method_name `(` params `)` `:` suite (within classes)

4. **Lambda Functions**:
   - `lambda` params `:` expression

5. **Class Definitions**:
   - `class` class_name `:` suite

6. **Inheritance, Encapsulation, Polymorphism**:
   - `class` subclass_name `(` superclass_name `)` `:` suite

7. **Method Visibility Modifiers**:
   - `public`, `private`, `protected` (used within classes)

8. **Exception Handling**:
   - `try` `:` suite
   - `except` [exception_type `as` identifier] `:` suite
   - `finally` `:` suite

9. **Modules and Packages**:
   - `import` module_name
   - `require` library_name

10. **Indentation and Blocks**:
   - Use of indentation for code blocks, similar to Python.
   - Use of `end` keyword to terminate code blocks, similar to Ruby.

### Example Pyru Code:

```pyru
# Conditional Statement
if condition:
    statement
elif another_condition:
    statement
else:
    statement

# Looping Construct
for item in iterable:
    statement

# Function Definition
def my_function(arg1, arg2):
    statement

# Method Definition
class MyClass:
    def my_method(self, arg):
        statement

# Lambda Function
square = lambda x: x * x

# Class Definition with Inheritance
class SubClass(SuperClass):
    def __init__(self, arg):
        statement

# Exception Handling
try:
    statement
except Exception as e:
    statement
finally:
    statement

# Module Import
import my_module

# Package Require
require 'my_library'
```

This structure provides a foundation for developing a Pyru interpreter or compiler. Each component (lexer, parser, compiler) would need to be implemented according to these grammar rules to build a working Pyru environment.
