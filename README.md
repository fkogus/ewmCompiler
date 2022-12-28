# Compilador para a linguagem EWM (Easy Webpage Maker)

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

Para gerar a AST você deve rodar o arquivo EwmParser.py com o comando abaixo e a saída será algo como o exemplo a seguir

```
python3 EwmParser.py
```

```
start
  structure
    header
      definition        title
      argument  "login"
    header
      definition        lang
      argument  "pt-BR"
    header
      style_definition
        classe1
        style
          color
          argument      "black"
        style
          background
          argument      "bisque"
    header
      style_definition
        classe2
        style
          color
          argument      "black"
    header
      style_definition
        classe3
        style
          align
          argument      "center"
    page
      body
      command
        container
          container_command
            section
            classe1
          command
            component_command
              img
              specification
                "logo.png"
                "logo"
          command
            form_command
              form
              method    post
              "cadastrar/usar"
      command
        container
          container_command
            section
            classe3
          command
            component_command
              input
              specification
                txt
                argument        "Login"
          command
            component_command
              input
              specification
                password
                argument        "Senha"
          command
            component_command
              button
              specification
                submit
                argument        "Fazer Login"
          command
            container
              container_command section
              command
                text_command
                  text
                  classe2
                  "Ainda não tem cadastro?"
              command
                component_command
                  link
                  specification
                    "cadastrar.html"
                    "Cadastre-se"
```

#### Análise Semântica

#### Geração de Código

#### Live Server
