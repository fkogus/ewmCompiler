import json

def generate_header(header_data):
    header_html = ''

    for item in header_data:
        if 'def' in item:
            if item['def'] == 'title':
                header_html += f'<title>{item["arg"]}</title>\n'
            elif item['def'] == 'lang':
                header_html += f'<meta http-equiv="Content-Language" content="{item["arg"]}" />\n'
            elif item['def'] == 'script':
                header_html += f'<script src="{item["arg"]}" type="text/javascript"></script>\n'
        elif 'style_def' in item:
            for style_item in item['style_def']:
                style = ';'.join([f'{s["property"]}:{s["argument"]}' for s in style_item['style']])
                header_html += f'<style>.{style_item["id"]}{{{style}}}</style>\n'

    return header_html


def generate_container(c):

    div_callback = False

    container = ''

    for item in c:

        if 'container' in item:
            container += generate_container(item['container'])
            continue

        if item['type'] == 'container':
            container += "<div "
            if 'class' in item:
                container += 'class = \"' + item['class'] + '\">\n'
            else:
                container += ">\n"
            div_callback = True

        elif item['type'] == 'component':
            if item['command'] == 'img':
                container += '<img src=\"' + item['spec'][0] + '\" alt=\"' + item['spec'][1] + '\">\n'

            elif item['command'] == 'input':
                container += '<input type=\"' + __get_input_type__(item['spec']['type']) + '\"> ' + item['spec']['arg'] + ' </input>\n'
            
            elif item['command'] == 'button':
                container += '<button type=\"' + item['spec']['type'] + '\"> ' + item['spec']['arg'] + ' </button>\n'

            elif item['command'] == 'link':
                container += '<a href=\"' + item['spec'][0] + "\"> " + item['spec'][1] + ' </a>\n'

        elif item['type'] == 'form':
            container += '<form action=\"' + item['arg'] + '\" method=\"' + item['method'] + '\">\n'

            container += generate_container(item['content'])

            container += '\n</form>\n'

        elif item['type'] == 'text':
            if 'class' in item:
                container += '<p class=\"' + item['class'] + '\">\n'
            else:
                container += '<p>\n'
            container += item['arg'] + '\n</p>'

        elif item['type'] == 'table':
            container += generate_table(item)

    if div_callback:
        container += '</div>'

    return container

def generate_table(data):
    table_html = '<table>'

    # Add table header to table
    table_html += '<thead><tr>'
    for header in data['thead']['values']:
        table_html += f'<th>{header}</th>'
    table_html += '</tr></thead>'

    # Add table body to table
    table_html += '<tbody>'
    for item in data['tbody']['items']:
        table_html += '<tr>'
        for value in item:
            table_html += f'<td>{value}</td>'
        table_html += '</tr>'
    table_html += '</tbody>'

    table_html += '</table>'
    return table_html


def __get_input_type__(t):
    if t == 'txt':
        return 'text'
    else:
        return t
    

        

import json

ast = {}

with open('out.json', 'r') as file:
    ast = json.load(file)

# Generate the header and CSS code
header_code = generate_header(ast[0]['header'])

# Create a template HTML document
html_template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  {header_code}
</head>
<body>
  {page_content}
</body>
</html>
"""

# Insert the generated code into the HTML document
# html_document = html_template.format(
#     title=ast[0]['header'][0]['arg'],
#     header_code=header_code,
#     css_code=''
# )

page = ''

page_json = ast[0]['page']['commands']#[0]['container']

for a in page_json:
    page += generate_container(a['container'])

# page += generate_container(page_json)

html_document = html_template.format(
    title=ast[0]['header'][0]['arg'],
    header_code=header_code,
    css_code='',
    page_content=page
)

# print(page_json)

with open('teste.html', 'w') as teste:
    print(html_document, file=teste)

