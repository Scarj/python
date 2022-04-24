from course01.fruits.Fruit import Fruit


class Grape(Fruit):

    def __str__(self):
        return "Grape: " + super().__str__()
