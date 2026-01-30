class Conversions:
    @staticmethod
    def pyru_to_python(pyru_value):
        if isinstance(pyru_value, list):
            return [Conversions.pyru_to_python(item) for item in pyru_value]
        elif isinstance(pyru_value, dict):
            return {Conversions.pyru_to_python(key): Conversions.pyru_to_python(value) for key, value in pyru_value.items()}
        # Add more conversion rules as needed
        else:
            return pyru_value

    @staticmethod
    def python_to_pyru(python_value):
        if isinstance(python_value, list):
            return [Conversions.python_to_pyru(item) for item in python_value]
        elif isinstance(python_value, dict):
            return {Conversions.python_to_pyru(key): Conversions.python_to_pyru(value) for key, value in python_value.items()}
        # Add more conversion rules as needed
        else:
            return python_value

    @staticmethod
    def pyru_to_ruby(pyru_value):
        if isinstance(pyru_value, list):
            return Conversions.pyru_to_ruby_array(pyru_value)
        elif isinstance(pyru_value, dict):
            return Conversions.pyru_to_ruby_hash(pyru_value)
        # Add more conversion rules as needed
        else:
            return pyru_value

    @staticmethod
    def ruby_to_pyru(ruby_value):
        if isinstance(ruby_value, list):
            return Conversions.ruby_array_to_pyru(ruby_value)
        elif isinstance(ruby_value, dict):
            return Conversions.ruby_hash_to_pyru(ruby_value)
        # Add more conversion rules as needed
        else:
            return ruby_value

    @staticmethod
    def pyru_to_ruby_array(pyru_list):
        return pyru_list

    @staticmethod
    def pyru_to_ruby_hash(pyru_dict):
        return pyru_dict

    @staticmethod
    def ruby_array_to_pyru(ruby_array):
        return ruby_array

    @staticmethod
    def ruby_hash_to_pyru(ruby_hash):
        return ruby_hash
