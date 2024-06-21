py_compile.compile(file, cfile=None, dfile=None, doraise=False, optimize=-1, invalidation_mode=PycInvalidationMode.TIMESTAMP, quiet=0)

__all__ = ["compile_dir","compile_file","compile_path"]

class PyruCompiler:
    def __init__(self, ast):
        self.ast = ast

    def compile(self):
        compiled_code = ""
        for node in self.ast:
            compiled_code += self.compile_node(node)
        return compiled_code

    def compile_node(self, node):
        node_type = node[0]
        if node_type == "ConditionalStatement":
            return self.compile_conditional_statement(node)
        elif node_type == "LoopStatement":
            return self.compile_loop_statement(node)
        elif node_type == "FunctionDefinition":
            return self.compile_function_definition(node)
        elif node_type == "ClassDefinition":
            return self.compile_class_definition(node)
        elif node_type == "LambdaFunction":
            return self.compile_lambda_function(node)
        elif node_type == "TryExceptStatement":
            return self.compile_try_except_statement(node)
        elif node_type == "Assignment":
            return self.compile_assignment(node)
        elif node_type == "ImportStatement":
            return self.compile_import_statement(node)
        elif node_type == "RequireStatement":
            return self.compile_require_statement(node)
        else:
            raise Exception(f"Invalid node type: {node_type}")

    def compile_conditional_statement(self, node):
        compiled_code = f"if {self.compile_expression(node[1])}:\n"
        compiled_code += self.compile_suite(node[2])
        for elif_node in node[3:]:
            compiled_code += f"elif {self.compile_expression(elif_node[1])}:\n"
            compiled_code += self.compile_suite(elif_node[2])
        if len(node) > 3 and node[-1][0] == "ElseStatement":
            compiled_code += "else:\n"
            compiled_code += self.compile_suite(node[-1][1])
        return compiled_code

    def compile_loop_statement(self, node):
        compiled_code = f"for {node[1]} in {self.compile_expression(node[2])}:\n"
        compiled_code += self.compile_suite(node[3])
        return compiled_code

    def compile_function_definition(self, node):
        parameters = ", ".join(node[2])
        compiled_code = f"def {node[1]}({parameters}):\n"
        compiled_code += self.compile_suite(node[3])
        return compiled_code

    def compile_class_definition(self, node):
        compiled_code = f"class {node[1]}:\n"
        compiled_code += self.compile_suite(node[2])
        return compiled_code

    def compile_lambda_function(self, node):
        parameters = ", ".join(node[1])
        compiled_code = f"lambda {parameters}: {self.compile_expression(node[2])}"
        return compiled_code

    def compile_try_except_statement(self, node):
        compiled_code = f"try:\n"
        compiled_code += self.compile_suite(node[1])
        if node[2] is not None:
            compiled_code += f"except Exception as e:\n"
            compiled_code += self.compile_suite(node[2])
        if node[3] is not None:
            compiled_code += f"finally:\n"
            compiled_code += self.compile_suite(node[3])
        return compiled_code

    def compile_assignment(self, node):
        return f"{node[1]} = {self.compile_expression(node[2])}\n"

    def compile_import_statement(self, node):
        return f"import {node[1]}\n"

    def compile_require_statement(self, node):
        return f"from {node[1]} import *\n"

    def compile_suite(self, suite):
        compiled_code = ""
        for statement in suite:
            compiled_code += self.compile_node(statement)
        return compiled_code

    def compile_expression(self, expression):
        if isinstance(expression, list):
            if expression[0] == "BinaryOperation":
                left = self.compile_expression(expression[1])
                operator = expression[2]
                right = self.compile_expression(expression[3])
                return f"{left} {operator} {right}"
            elif expression[0] == "FunctionCall":
                function_name = expression[1]
                args = ", ".join([self.compile_expression(arg) for arg in expression[2]])
                return f"{function_name}({args})"
            elif expression[0] == "Identifier":
                return expression[1]
            elif expression[0] == "Number":
                return str(expression[1])
            elif expression[0] == "String":
                return f'"{expression[1]}"'
            elif expression[0] == "AttributeAccess":
                obj = self.compile_expression(expression[1])
                attr = expression[2]
                return f"{obj}.{attr}"
            else:
                raise Exception(f"Invalid expression node: {expression}")
        else:
            return expression

# Example usage:
ast = [
    ["ConditionalStatement", "condition", ["BinaryOperation", "condition1", "==", "condition2"], [["statement1"]], [["ElifStatement", ["BinaryOperation", "condition3", "!=", "condition4"], [["elif_statement"]]]], ["ElseStatement", [["else_statement"]]]], 
    ["LoopStatement", "variable", "iterable", [["loop_statement"]]],
    ["FunctionDefinition", "my_function", ["arg1", "arg2"], [["function_statement"]]],
    ["ClassDefinition", "MyClass", [["class_statement"]]],
    ["LambdaFunction", ["arg"], "expression"],
    ["TryExceptStatement", [["try_suite"]], [["except_suite"]], [["finally_suite"]]],
    ["Assignment", "x", "10"],
    ["ImportStatement", "my_module"],
    ["RequireStatement", "my_library"]
]

compiler = PyruCompiler(ast)
python_code = compiler.compile()
print(python_code)
