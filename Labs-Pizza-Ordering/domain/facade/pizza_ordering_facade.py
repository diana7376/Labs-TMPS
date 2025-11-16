from domain.factory.pizza_factory import PizzaFactory
from domain.builder import PizzaBuilder
from domain.factory.singleton import PizzaOrderManager
from domain.models.decorator import ToppingDecorator

class PizzaOrderingFacade:
    def __init__(self):
        self.manager = PizzaOrderManager()

    def order_classic_pizza(self, customer, pizza_type, extra_toppings=None):
        pizza = PizzaFactory.create_pizza(pizza_type)
        # Apply Decorator for extra toppings
        if extra_toppings:
            for topping in extra_toppings:
                pizza = ToppingDecorator(pizza, topping)
        self.manager.add_order({"customer": customer, "pizza": pizza})
        return pizza

    def order_custom_pizza(self, customer, size, crust, toppings):
        builder = PizzaBuilder()
        builder.set_size(size)
        builder.set_crust(crust)
        pizza = builder.build()
        # Decorate with all selected toppings, one by one
        for topping in toppings:
            pizza = ToppingDecorator(pizza, topping)
        self.manager.add_order({"customer": customer, "pizza": pizza})
        return pizza

    def get_orders(self):
        return self.manager.list_orders()
