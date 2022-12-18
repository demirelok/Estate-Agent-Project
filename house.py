
from property import Property
from utility import getValidInput


class House(Property):
    def __init__(self, number_stories='', garage='', fence='', pool='', *args, **kwargs):
        super(House, self).__init__(*args, **kwargs)
        self.pool = pool
        self.fence = fence
        self.garage = garage
        self.number_stories = number_stories

    def display(self):
        super(House, self).display()
        print(f'Number of stories: {self.number_stories}\n'
              f'Garage: {self.garage}\n'
              f'Fence: {self.fence}\n'
              f'Pool: {self.pool}\n')

    def prompt_init():
        parent_init = Property.prompt_init()
        number_stories = input("How many stories do you prefer: ")
        garage = getValidInput("Do you want to attach garage?", ("attached", "detached", "none"))
        fence = getValidInput("Do you want to attach fence", ("yes", "no"))
        pool = getValidInput("Do you want to attach pool", ("yes", "no"))

        parent_init.update(
            {"number_stories": number_stories, "garage": garage, "fence": fence, "pool": pool}
        )

        return parent_init
    
    prompt_init = staticmethod(prompt_init)