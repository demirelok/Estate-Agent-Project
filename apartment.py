
from property import Property
from utility import getValidInput


class Apartment(Property):
    def __init__(self, balcony='', laundry='', *args, **kwargs):
        super(Apartment, self).__init__(*args, **kwargs)
        self.laundry = laundry
        self.balcony = balcony

    def display(self):
        super(Apartment, self).display()
        print('Apartment Information')
        print('=======================')
        print(f'Balcony: {self.balcony}')
        print(f'Laundry: {self.laundry}')

    def prompt_init():
        parent_init = Property.prompt_init()
        balcony = getValidInput("Does apartment have a balcony?", ("yes", "no"))
        laundry = getValidInput("Which payment do you prefer for laundry?", ("coin", "credit card", "none"))

        parent_init.update(
            {"laundry": laundry, "balcony": balcony}
        )

        return parent_init

    prompt_init = staticmethod(prompt_init)