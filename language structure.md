# language structure for Pyru, combining the features of both Python and Ruby:

### Pyru Language Structure:

#### 1. Data Types:
   - Support for dynamic typing with optional static typing annotations (like Python).
   - Common data types such as integers, floats, strings, lists, dictionaries, tuples, etc.

#### 2. Control Structures:
   - Conditional statements (`if`, `elif`, `else`) similar to Python.
   - Looping constructs (`for`, `while`) similar to Python.
   - Ruby-style iterators (`each`, `map`, `reduce`, etc.).

#### 3. Functions and Methods:
   - Define functions using `def` keyword similar to Python.
   - Support for both positional and keyword arguments.
   - Methods defined using `def` keyword within classes, similar to both Python and Ruby.
   - Support for lambda functions (anonymous functions) similar to both Python and Ruby.

#### 4. Classes and Objects:
   - Class definition using `class` keyword, similar to both Python and Ruby.
   - Support for inheritance, encapsulation, and polymorphism.
   - Ruby-style method visibility modifiers (`public`, `private`, `protected`).

#### 5. Error Handling:
   - Exception handling using `try`, `except`, `finally` blocks similar to Python.
   - Ruby-style `rescue` clauses for handling exceptions.

#### 6. Modules and Packages:
   - Organize code into modules and packages, similar to both Python and Ruby.
   - Import modules using `import` statement similar to Python.
   - Ruby-style `require` statement for loading external libraries.

#### 7. Syntax:
   - Significant indentation for code blocks (like Python).
   - Use of `end` keyword to terminate code blocks (like Ruby).

#### 8. Interoperability:
   - Seamless integration with Python and Ruby libraries.
   - Ability to call Python functions from Pyru and vice versa.

### Example Pyru Code:

```pyru
# Define a function
def greet(name)
  puts "Hello, #{name}"
end

# Define a class
class MyClass
  def initialize(value)
    @value = value
  end

  def display
    puts "Value: #{@value}"
  end
end

# Use the function
greet("World")

# Create an instance of MyClass
obj = MyClass.new(10)
obj.display
```


### Conclusion:

Pyru aims to combine the best features of Python and Ruby into a single programming language, providing developers with a familiar syntax and powerful features for building applications. With support for dynamic and optional static typing, control structures, functions, classes, error handling, modules, packages, and interoperability with Python and Ruby libraries, Pyru offers a versatile and expressive environment for software development.
