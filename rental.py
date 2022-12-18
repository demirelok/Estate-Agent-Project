
from property import Property
from utility import getValidInput

class Rental(Property):
    def __init__(self, furnished='', extras='', rent='', *args, **kwargs):
        super(Rental, self).__init__(*args, **kwargs)
        self.rent = rent
        self.extras = extras
        self.furnished = furnished

    def display(self):
        super(Rental, self).display()
        print(f"Rental Details\n"
              f"===============\n"
              f"Rent: {self.rent}\n"
              f"Furnished: {self.furnished}\n"
              f"Extras: {self.extras}\n")

    def prompt_init():
        return dict(
            furnished=getValidInput("Is property furnished?", ("yes", "no")),
            extras=input("What are the estimated extras: "),
            rent=input("What is the estimated montly rent: ")
        )

    prompt_init = staticmethod(prompt_init)