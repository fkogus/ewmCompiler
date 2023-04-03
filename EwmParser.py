from lark import *
from lark.indenter import Indenter
from transf import EwmTransformer
import json

def main():

    ewmGrammarFile = open("EwmGrammar.lark", "r")
    ewmGrammar = ewmGrammarFile.read()

    ewmParser = Lark(ewmGrammar, start='start', propagate_positions=True, postlex=TreeIndenter())

    exFile = open("home.ewm", "r")
    ex = exFile.read()

    tree = ewmParser.parse(ex)

    saida = EwmTransformer().transform(tree)

    with open("out.json", "w") as outfile:
        json.dump(saida, outfile, indent=2)


class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

if __name__ == "__main__":
    main()