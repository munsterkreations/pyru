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

 
try:
    # Ruby code that may raise an exception
   raise RubyException ("An error occurred in Ruby code.")
rescue; RubyException => e # type: ignore
    # Handle the Ruby exception
puts "Caught Ruby exception: #{e.message}" # type: ignore
     ruby.execute("""
        # Your Ruby code here
        raise RubyException, "An error occurred in Ruby code."
    """)
except ruby.RubyError as e:
    # Handle the Ruby exception
    print("Caught Ruby exception:", e)
    # Example usage: Ruby code that may raise an exception
    begin # type: ignore

end
