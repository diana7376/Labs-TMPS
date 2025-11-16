class PizzaDecorator:
    def __init__(self, pizza):
        self.pizza = pizza

    def __str__(self):
        return str(self.pizza)


class ToppingDecorator(PizzaDecorator):
    def __init__(self, pizza, topping):
        super().__init__(pizza)
        self.topping = topping

    def __str__(self):
        base = str(self.pizza)
        if hasattr(self.pizza, "toppings"):
            all_toppings = self.pizza.toppings + [self.topping]
        else:
            all_toppings = [self.topping]
        # Customize representation as needed for your pizza class:
        return f"{base} + {self.topping}"
