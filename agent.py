
from purchaseHouse import HousePurchase
from purchaseApartment import ApartmentPurchase
from houseRental import HouseRental
from apartmentRental import ApartmentRental
from utility import getValidInput

class Agent:
    def __init__(self):
        self.property_list = []

    def display_property_list(self):
        for property in self.property_list:
            property.display()

    process_type = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        property_type = getValidInput("What type of property do you want?", ("house", "apartment"))
        payment_type = getValidInput("What payment type do you prefer?", ("purchase", "rental"))

        property_class = self.process_type[(property_type, payment_type)]
        init_args = property_class.prompt_init()
        self.property_list.append(property_class(**init_args))

agent = Agent()
agent.add_property()
agent.display_property_list()