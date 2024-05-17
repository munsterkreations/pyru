import ruby
from turtle import begin_fill, begin_poly


class PyruException(Exception):
    pass

class PythonException(Exception):
    pass

class RubyException(Exception):
    pass

# Example usage:
try:
    # Pyru code that may raise an exception
    raise PyruException("An error occurred in Pyru code.")
except PyruException as e:
    # Handle the Pyru exception
    print("Caught Pyru exception:", e)

try:
    # Python code that may raise an exception
    raise PythonException("An error occurred in Python code.")
except PythonException as e:
    # Handle the Python exception
    print("Caught Python exception:", e)

 
class RubyException(Exception):
    pass
    # Example usage: Ruby code that may raise an exception
    begin # type: ignore
raise RubyException "An error occurred in Ruby code."
rescue; RubyException => e # type: ignore
    # Handle the Ruby exception
puts "Caught Ruby exception: #{e.message}" # type: ignore
end
