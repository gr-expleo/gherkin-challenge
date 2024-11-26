import ply.lex as lex
import re

class GherkinLexerError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
        
class GherkinLexer:
    # Define tokens
    tokens = (
        'FEATURE', 'SCENARIO', 'GIVEN', 'WHEN', 'THEN', 'AND', 'TEXT'
    )

    def t_FEATURE(self, t):
        r'Feature:'
        return t

    # Making sure to let the user know they have forgotten semicolon
    def t_partial_FEATURE(self, t):
        r'Feature'
        raise GherkinLexerError(f"Syntax error: Missing ':' after 'Feature' at line {t.lexer.lineno}", 400)

    def t_SCENARIO(self, t):
        r'Scenario:'
        return t

    # Making sure to let the user know they have forgotten semicolon
    def t_partial_SCENARIO(self, t):
        r'Scenario' 
        raise GherkinLexerError(f"Syntax error: Missing ':' after 'Scenario' at line {t.lexer.lineno}", 400)
    
    def t_GIVEN(self, t):
        r'Given'
        return t

    def t_WHEN(self, t):
        r'When'
        self.when_seen = True
        return t

    def t_THEN(self, t):
        r'Then'
        self.then_seen = True
        return t

    def t_AND(self, t):
        r'And'
        return t

    # Token to capture non-keyword text
    def t_TEXT(self, t):
        r'[^\n#]+'  # don't match #
        return t

    # Token for comments
    def t_COMMENT(self, t):
        r'#.*'  # Any line with # , we skip
        pass  # We simply ignore comments

    t_ignore = ' \t \r'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        raise GherkinLexerError(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}", 400)
        
    def build(self, **kwargs):
        try:
            self.lexer = lex.lex(module=self, reflags=re.IGNORECASE, **kwargs)
        except Exception as e:
            raise
        
    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()
