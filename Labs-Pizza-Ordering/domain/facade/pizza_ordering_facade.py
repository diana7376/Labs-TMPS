from ..factory.pizza_factory import PizzaFactory
from ..builder import PizzaBuilder
from ..factory.singleton import PizzaOrderManager
from ..models.decorator import ToppingDecorator
from ..utilities.notification_interface import NotificationService

class PizzaOrderingFacade:
    def __init__(self, notifier: NotificationService = None):
        """Initialize the facade. Accept an optional notifier instance (adapters subclassing NotificationService).

        - notifier: an instance providing send_notification(customer, message)
        """
        self.manager = PizzaOrderManager()
        self.notifier = notifier

    def order_classic_pizza(self, customer, pizza_type, extra_toppings=None):
        pizza = PizzaFactory.create_pizza(pizza_type)
        # Apply Decorator for extra toppings
        if extra_toppings:
            for topping in extra_toppings:
                pizza = ToppingDecorator(pizza, topping)
        self.manager.add_order({"customer": customer, "pizza": pizza})
        if self.notifier:
            self.notifier.send_notification(customer, "Your classic pizza order is confirmed!")
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
        if self.notifier:
            self.notifier.send_notification(customer, "Your custom pizza order is confirmed!")
        return pizza

    def get_orders(self):
        return self.manager.list_orders()
