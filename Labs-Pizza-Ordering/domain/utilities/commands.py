class Command:
    def execute(self):
        raise NotImplementedError

class PlaceOrderCommand(Command):
    def __init__(self, facade, customer, size, crust, toppings):
        self.facade = facade
        self.customer = customer
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def execute(self):
        self.facade.order_custom_pizza(self.customer, self.size, self.crust, self.toppings)

class PlaceClassicOrderCommand(Command):
    def __init__(self, facade, customer, pizzatype):
        self.facade = facade
        self.customer = customer
        self.pizzatype = pizzatype

    def execute(self):
        self.facade.order_classic_pizza(self.customer, self.pizzatype)

