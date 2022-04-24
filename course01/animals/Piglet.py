class Piglet:
    """ Piglet class description
        @author evgeniy.scherbakov@gmail.com
    """

    name = "piglet"
    years = 0

    def __init__(self, name, years):
        self.name = name
        self.years = years

    def __str__(self) -> str:
        return "Piglet [{}, {}]".format(self.name, self.years)

    def speak(self):
        """
         print greeting piglet
        """
        print("Oink! I'm {}! Oink! I'm {} years old.".format(self.name, self.pig_years()))

    def pig_years(self):
        """
        Calculate man's age from piglet age
        :return: man's age equivalent
        """
        return self.years * 18
