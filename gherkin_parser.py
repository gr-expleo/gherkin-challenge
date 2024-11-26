import ply.yacc as yacc

class GherkinParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokens

    # Parsing rules
    def p_features(self, p):
        '''features : features feature
                    | feature'''
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_feature(self, p):
        '''feature : FEATURE TEXT scenarios'''
        p[0] = {
            "Feature": {
                p[2].strip(): {
                    "Scenarios": p[3]
                }
            }
        }

    def p_scenarios(self, p):
        '''scenarios : scenarios scenario
                     | scenario'''
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_scenario(self, p):
        '''scenario : SCENARIO TEXT steps'''
        p[0] = {
            "Scenario": p[2].strip(),
            "Steps": p[3]
        }

    def p_steps(self, p):
        '''steps : steps step
                 | step'''
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_step(self, p):
        '''step : GIVEN TEXT
                | WHEN TEXT
                | THEN TEXT
                | AND TEXT'''
        p[0] = {p[1]: p[2].strip()}

    def p_error(self, p):
        if p:
            raise SyntaxError(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
        else:
            raise SyntaxError("Syntax error: Unexpected end of input")

    def build(self, **kwargs):
        """Build the parser."""
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data):
        return self.parser.parse(data, lexer=self.lexer.lexer)
