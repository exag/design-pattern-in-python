import sys

from Builder.director import Director
from Builder.html_builder import HtmlBuilder
from Builder.text_builder import TextBuilder


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
        exit()

    if args[0] == 'plain':
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_result()
        print(result)

    if args[0] == 'html':
        html_builder = HtmlBuilder()
        director = Director(html_builder)
        director.construct()
        file_name = html_builder.get_result()
        print(file_name + 'が作成されました。')


def usage():
    print('Usage: main("plain")     プレーンテキストで文書作成')
    print('Usage: main("html")      HTMLファイルで文書作成')


if __name__ == '__main__':
    main()
