from course01.fruits.Fruit import Fruit


class Apple(Fruit):

    def __str__(self):
        return "Apple: " + super().__str__()
