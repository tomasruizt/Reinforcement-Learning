class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "Card{{name: {}, value: {}}}".format(self.name, self.value)
