
from house import House
from purchase import Purchase

class HousePurchase(House, Purchase):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)