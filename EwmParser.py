from lark import *
from lark.indenter import Indenter
from transf import EwmTransformer

def main():

    ewmGrammarFile = open("EwmGrammar.lark", "r")
    ewmGrammar = ewmGrammarFile.read()

    ewmParser = Lark(ewmGrammar, start='start', propagate_positions=True, postlex=TreeIndenter())

    exFile = open("example.ewm", "r")
    ex = exFile.read()

    tree = ewmParser.parse(ex)

    carlos = EwmTransformer().transform(tree)

    print(carlos)

    # print(tree.pretty())



class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

if __name__ == "__main__":
    main()