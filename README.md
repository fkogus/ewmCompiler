## Compilador para a linguagem EWM (Easy Webpage Maker)

### Definição

A linguagem Easy Web Page Maker (EWM) foi projetada para ter como entrada um arquivo no formato .ewm e vai gerar como saída uma página web devidamente formatada de maneira facilitada para o usuário.


### Gramática

A gramática da linguagem pode ser vista no arquivo EwmGrammar.lark

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

