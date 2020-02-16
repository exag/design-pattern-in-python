from io import StringIO

from Builder.builder import Builder


class TextBuilder(Builder):
    buffer = StringIO()

    def make_title(self, title):
        self.buffer.write('==============================\n')
        self.buffer.write('「{}」'.format(title))
        self.buffer.write('\n')

    def make_string(self, string):
        self.buffer.write('■{}\n'.format(string))
        self.buffer.write('\n')

    def make_items(self, items):
        for item in items:
            self.buffer.write('\t・{}\n'.format(item))
        self.buffer.write('\n')

    def close(self):
        self.buffer.write('==============================\n')

    def get_result(self):
        return self.buffer.getvalue()
