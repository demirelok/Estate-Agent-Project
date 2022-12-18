
from apartment import Apartment
from purchase import Purchase

class ApartmentPurchase(Apartment, Purchase):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)