class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "[{}, {}]".format(self.color, self.flavor)
