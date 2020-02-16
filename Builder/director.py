class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.make_title('Greeting')
        self.builder.make_string('朝から昼にかけて')
        self.builder.make_items([
            'おはようございます。',
            'こんにちは。'
        ])
        self.builder.make_string('夜に')
        self.builder.make_items([
            'こんばんは。',
            'おやすみなさい。',
            'さようなら。'
        ])
        self.builder.close()
