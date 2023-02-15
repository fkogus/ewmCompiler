from lark import Transformer, Tree

class EwmTransformer(Transformer):
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
            return items
    
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
        cmd = {'type': 'form', 'command': items[0].value, 'method': items[1], 'arg': items[2].value.replace("\"", "")}

        return cmd

    
    def component_command(self, items):
        cmd = {'type': 'component', 'command': items[0].value}

        if type(items[1]) == dict and len(items) > 2:
            cmd['style'] = items[1]
            cmd['spec'] = items[2]
        elif type(items[1]) != list and len(items) > 2:
            cmd['class'] = items[1].value
            cmd['spec'] = items[2]
        else:
            cmd['spec'] = items[1]

        return cmd

    def specification(self, items):
        spec = {}
        if items[0].type == "TYPE":
            spec['type'] = items[0].value
            spec['arg'] = items[1]
            return spec
        else:
            strings = []
            for i in range(len(items)):
                strings.append(items[i].value.replace("\"", ""))
            return strings

    def argument(self, items):

        argument = items[0].value.replace("\"", "")

        return argument

    def method(self, items):
        return items[0].value
    
    def definition(self, items):
        return items[0].value

    def container(self, items):
        return {'container': items}

