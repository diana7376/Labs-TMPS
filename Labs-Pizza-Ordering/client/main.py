import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.facade.pizza_ordering_facade import PizzaOrderingFacade
from domain.factory.singleton import PizzaOrderManager
from domain.utilities.email_adapter import EmailAdapter
from domain.utilities.sms_adapter import SMSAdapter
from domain.utilities.commands import PlaceOrderCommand, PlaceClassicOrderCommand
from domain.utilities.strategy import HomeDeliveryStrategy, PickupStrategy

# ----- Observer setup -----
manager = PizzaOrderManager()
email_observer = EmailAdapter()
sms_observer = SMSAdapter()
manager.register_observer(email_observer)
manager.register_observer(sms_observer)

# ----- Facade and Command pattern usage -----
facade = PizzaOrderingFacade(notifier=None)

commands = [
    PlaceOrderCommand(facade, "Bob", "Large", "Thin", ["pepperoni", "mushrooms"]),
    PlaceClassicOrderCommand(facade, "Alice", "margherita")
]

for cmd in commands:
    cmd.execute()

# ----- Utility function for showing orders -----
def print_orders(order_list):
    for idx, order in enumerate(order_list, 1):
        customer = order["customer"]
        pizza = order["pizza"]
        print(f"Order {idx}")
        print(f" Customer: {customer}")
        print(f" Pizza: {pizza}")
        print("-" * 30)

print("\nCurrent Pizza Orders:")
print_orders(manager.list_orders())

# ----- Strategy pattern usage -----
# Example: Deliver Bob's order via home delivery, Alice's via pickup

facade.set_delivery_strategy(HomeDeliveryStrategy())
facade.deliver_order("Bob")

facade.set_delivery_strategy(PickupStrategy())
facade.deliver_order("Alice")
