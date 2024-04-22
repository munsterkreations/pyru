# pyru_examples.rb

# Require the pyru_ruby_bridge gem
require 'pyru_ruby_bridge'

# Example method to demonstrate calling a Pyru method using the bridge module
def call_pyru_method
  begin
    # Call the Pyru method using the RubyBridge class
    result = PyruRubyBridge::RubyBridge.some_pyru_method("example_argument")

    # Print the result
    puts "Result from Pyru method: #{result}"
  rescue PyruRubyBridge::PyruException => e
    # Handle Pyru exceptions raised by the bridge module
    puts "Pyru exception caught: #{e.message}"
  end
end

# Main method
def main
  # Call the example method to demonstrate calling a Pyru method
  call_pyru_method
end

# Entry point of the script
if __FILE__ == $0
  main
end
