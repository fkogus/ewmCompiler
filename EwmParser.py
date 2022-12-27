from lark import *
from lark.indenter import Indenter

def main():

    ewmGrammarFile = open("EwmGrammar.lark", "r")
    ewmGrammar = ewmGrammarFile.read()

    ewmParser = Lark(ewmGrammar, start='start', propagate_positions=True, postlex=TreeIndenter())

    exFile = open("example.ewm", "r")
    ex = exFile.read()

    tree = ewmParser.parse(ex)

    print(tree.pretty())


 
# class MyTransformer(Transformer):

#     def __init__(self, visit_tokens: bool = True) -> None:
#         self.vars = {}
#         super().__init__(visit_tokens)

#     def style_definition(self, a):
#         print("\n\n\n", type(a), "\n\n\n")
        
#         return a

class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

if __name__ == "__main__":
    main()