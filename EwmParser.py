from lark import *
from lark.indenter import Indenter
from codegen import CodeGenerator
from transf import EwmTransformer
import json
import argparse
import os

def main():

    ewmGrammar = """PROPERTY.2 : "accent-color" | "align-content" | "align-items" | "align-self" | "all" | "animation" | "animation-delay" | "animation-direction" | "animation-duration" | "animation-fill-mode" | "animation-iteration-count" | "animation-name" | "animation-play-state" | "animation-timing-function" | "aspect-ratio" | "backdrop-filter" | "backface-visibility" | "background" | "background-attachment" | "background-blend-mode" | "background-clip" | "background-color" | "background-image" | "background-origin" | "background-position" | "background-position-x" | "background-position-y" | "background-repeat" | "background-size" | "block-size" | "border" | "border-block" | "border-block-color" | "border-block-end-color" | "border-block-end-style" | "border-block-end-width" | "border-block-start-color" | "border-block-start-style" | "border-block-start-width" | "border-block-style" | "border-block-width" | "border-bottom" | "border-bottom-color" | "border-bottom-left-radius" | "border-bottom-right-radius" | "border-bottom-style" | "border-bottom-width" | "border-collapse" | "border-color" | "border-image" | "border-image-outset" | "border-image-repeat" | "border-image-slice" | "border-image-source" | "border-image-width" | "border-inline" | "border-inline-color" | "border-inline-end-color" | "border-inline-end-style" | "border-inline-end-width" | "border-inline-start-color" | "border-inline-start-style" | "border-inline-start-width" | "border-inline-style" | "border-inline-width" | "border-left" | "border-left-color" | "border-left-style" | "border-left-width" | "border-radius" | "border-right" | "border-right-color" | "border-right-style" | "border-right-width" | "border-spacing" | "border-style" | "border-top" | "border-top-color" | "border-top-left-radius" | "border-top-right-radius" | "border-top-style" | "border-top-width" | "border-width" | "bottom" | "box-decoration-break" | "box-reflect" | "box-shadow" | "box-sizing" | "break-after" | "break-before" | "break-inside" | "caption-side" | "caret-color" | "@charset" | "clear" | "clip" | "color" | "column-count" | "column-fill" | "column-gap" | "column-rule" | "column-rule-color" | "column-rule-style" | "column-rule-width" | "column-span" | "column-width" | "columns" | "content" | "counter-increment" | "counter-reset" | "cursor" | "direction" | "display" | "empty-cells" | "filter" | "flex" | "flex-basis" | "flex-direction" | "flex-flow" | "flex-grow" | "flex-shrink" | "flex-wrap" | "float" | "font" | "@font-face" | "font-family" | "font-feature-settings" | "font-kerning" | "font-size" | "font-size-adjust" | "font-stretch" | "font-style" | "font-variant" | "font-variant-caps" | "font-weight" | "gap" | "grid" | "grid-area" | "grid-auto-columns" | "grid-auto-flow" | "grid-auto-rows" | "grid-column" | "grid-column-end" | "grid-column-gap" | "grid-column-start" | "grid-gap" | "grid-row" | "grid-row-end" | "grid-row-gap" | "grid-row-start" | "grid-template" | "grid-template-areas" | "grid-template-columns" | "grid-template-rows" | "hanging-punctuation" | "height" | "hyphens" | "image-rendering" | "@import" | "inline-size" | "inset" | "inset-block" | "inset-block-end" | "inset-block-start" | "inset-inline" | "inset-inline-end" | "inset-inline-start" | "isolation" | "justify-content" | "justify-items" | "justify-self" | "@keyframes" | "left" | "letter-spacing" | "line-height" | "list-style" | "list-style-image" | "list-style-position" | "list-style-type" | "margin" | "margin-block" | "margin-block-end" | "margin-block-start" | "margin-bottom" | "margin-inline" | "margin-inline-end" | "margin-inline-start" | "margin-left" | "margin-right" | "margin-top" | "mask-image" | "mask-mode" | "mask-origin" | "mask-position" | "mask-repeat" | "mask-size" | "max-height" | "max-width" | "@media" | "max-block-size" | "max-inline-size" | "min-block-size" | "min-inline-size" | "min-height" | "min-width" | "mix-blend-mode" | "object-fit" | "object-position" | "offset" | "offset-anchor" | "offset-distance" | "offset-path" | "offset-rotate" | "opacity" | "order" | "orphans" | "outline" | "outline-color" | "outline-offset" | "outline-style" | "outline-width" | "overflow" | "overflow-anchor" | "overflow-wrap" | "overflow-x" | "overflow-y" | "overscroll-behavior" | "overscroll-behavior-block" | "overscroll-behavior-inline" | "overscroll-behavior-x" | "overscroll-behavior-y" | "padding" | "padding-block" | "padding-block-end" | "padding-block-start" | "padding-bottom" | "padding-inline" | "padding-inline-end" | "padding-inline-start" | "padding-left" | "padding-right" | "padding-top" | "page-break-after" | "page-break-before" | "page-break-inside" | "paint-order" | "perspective" | "perspective-origin" | "place-content" | "place-items" | "place-self" | "pointer-events" | "position" | "quotes" | "resize" | "right" | "rotate" | "row-gap" | "scale" | "scroll-behavior" | "scroll-margin" | "scroll-margin-block" | "scroll-margin-block-end" | "scroll-margin-block-start" | "scroll-margin-bottom" | "scroll-margin-inline" | "scroll-margin-inline-end" | "scroll-margin-inline-start" | "scroll-margin-left" | "scroll-margin-right" | "scroll-margin-top" | "scroll-padding" | "scroll-padding-block" | "scroll-padding-block-end" | "scroll-padding-block-start" | "scroll-padding-bottom" | "scroll-padding-inline" | "scroll-padding-inline-end" | "scroll-padding-inline-start" | "scroll-padding-left" | "scroll-padding-right" | "scroll-padding-top" | "scroll-snap-align" | "scroll-snap-stop" | "scroll-snap-type" | "tab-size" | "table-layout" | "text-align" | "text-align-last" | "text-decoration" | "text-decoration-color" | "text-decoration-line" | "text-decoration-style" | "text-decoration-thickness" | "text-emphasis" | "text-indent" | "text-justify" | "text-orientation" | "text-overflow" | "text-shadow" | "text-transform" | "top" | "transform" | "transform-origin" | "transform-style" | "transition" | "transition-delay" | "transition-duration" | "transition-property" | "transition-timing-function" | "translate" | "unicode-bidi" | "direction" | "user-select" | "vertical-align" | "visibility" | "white-space" | "widows" | "width" | "word-break" | "word-spacing" | "word-wrap" | "writing-mode" | "z-index" 

    TYPE.2 : "btn" | "checkbox" | "colour" | "date" | "datetime-local" | "email" | "file" | "hidden" | "image" | "month" | "number" | "radio" | "range" | "reset" | "submit" | "tel" | "txt" | "time" | "url" | "week" | "password" | "submit" | "reset"

    TEXT_TAG.2: "text"

    TABLE_TAG.2: "table"

    TABLE_HEAD_TAG.2: "thead"

    TABLE_BODY_TAG.2: "tbody"

    CONTAINER_TAG.2: "section"

    COMPONENT_TAG.3 : "input" | "button" | "link" | "img"

    pure_style.2 : "$" STRING

    DOWNLOAD : "download"

    STRING : ESCAPED_STRING | /\"\"\"((.|\\n)*)\"\"\"/

    ID.1 :  /[a-zA-Z][a-zA-Z0-9]*/

    TITLE.2 : "title" 

    LANGUAGE.2 : "lang" 

    SCRIPT.2 : "script"

    BODY.2 : "body"

    FORM.2 : "form" 

    GET.2 : "get"

    POST.2 : "post" 

    _NL: /(\\r?\\n[\\t ]*)+/

    start : _NL* structure

    structure : header+ page

    header : (definition argument _NL) | (style_definition)

    page : BODY ":" _NL _INDENT command+ _DEDENT

    definition : (LANGUAGE ":") | (TITLE ":") | (SCRIPT ":")

    style_definition : (ID | pure_style) ":" _NL _INDENT (style _NL)+  _DEDENT

    container : container_command _NL _INDENT command+ _DEDENT

    command : text_command | container | form_command | component_command | table_command

    text_command : TEXT_TAG ("(" (ID) ")")? STRING _NL?

    container_command : CONTAINER_TAG ("(" (ID) ")")? ":"

    form_command : FORM method STRING _NL _INDENT command+ _DEDENT

    component_command : COMPONENT_TAG ("(" (ID) ")")? specification _NL? 

    table_command : TABLE_TAG ("(" (ID) ")")? ":" _NL _INDENT table_head table_body _DEDENT

    table_head: TABLE_HEAD_TAG ":" _NL _INDENT STRING+ _NL _DEDENT 

    table_body: TABLE_BODY_TAG ":" _NL _INDENT (table_item _NL?)+ _NL? _DEDENT

    table_item: STRING+ ","

    method : GET | POST

    specification : STRING STRING (DOWNLOAD)?| (TYPE argument)

    style : PROPERTY argument

    argument : STRING | ID


    %import common.ESCAPED_STRING
    %import common.WS_INLINE

    %declare _INDENT _DEDENT

    %ignore WS_INLINE"""

    parser = argparse.ArgumentParser(description='Processa um arquivo')
    parser.add_argument('arquivo', metavar='ARQUIVO', type=str,
                        help='o nome do arquivo a ser processado')
    args = parser.parse_args()

    nome_arquivo_completo = args.arquivo
    filename, extensao = os.path.splitext(nome_arquivo_completo)

    # with open("EwmGrammar.lark", "r") as grammar:
    #     ewmGrammar = grammar.read()

    ewmParser = Lark(ewmGrammar, start='start', propagate_positions=True, postlex=TreeIndenter())

    with open(nome_arquivo_completo, "r") as f:
        input = f.read()

    tree = ewmParser.parse(input)

    output = EwmTransformer().transform(tree)

    with open("out.json", "w") as outfile:
        json.dump(output, outfile, indent=2)

    with open('out.json', 'r') as file:
        ast = json.load(file)

    code_gen = CodeGenerator(ast)

    code_gen.generate_html(filename + ".html")

    os.remove("./out.json")

class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

if __name__ == "__main__":
    main()