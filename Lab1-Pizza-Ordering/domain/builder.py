from domain.models.pizza import Pizza

class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.size = "Medium"
        self.toppings = []
        self.crust = "Classic"

    def set_size(self, size):
        self.size = size
        return self

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self

    def set_crust(self, crust):
        self.crust = crust
        return self

    def build(self):
        pizza = Pizza(self.size, self.crust, self.toppings)
        self.reset()
        return pizza
