
from apartment import Apartment
from rental import Rental

class ApartmentRental(Apartment, Rental):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

