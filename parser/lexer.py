import string
from typing import Optional

class Token:
    def __init__(self, type_: str, value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    DIGITS = "0123456789"
    LETTERS = string.ascii_letters

    def __init__(self, text: str):
        self.text = text
        self.position = 0
        self.current_character = text[0] if text else None

    def advance(self):
        """
        Move to the next character.
        """
        self.position += 1
        if self.position < len(self.text):
            self.current_character = self.text[self.position]
        else:
            self.current_character = None
    
    def peek(self) -> Optional[str]:
        """
        Look at the next character without consuming it.
        """
        if self.position + 1 < len(self.text):
            return self.text[self.position + 1]
        return None

    def skip_whitespace(self):
        while self.current_character and self.current_character.isspace():
            self.advance()
        
    def tokenize(self):
        tokens = []

        while self.current_character is not None:
            character = self.current_character

            if character.isspace():
                self.skip_whitespace()
                continue
            
            next_character = self.peek()
            if character in self.DIGITS or (character == '.' and next_character in self.DIGITS if next_character else False):
                tokens.append(self._make_number())
                continue

            if character in self.LETTERS:
                tokens.append(self._make_identifier())
                continue

            if character == "+":
                tokens.append(Token("PLUS", character))
            elif character == "-":
                tokens.append(Token("MINUS", character))
            elif character == "*":
                tokens.append(Token("MUL", character))
            elif character == "/":
                tokens.append(Token("DIV", character)) 
            elif character == "^":
                tokens.append(Token("POW", character))
            elif character == "(":
                tokens.append(Token("LPAREN", character))
            elif character == ")":
                tokens.append(Token("RPAREN", character))
            else:
                raise ValueError(f"Illegal character: {character}")
            
            self.advance()
        
        tokens.append(Token("EOF"))
        return tokens

            
    def _make_number(self) -> Token:
        num_str = ""
        dot_count = 0

        while self.current_character is not None and (self.current_character in self.DIGITS or self.current_character == '.'):
            if self.current_character == '.':
                if dot_count == 1:
                    raise ValueError("Invalid number format (multiple dots)")
                dot_count += 1
            num_str += self.current_character
            self.advance()
        
        return Token('Number', float(num_str))

    def _make_identifier(self) -> Token:
        id_str = ""
        while self.current_character is not None and (self.current_character in self.LETTERS or self.current_character in self.DIGITS):
            id_str += self.current_character
            self.advance()
        
        save_pos = self.position
        self.skip_whitespace()
        is_function = self.current_character == '('
        self.position = save_pos
        self.current_char = self.text[self.position] if self.position < len(self.text) else None
        
        token_type = 'FUNCTION' if is_function else 'VARIABLE'
        return Token(token_type, id_str)
    
if __name__ == "__main__":
    exprs = [
        "3.14 + x",
        "sin(x) + cos(y)",
        "a1 + b2 * 4.5",
        ".5 + 1.5"
    ]

    for e in exprs:
        lexer = Lexer(e)
        tokens = lexer.tokenize()
        print (e, "->", tokens)