import re
import yaml
from pathlib import Path

TOKEN_SPEC_PATH = Path(__file__).parents[2] / "spec" / "tokens.yml"

class Lexer:
    def __init__(self):
        spec = yaml.safe_load(TOKEN_SPEC_PATH.read_text())
        self.rules = []

        for name, rule in spec.items():
            if "regex" in rule:
                self.rules.append((name, re.compile(rule["regex"])))
            elif isinstance(rule, str):
                self.rules.append((name, re.compile(re.escape(rule))))

    def tokenize(self, text):
        pos = 0
        tokens = []

        while pos < len(text):
            match = None
            for name, regex in self.rules:
                match = regex.match(text, pos)
                if match:
                    tokens.append((name, match.group()))
                    pos = match.end()
                    break

            if not match:
                raise SyntaxError(f"Illegal character at {pos}")

        tokens.append(("EOF", None))
        return tokens
        
