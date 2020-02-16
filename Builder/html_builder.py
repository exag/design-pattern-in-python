from Builder.builder import Builder


class HtmlBuilder(Builder):
    file_name = ''

    def make_title(self, title):
        self.file_name = title + '.html'
        with open(self.file_name, 'w') as f:
            html = '''<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{0}</h1>'''
            html = html.format(title)
            f.write(html)

    def make_string(self, string):
        with open(self.file_name, 'a') as f:
            html = '''
        <p>{0}</p>'''
            html = html.format(string)
            f.write(html)

    def make_items(self, items):
        with open(self.file_name, 'a') as f:
            html = '''
        <ul>'''
            for item in items:
                html += '''
            <li>{0}</li>'''.format(item)
            html += '''
        </ul>'''
            f.write(html)

    def close(self):
        with open(self.file_name, 'a') as f:
            html = '''
    </body>
</html>'''
            f.write(html)

    def get_result(self):
        return self.file_name
