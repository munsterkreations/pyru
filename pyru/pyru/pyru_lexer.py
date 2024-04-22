import re

class PyruLexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.current_position = 0

    def tokenize(self):
        while self.current_position < len(self.code):
            char = self.code[self.current_position]
            if char.isspace():
                self.current_position += 1
            elif char.isalpha() or char == '_':
                self.tokenize_identifier()
            elif char.isdigit():
                self.tokenize_number()
            elif char == '"':
                self.tokenize_string()
            elif char in ('+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|'):
                self.tokenize_operator()
            elif char in ('(', ')', '[', ']', '{', '}', ',', ':'):
                self.tokens.append((char, "PUNCTUATION"))
                self.current_position += 1
            elif char == '#':
                self.tokenize_comment()
            else:
                raise Exception(f"Invalid character '{char}' at position {self.current_position}")

        return self.tokens

    def tokenize_identifier(self):
        identifier = ''
        while self.current_position < len(self.code):
            char = self.code[self.current_position]
            if char.isalnum() or char == '_':
                identifier += char
                self.current_position += 1
            else:
                self.tokens.append((identifier, "IDENTIFIER"))
                return

    def tokenize_number(self):
        number = ''
        while self.current_position < len(self.code):
            char = self.code[self.current_position]
            if char.isdigit() or char == '.':
                number += char
                self.current_position += 1
            else:
                self.tokens.append((number, "NUMBER"))
                return

    def tokenize_string(self):
        string = ''
        self.current_position += 1
        while self.current_position < len(self.code):
            char = self.code[self.current_position]
            if char != '"':
                string += char
                self.current_position += 1
            else:
                self.tokens.append((string, "STRING"))
                self.current_position += 1
                return
        raise Exception("Unterminated string")

    def tokenize_operator(self):
        operator = ''
        while self.current_position < len(self.code):
            char = self.code[self.current_position]
            if char in ('+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|'):
                operator += char
                self.current_position += 1
            else:
                self.tokens.append((operator, "OPERATOR"))
                return

    def tokenize_comment(self):
        comment = ''
        while self.current_position < len(self.code):
            char = self.code[self.current_position]
            if char != '\n':
                comment += char
                self.current_position += 1
            else:
                self.tokens.append((comment, "COMMENT"))
                self.current_position += 1
                return

# Example usage:
code = """
# This is a comment
x = 10
y = 20
print("Sum:", x + y)
"""

lexer = PyruLexer(code)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
