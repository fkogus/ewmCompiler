GRAMMAR = '''
    @@grammar :: EWM

    @@keyword :: color  height  width border background align
    @@keyword :: section text input button link img
    @@keyword :: text password submit title lang body form get post

    @@parseinfo :: False

    structure = {header}+ page $;

    header = definition argument | {styleDefinition}+;

    page = BODY ':' {command}+ ;

    definition = (LANGUAGE ':') | (TITLE ':') ;

    styleDefinition = argument ':' {style}+ ;

    command = styleCommand | actionCommand | containerCommand ;

    containerCommand = tag:TAG spec:specification ;

    actionCommand = FORM method:method arg:argument ;

    method = GET | POST ;
    
    styleCommand = tag:TAG '(' ({style}+ | arg:argument) ')' spec:specification ;

    specification = arg:{argument}+ | (type:TYPE arg:argument) | {} ;
 
    style = prop:PROPERTY arg:argument ;

    argument = STRING | ID ;

    PROPERTY = 'color' | 'height' | 'width' | 'border' | 'background' | 'align' ;

    TAG = 'section' | 'text' | 'input' | 'button' | 'link' | 'img' ;

    TYPE = 'text' | 'password' | 'submit' ;

    STRING = /\"[^\"]*\"/ ;

    @name
    ID =  ?"[a-zA-Z][a-zA-Z0-9]*" ;

    TITLE = 'title' ;

    LANGUAGE = 'lang' ;

    BODY = 'body' ;

    FORM = 'form' ;

    GET = 'get';

    POST = 'post' ;



'''


def main():
    import pprint
    import json
    from tatsu import parse
    from tatsu.util import asjson
    from tatsu.tokenizing import Tokenizer

    ewm_file = open('example.ewm', "r")

    ex = ewm_file.read()

    ast = parse(GRAMMAR, ex, start='structure')
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print()

    ewm_file.close()

    print('JSON')
    print(json.dumps(asjson(ast), indent=2))
    print()


if __name__ == '__main__':
    main()