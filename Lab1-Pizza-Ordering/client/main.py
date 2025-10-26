from domain.factory.singleton import PizzaOrderManager
from domain.factory.pizza_factory import PizzaFactory
from domain.builder import PizzaBuilder

def print_orders(order_list):
    for idx, order in enumerate(order_list, 1):
        customer = order.get("customer")
        pizza = order.get("pizza")
        print(f"Order {idx}:")
        print(f"  Customer: {customer}")
        print(f"  Pizza: {pizza}")
        print("-" * 30)

# Use Factory to create pizzas
pizza1 = PizzaFactory.create_pizza("margherita")

# Use Builder for a custom pizza
builder = PizzaBuilder().set_size("Large").add_topping("mushrooms").add_topping("chicken")
pizza2 = builder.build()

# Manage orders with Singleton
manager = PizzaOrderManager()
manager.add_order({"customer": "Alice", "pizza": pizza1})
manager.add_order({"customer": "Bob", "pizza": pizza2})

print("Current Pizza Orders:")
print_orders(manager.list_orders())
