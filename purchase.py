
from property import Property


class Purchase(Property):
    def __init__(self, price='', taxes='', *args, **kwargs):
        super(Purchase, self).__init__(*args, **kwargs)
        self.taxes = taxes
        self.price = price


    def display(self):
        super(Purchase, self).display()
        print(f'Purchase Details\n'
              f'==================\n'
              f'Estimated Taxes: {self.taxes}\n'
              f'Selling Price: {self.price}\n')

    def prompt_init():
        return dict(
            price=input("What is the selling price: "),
            taxes=input("What is the estimated taxes: ")
        )

    prompt_init = staticmethod(prompt_init)