## Compilador para a linguagem EWM (Easy Webpage Maker)

### Definição

A linguagem Easy Web Page Maker (EWM) foi projetada para ter como entrada um arquivo no formato .ewm e vai gerar como saída uma página web devidamente formatada de maneira facilitada para o usuário.


### Gramática

A gramática da linguagem pode ser vista no arquivo EwmGrammar.lark

Uma entrada válida no formato .ewm encontra-se abaixo

```
title:"login"
lang:"pt-BR"
classe1 : 
    color "black" 
    background "bisque"
classe2 : 
    color "black"
classe3 :
    align "center"
body : 
    section (classe1):
        img "logo.png" "logo"
        form post "cadastrar/usar"
    section (classe3):
        input txt "Login" 
        input password "Senha"
        button submit "Fazer Login"
        section:
            text (classe2) "Ainda não tem cadastro?" 
            link "cadastrar.html" "Cadastre-se"
```

### Código

Para todo o processo do Compilador, bem como Análise Léxica, Sintática, Semântica e Geração de Código foi realizada com auxílio de uma biblioteca de Python chamada Lark, que é capaz de analisar qualquer gramática sem contexto. Para fazer a instalação você deve rodar em seu terminal o comando abaixo

```
pip install lark
```
#### Análise Léxica e Sintática

Para gerar a AST você deve rodar o arquivo EwmParser.py com o comando abaixo e um arquivo out.json será gerado contendo algo como o exemplo a seguir

```
python3 EwmParser.py
```

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

#### Live Server
