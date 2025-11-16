class Pizza:
    def __init__(self, size, crust, toppings):
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def __str__(self):
        return f"Pizza(size={self.size}, crust={self.crust}, toppings={', '.join(self.toppings)})"

    __repr__ = __str__

class Margherita(Pizza):
    def __init__(self):
        super().__init__('Medium', 'Classic', ['mozzarella', 'basil'])

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__('Large', 'Thin', ['pepperoni', 'mozzarella'])
