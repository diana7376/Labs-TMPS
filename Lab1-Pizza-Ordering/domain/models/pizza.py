class Pizza:
    def __init__(self, size, crust, toppings):
        self.size = size
        self.crust = crust
        self.toppings = toppings

class Margherita(Pizza):
    def __init__(self):
        super().__init__('Medium', 'Classic', ['mozzarella', 'basil'])

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__('Large', 'Thin', ['pepperoni', 'mozzarella'])
