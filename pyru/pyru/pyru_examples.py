# pyru_examples.py

# Import the Pyru-to-Ruby bridge module
from pyru_ruby_bridge import RubyBridge, PyruException # type: ignore

# Example function to demonstrate calling a Ruby method using the bridge module
def call_ruby_method():
    try:
        # Call the Ruby method using the RubyBridge class
        result = RubyBridge.some_ruby_method("example_argument")

        # Print the result
        print("Result from Ruby method:", result)
    except PyruException as e:
        # Handle Pyru exceptions raised by the bridge module
        print("Pyru exception caught:", e)

# Main function
def main():
    # Call the example function to demonstrate calling a Ruby method
    call_ruby_method()

# Entry point of the script
if __name__ == "__main__":
    main()
