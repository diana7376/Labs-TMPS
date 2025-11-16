from domain.facade.pizza_ordering_facade import PizzaOrderingFacade
from domain.utilities.email_adapter import EmailAdapter
from domain.utilities.notification_interface import NotificationService

def print_orders(order_list):
    for idx, order in enumerate(order_list, 1):
        customer = order.get("customer")
        pizza = order.get("pizza")
        print(f"Order {idx}:")
        print(f"  Customer: {customer}")
        print(f"  Pizza: {pizza}")
        print("-" * 30)
facade = PizzaOrderingFacade(notifier=EmailAdapter())
facade.order_custom_pizza("Bob", "Large", "Thin", ["pepperoni", "mushrooms"])
facade.order_classic_pizza("Alice", "margherita")

print("Current Pizza Orders:")
print_orders(facade.get_orders())
