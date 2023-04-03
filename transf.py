from lark import Transformer, Tree
import sys
sys.path.append('errors')

from WrongAttributeError import WrongAttributeError
from WrongSpecError import WrongSpecError


class EwmTransformer(Transformer):

    errors = []

    semantic_dict = {'button': ['btn', 'submit', 'reset'],
    'input': ['btn', 'checkbox', 'colour', 'date', 'datetime-local', 'email', 'file', 'hidden', 'image', 'month', 'number', 'radio', 'range', 'reset', 'submit', 'tel', 'txt', 'time', 'url', 'week', 'password'],
    }

    def start(self, items):
        return items
    
    def structure(self, items):
        header = []
        for i in range(0,len(items)-1):
            header.append(items[i])
        
        return {'header': header, 'page': items[-1]}
    
    def header(self, items):
        if len(items) == 1:
            return {'style_def': items}
        else:
            return {'def': items[0], 'arg': items[1]}
    
    def definition(self, items):
        return str(items)
    
    def style_definition(self, items):

        style_def = {}

        if isinstance(items[0], str):
            style_def['id'] = items[0]
        else:
            style_def['id'] = items[0].value

        styles = []

        for i in range(1,len(items)):
            styles.append(items[i])

        style_def['style'] = styles

        return style_def

    
    def style(self, items):
        if type(items) == dict:
            return items
            
        style = {}
        
        style['property'] = items[0].value
        style['argument'] = items[1]


        return style

    
    def page(self, items):
        page = {'body': items[0].value}

        commmands = []

        for i in range(1,len(items)):
            commmands.append(items[i])

        page['commands'] = commmands

        return page

    
    def command(self, items):
        if type(items[0]) == Tree:
            return items[0].children
        else:
            return items[0]
    
    def text_command(self, items):
        cmd = {'type': 'text', 'command': items[0].value}

        if type(items[1]) == dict:
            cmd['style'] = items[1]
            cmd['arg'] = items[2]
        elif items[1].type == 'ID':
            cmd['class'] = items[1].value
            cmd['arg'] = items[2].value.replace("\"", "")
        else:
            cmd['arg'] = items[1]

        return cmd

    
    def container_command(self, items):
        cmd = {'type': 'container', 'command': items[0].value}

        if len(items) > 1 and type(items[1]) == dict :
            cmd['style'] = items[1]
        elif len(items) > 1:
            cmd['class'] = items[1].value

        return cmd
    
    def form_command(self, items):

        cmd = {'type': 'form', 'command': items[0].value, 'method': items[1], 'arg': items[2].value.replace("\"", ""), 'content': items[3:]}

        return cmd

    
    def component_command(self, items):
        cmd = {'type': 'component', 'command': items[0].value}

        pos_spec = 1

        if type(items[1]) == dict and len(items) > 2:
            cmd['style'] = items[1]
            cmd['spec'] = items[2][0]
            pos_spec = 2
        elif type(items[1]) != list and len(items) > 2:
            cmd['class'] = items[1].value
            cmd['spec'] = items[2][0]
            pos_spec = 2
        else:
            cmd['spec'] = items[1][0]

        try:
            if 'spec' in cmd:
                if 'type' in cmd['spec']:

                    if cmd['command'] == 'link':
                        if type(cmd['spec']) == dict:
                            raise WrongSpecError('link', items[pos_spec][1], items[pos_spec][2])
                        
                    if cmd['spec']['type'] not in self.semantic_dict[cmd['command']]:
                        raise WrongAttributeError(cmd['spec']['type'], cmd['command'], items[pos_spec][1], items[pos_spec][2])
        except Exception as e:
            self.errors.append(e)

        for e in self.errors:
            print(e)

        return cmd

    def specification(self, items):
        spec = {}
        if items[0].type == "TYPE":
            spec['type'] = items[0].value
            spec['arg'] = items[1]
            return (spec, items[0].line, items[0].column)
        else:
            strings = []
            for i in range(len(items)):
                strings.append(items[i].value.replace("\"", ""))
            return (strings, )

    def argument(self, items):

        argument = items[0].value.replace("\"", "")

        return argument

    def method(self, items):
        return items[0].value
    
    def definition(self, items):
        return items[0].value

    def container(self, items):
        return {'container': items}
    
    def table_command(self, items):
        
        dictionary = {}

        dictionary['type'] = 'table'

        if len(items) == 4:
            dictionary['class'] = items[1].value
            dictionary['thead'] = items[2]
            dictionary['tbody'] = items[3]

        else:
            dictionary['thead'] = items[1]
            dictionary['tbody'] = items[2]

        return dictionary
    
    def table_body(self, items):

        items_list = []

        for i in items[1:]:
            items_list.append(i)

        return {'component': 'tbody', 'items': items_list}
    
    def table_head(self, items):

        values = items[1:]

        values = [item.value for item in values]
        values = [item.replace("\"", "") for item in values]

        return {'component': 'thead', 'values': values}
    
    def table_item(self, items):
        values = items

        values = [item.value for item in values]
        values = [item.replace("\"", "") for item in values]

        return values
    
    def pure_style(self, items):

        return "$" + items[0]

