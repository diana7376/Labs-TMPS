import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.factory.pizza_factory import PizzaFactory
from domain.models.builder import PizzaBuilder
from domain.factory.singleton import PizzaOrderManager
from domain.models.decorator import ToppingDecorator
from domain.utilities.notification_interface import NotificationService

class PizzaOrderingFacade:
    def __init__(self, notifier: NotificationService = None):
        self.manager = PizzaOrderManager()
        self.notifier = notifier
        self.delivery_strategy = None  # For Strategy pattern

    def set_delivery_strategy(self, strategy):
        """Assign a delivery strategy (Strategy pattern)"""
        self.delivery_strategy = strategy

    def deliver_order(self, customer):
        """Deliver the order for the given customer using the selected strategy."""
        # Find the first matching order for customer
        orders = self.manager.list_orders()
        order = next((o for o in orders if o["customer"] == customer), None)
        if order and self.delivery_strategy:
            self.delivery_strategy.deliver(order)
        else:
            print("Order or delivery strategy not found.")

    def order_classic_pizza(self, customer, pizzatype, extratoppings=None):
        """Order a classic pizza, optionally with extra toppings."""
        pizza = PizzaFactory.create_pizza(pizzatype)
        # Decorate pizza with extra toppings
        if extratoppings:
            for topping in extratoppings:
                pizza = ToppingDecorator(pizza, topping)
        # Save order with Observer notification
        self.manager.add_order(customer, pizza)
        if self.notifier:
            self.notifier.send_notification(customer, "Your classic pizza order is confirmed!")
        return pizza

    def order_custom_pizza(self, customer, size, crust, toppings):
        """Order a custom pizza by specifying size, crust, toppings."""
        builder = PizzaBuilder()
        builder.set_size(size)
        builder.set_crust(crust)
        pizza = builder.build()
        # Decorate pizza for each topping
        for topping in toppings:
            pizza = ToppingDecorator(pizza, topping)
        # Save order with Observer notification
        self.manager.add_order(customer, pizza)
        if self.notifier:
            self.notifier.send_notification(customer, "Your custom pizza order is confirmed!")
        return pizza

    def get_orders(self):
        return self.manager.list_orders()
