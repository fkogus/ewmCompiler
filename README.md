## Compilador para a linguagem EWM (Easy Webpage Maker)

### Definição

A linguagem Easy Web Page Maker (EWM) foi projetada para ter como entrada um arquivo no formato .ewm e vai gerar como saída uma página web devidamente formatada de maneira facilitada para o usuário.


### Gramática

A gramática da linguagem pode ser vista no arquivo EwmGrammar.lark

```
PROPERTY.2 : "accent-color" | "align-content" | "align-items" | "align-self" | "all" | "animation" | "animation-delay" | "animation-direction" | "animation-duration" | "animation-fill-mode" | "animation-iteration-count" | "animation-name" | "animation-play-state" | "animation-timing-function" | "aspect-ratio" | "backdrop-filter" | "backface-visibility" | "background" | "background-attachment" | "background-blend-mode" | "background-clip" | "background-color" | "background-image" | "background-origin" | "background-position" | "background-position-x" | "background-position-y" | "background-repeat" | "background-size" | "block-size" | "border" | "border-block" | "border-block-color" | "border-block-end-color" | "border-block-end-style" | "border-block-end-width" | "border-block-start-color" | "border-block-start-style" | "border-block-start-width" | "border-block-style" | "border-block-width" | "border-bottom" | "border-bottom-color" | "border-bottom-left-radius" | "border-bottom-right-radius" | "border-bottom-style" | "border-bottom-width" | "border-collapse" | "border-color" | "border-image" | "border-image-outset" | "border-image-repeat" | "border-image-slice" | "border-image-source" | "border-image-width" | "border-inline" | "border-inline-color" | "border-inline-end-color" | "border-inline-end-style" | "border-inline-end-width" | "border-inline-start-color" | "border-inline-start-style" | "border-inline-start-width" | "border-inline-style" | "border-inline-width" | "border-left" | "border-left-color" | "border-left-style" | "border-left-width" | "border-radius" | "border-right" | "border-right-color" | "border-right-style" | "border-right-width" | "border-spacing" | "border-style" | "border-top" | "border-top-color" | "border-top-left-radius" | "border-top-right-radius" | "border-top-style" | "border-top-width" | "border-width" | "bottom" | "box-decoration-break" | "box-reflect" | "box-shadow" | "box-sizing" | "break-after" | "break-before" | "break-inside" | "caption-side" | "caret-color" | "@charset" | "clear" | "clip" | "color" | "column-count" | "column-fill" | "column-gap" | "column-rule" | "column-rule-color" | "column-rule-style" | "column-rule-width" | "column-span" | "column-width" | "columns" | "content" | "counter-increment" | "counter-reset" | "cursor" | "direction" | "display" | "empty-cells" | "filter" | "flex" | "flex-basis" | "flex-direction" | "flex-flow" | "flex-grow" | "flex-shrink" | "flex-wrap" | "float" | "font" | "@font-face" | "font-family" | "font-feature-settings" | "font-kerning" | "font-size" | "font-size-adjust" | "font-stretch" | "font-style" | "font-variant" | "font-variant-caps" | "font-weight" | "gap" | "grid" | "grid-area" | "grid-auto-columns" | "grid-auto-flow" | "grid-auto-rows" | "grid-column" | "grid-column-end" | "grid-column-gap" | "grid-column-start" | "grid-gap" | "grid-row" | "grid-row-end" | "grid-row-gap" | "grid-row-start" | "grid-template" | "grid-template-areas" | "grid-template-columns" | "grid-template-rows" | "hanging-punctuation" | "height" | "hyphens" | "image-rendering" | "@import" | "inline-size" | "inset" | "inset-block" | "inset-block-end" | "inset-block-start" | "inset-inline" | "inset-inline-end" | "inset-inline-start" | "isolation" | "justify-content" | "justify-items" | "justify-self" | "@keyframes" | "left" | "letter-spacing" | "line-height" | "list-style" | "list-style-image" | "list-style-position" | "list-style-type" | "margin" | "margin-block" | "margin-block-end" | "margin-block-start" | "margin-bottom" | "margin-inline" | "margin-inline-end" | "margin-inline-start" | "margin-left" | "margin-right" | "margin-top" | "mask-image" | "mask-mode" | "mask-origin" | "mask-position" | "mask-repeat" | "mask-size" | "max-height" | "max-width" | "@media" | "max-block-size" | "max-inline-size" | "min-block-size" | "min-inline-size" | "min-height" | "min-width" | "mix-blend-mode" | "object-fit" | "object-position" | "offset" | "offset-anchor" | "offset-distance" | "offset-path" | "offset-rotate" | "opacity" | "order" | "orphans" | "outline" | "outline-color" | "outline-offset" | "outline-style" | "outline-width" | "overflow" | "overflow-anchor" | "overflow-wrap" | "overflow-x" | "overflow-y" | "overscroll-behavior" | "overscroll-behavior-block" | "overscroll-behavior-inline" | "overscroll-behavior-x" | "overscroll-behavior-y" | "padding" | "padding-block" | "padding-block-end" | "padding-block-start" | "padding-bottom" | "padding-inline" | "padding-inline-end" | "padding-inline-start" | "padding-left" | "padding-right" | "padding-top" | "page-break-after" | "page-break-before" | "page-break-inside" | "paint-order" | "perspective" | "perspective-origin" | "place-content" | "place-items" | "place-self" | "pointer-events" | "position" | "quotes" | "resize" | "right" | "rotate" | "row-gap" | "scale" | "scroll-behavior" | "scroll-margin" | "scroll-margin-block" | "scroll-margin-block-end" | "scroll-margin-block-start" | "scroll-margin-bottom" | "scroll-margin-inline" | "scroll-margin-inline-end" | "scroll-margin-inline-start" | "scroll-margin-left" | "scroll-margin-right" | "scroll-margin-top" | "scroll-padding" | "scroll-padding-block" | "scroll-padding-block-end" | "scroll-padding-block-start" | "scroll-padding-bottom" | "scroll-padding-inline" | "scroll-padding-inline-end" | "scroll-padding-inline-start" | "scroll-padding-left" | "scroll-padding-right" | "scroll-padding-top" | "scroll-snap-align" | "scroll-snap-stop" | "scroll-snap-type" | "tab-size" | "table-layout" | "text-align" | "text-align-last" | "text-decoration" | "text-decoration-color" | "text-decoration-line" | "text-decoration-style" | "text-decoration-thickness" | "text-emphasis" | "text-indent" | "text-justify" | "text-orientation" | "text-overflow" | "text-shadow" | "text-transform" | "top" | "transform" | "transform-origin" | "transform-style" | "transition" | "transition-delay" | "transition-duration" | "transition-property" | "transition-timing-function" | "translate" | "unicode-bidi" | "direction" | "user-select" | "vertical-align" | "visibility" | "white-space" | "widows" | "width" | "word-break" | "word-spacing" | "word-wrap" | "writing-mode" | "z-index" 

TYPE.2 : "btn" | "checkbox" | "colour" | "date" | "datetime-local" | "email" | "file" | "hidden" | "image" | "month" | "number" | "radio" | "range" | "reset" | "submit" | "tel" | "txt" | "time" | "url" | "week" | "password" | "submit" | "reset"

TEXT_TAG.2: "text"

TABLE_TAG.2: "table"

TABLE_HEAD_TAG.2: "thead"

TABLE_BODY_TAG.2: "tbody"

CONTAINER_TAG.2: "section"

COMPONENT_TAG.3 : "input" | "button" | "link" | "img"

pure_style.2 : "$" STRING

DOWNLOAD : "download"

STRING : ESCAPED_STRING | /\"\"\"((.|\n)*)\"\"\"/

ID.1 :  /[a-zA-Z][a-zA-Z0-9]*/

TITLE.2 : "title" 

LANGUAGE.2 : "lang" 

SCRIPT.2 : "script"

BODY.2 : "body"

FORM.2 : "form" 

GET.2 : "get"

POST.2 : "post" 

_NL: /(\r?\n[\t ]*)+/

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

%ignore WS_INLINE
```

Uma entrada válida no formato .ewm encontra-se abaixo

```
title:"home"
lang:"pt-BR"
home :
    background "#d7dfea"
header :
    display "flex"
    flex-direction "row"
    justify-content "space-between"
    padding "20px 60px"
nav :
    display "flex"
    flex-direction "row"
    column-gap "30px"
$ "a" :
    color "black"
    text-decoration "none"
active :
    text-decoration "underline"
$ "img" :
    max-width "100px"
h3 :
    font-size "30px"
    font-weight "bold"
main :
    padding "20px 60px"
features :
    padding "20px 60px"
cardgrid :
    display "flex"
    flex-direction "row"
    flex-wrap "wrap"
    justify-content "space-between"
codebox :
    background "black"
    color "#efefef"
    padding "20px"
    border-radius "10px"
    font-family "'Courier New'"
card :
    height "auto"
    width "30%"
    background "#e8f7fa"
    border "solid 2px"
    border-color "#e8f7fa"
    border-radius "25px"
    font-size "0.85rem"
    text-align "start"
    padding "10px"
    margin-bottom "20px"
cardtitle :
    font-weight "bold"
    margin-bottom "0.2rem"
    text-decoration "underline"

body :
    section (home):
        section (header):
            img "logo.png" "logo"
            section (nav):
                section (item):
                    link "https://cyan-lang.org/" "about"
                section (item):
                    link "https://compiler.cyan-lang.org" "compiler"
                section (item):
                    link "https://cyan-lang.org/docs" "docs"
                section (item):
                    link "https://cyan-lang.org/downloads/" "downloads"
                section (item):
                    link "https://cyan-lang.org/examples/" "examples"
        section (main):
            text (h3) "The Cyan Object-oriented Language"
            text (p) "Cyan is a statically-typed and prototype-based language for the JVM. The language has several innovations mainly in its Metaobject Protocol that allows tailoring the language to the developer’s goals. It supports all the expected features of modern languages and much more."
            text (p) "Below is the “Hello world” program. Soon there will be a short Cyan course."
            section (codebox):
                text (code) "package main"
                text (code) "object Program"
                text (code) "func run {"
                text (code) "'Hello world' println"
                text (code) "}"
                text (code) "end"
        section (features):
            text (h3) "Features"
            section (cardgrid):
                section (card):
                    text (cardtitle) "Simplicity is the main goal"
                    text (small) "No bells and whistles, complex features are implemented using metaobjects, outside the language"
                section (card):
                    text (cardtitle) "Simplicity is the main goal"
                    text (small) "No bells and whistles, complex features are implemented using metaobjects, outside the language"
                section (card):
                    text (cardtitle) "Simplicity is the main goal"
                    text (small) "No bells and whistles, complex features are implemented using metaobjects, outside the language"
                section (card):
                    text (cardtitle) "Simplicity is the main goal"
                    text (small) "No bells and whistles, complex features are implemented using metaobjects, outside the language"
```

### Código

Para todo o processo do Compilador, bem como Análise Léxica, Sintática, Semântica e Geração de Código foi realizada com auxílio de uma biblioteca de Python chamada Lark, que é capaz de analisar qualquer gramática sem contexto. Para fazer a instalação você deve rodar em seu terminal o comando abaixo

```
pip install lark
```
#### Análise Léxica e Sintática

A AST é gerada automaticamente quando rodamos o arquivo EwmParser.py, mas ela tem o formato como o exemplo a seguir

```
[
  {
    "header": [
      {
        "def": "title",
        "arg": "login"
      },
      {
        "def": "lang",
        "arg": "pt-BR"
      },
      {
        "style_def": [
          {
            "id": "classe1",
            "style": [
              {
                "property": "color",
                "argument": "black"
              },
              {
                "property": "background",
                "argument": "bisque"
              }
            ]
          }
        ]
      },
      {
        "style_def": [
          {
            "id": "classe2",
            "style": [
              {
                "property": "color",
                "argument": "black"
              }
            ]
          }
        ]
      },
      {
        "style_def": [
          {
            "id": "classe3",
            "style": [
              {
                "property": "align",
                "argument": "center"
              }
            ]
          }
        ]
      }
    ],
    "page": {
      "body": "body",
      "commands": [
        [
          {
            "container": [
              {
                "type": "container",
                "command": "section",
                "class": "classe1"
              },
              [
                {
                  "type": "component",
                  "command": "img",
                  "spec": [
                    "logo.png",
                    "logo"
                  ]
                }
              ],
              [
                {
                  "type": "form",
                  "command": "form",
                  "method": "post",
                  "arg": "cadastrar/usar"
                }
              ]
            ]
          }
        ],
        [
          {
            "container": [
              {
                "type": "container",
                "command": "section",
                "class": "classe3"
              },
              [
                {
                  "type": "component",
                  "command": "input",
                  "spec": {
                    "type": "txt",
                    "arg": "Login"
                  }
                }
              ],
              [
                {
                  "type": "component",
                  "command": "input",
                  "spec": {
                    "type": "password",
                    "arg": "Senha"
                  }
                }
              ],
              [
                {
                  "type": "component",
                  "command": "button",
                  "spec": {
                    "type": "submit",
                    "arg": "Fazer Login"
                  }
                }
              ],
              [
                {
                  "container": [
                    {
                      "type": "container",
                      "command": "section"
                    },
                    [
                      {
                        "type": "text",
                        "command": "text",
                        "class": "classe2",
                        "arg": "Ainda n\u00c3\u00a3o tem cadastro?"
                      }
                    ],
                    [
                      {
                        "type": "component",
                        "command": "link",
                        "spec": [
                          "cadastrar.html",
                          "Cadastre-se"
                        ]
                      }
                    ]
                  ]
                }
              ]
            ]
          }
        ]
      ]
    }
  }
]
```

#### Análise Semântica

Para a análise semântica foram realizadas validações antes de concluir a geração da AST. As validações incluem o mapeamento de determinados tags e tokens como por exemplo: 

```
semantic_dict = {
    'button': ['button', 'submit', 'reset'],
    'input': ['button', 'checkbox', 'color', 'date', 'datetime-local', 'email', 'file', 'hidden', 'image', 'month', 'number', 'radio', 'range', 'reset', 'submit', 'tel', 'txt', 'time', 'url', 'week', 'password'],
}
```

Aqui temos os mapeamentos possíveis que a tag button e a tag input aceitam respectivamente.

Foram também mapeados os possíveis erros semânticos da gramática, utilizamos o WrongAttributeError do python, que é como qualquer exceção custom da linguagem, para mostrar os erros como o exemplo:


```
Parameter {param} do not match with attribute {attr} in {line}:{column}
```

Aqui por exemplo colocamos o parâmetro colour para a tag button, a tag não está mapeada para recebê-lo, portanto recebemos o erro:

```
WrongAttributeError: Parameter colour do not match with attribute button in 17:16
```


#### Geração de Código

Para a geração de código, alteramos o EwmParser para receber um ARQUIVO de parâmetro, assim gerando um arquivo .html no mesmo diretório rodado.

```
python3 EwmParser.py home.ewm 
```

Também fizemos um executável ewm, que permite executar qualquer arquivo ewm e gera um html de saída.

```
ewm home.ewm 
```

#### Live Server

É possível acompanhar as mudanças usando o Live Preview no vsCode para uma experiência melhor.

<img width="1680" alt="image" src="https://user-images.githubusercontent.com/44788970/229805703-930e75ea-efc6-4182-a09a-245ff2581cb5.png">

