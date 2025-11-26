# Pizza Ordering System — Design Patterns Lab

## Overview

This directory demonstrates implementations of common design patterns in Python using a simple pizza-ordering domain.

Code is organized into modules and packages (client interface, domain models, factories, etc.) to maintain a clear separation of concerns and modular design.

In this project we implemented the following design patterns: Singleton, Builder, Factory Method, Facade, Adapter, and Decorator.

---

## Project Structure

```
Labs-Pizza-Ordering/
│
├── client/
│    ├── __init__.py
│    └── main.py
├── domain/
│    ├── facade/
│    │     ├── __init__.py
│    │     └── pizza_ordering_facade.py
│    ├── factory/
│    │     ├── __init__.py
│    │     ├── pizza_factory.py
│    │     └── singleton.py
│    ├── models/
│    │     ├── __init__.py
│    │     ├── builder.py
│    │     ├── decorator.py
│    │     └── pizza.py
│    └── utilities/
│          ├── __init__.py
│          ├── email_adapter.py
│          ├── notification_interface.py
│          ├── order_observer.py
│          ├── sms_adapter.py
│          ├── strategy.py
│          ├── commands.py
│          └── builder.py
├── README.md
```

---

## Design Patterns Used

### 1. Singleton

**File:** `domain/factory/singleton.py`

**Description:**
The Singleton pattern ensures there is only one instance of a class for managing pizza orders (the `PizzaOrderManager`). This central manager collects all orders, preventing duplication and inconsistency.

**Key code:**
```python
class PizzaOrderManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.orders = []
        return cls._instance
```
**Usage:**
```python
manager = PizzaOrderManager()
manager.add_order({...})
```

---

### 2. Builder

**File:** `domain/builder.py`

**Description:**
The Builder pattern allows for step-wise and flexible creation of pizza objects. Users can set attributes (size, crust, toppings) in chainable steps, and construct the final pizza easily.

**Key code:**
```python
class PizzaBuilder:
    def set_size(self, size): ...
    def add_topping(self, topping): ...
    def set_crust(self, crust): ...
    def build(self): ...
```
**Usage:**
```python
pizza = PizzaBuilder().set_size("Large").add_topping("mushrooms").build()
```

---

### 3. Factory Method

**File:** `domain/factory/pizza_factory.py`

**Description:**
The Factory Method centralizes and encapsulates creation logic for different pizza types (Margherita, Pepperoni, etc.), returning concrete pizza objects based on a string parameter.

**Key code:**
```python
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        ...
```
**Usage:**
```python
pizza = PizzaFactory.create_pizza("margherita")
```

---

## Structural Patterns

To complement the creational patterns above, the following structural patterns were added to simplify the client API and enable extensibility.

### 1. Facade

**File:** `domain/facade/pizza_ordering_facade.py`

**Description:**
The Facade provides a simplified interface for placing pizza orders (classic or custom) without exposing the internal creation and composition steps. It orchestrates the Factory, Builder, Decorator, and the Singleton order manager and delegates notifications to adapters.

**Key code (concept):**
```python
class PizzaOrderingFacade:
    def __init__(self, notifier=None):
        self.manager = PizzaOrderManager()
        self.notifier = notifier

    def order_custom_pizza(self, customer, size, crust, toppings):
        builder = PizzaBuilder()
        builder.set_size(size).set_crust(crust)
        pizza = builder.build()
        for t in toppings:
            pizza = ToppingDecorator(pizza, t)
        self.manager.add_order({"customer": customer, "pizza": pizza})
        if self.notifier:
            self.notifier.send_notification(customer, "Your custom pizza order is confirmed!")
```

**Usage:**
```python
facade = PizzaOrderingFacade(notifier=EmailAdapter())
facade.order_custom_pizza("Bob", "Large", "Thin", ["pepperoni"])
```

### 2. Adapter

**Files:** `domain/utilities/notification_interface.py`, `domain/utilities/email_adapter.py`, `domain/utilities/sms_adapter.py`

**Description:**
The Adapter pattern is used to provide pluggable notification channels. `NotificationService` defines the interface and concrete adapters (Email, SMS) implement `send_notification(customer, message)`. The facade depends on the abstract interface, not concrete implementations.

**Key code (concept):**
```python
class NotificationService:
    def send_notification(self, customer, message):
        raise NotImplementedError

class EmailAdapter(NotificationService):
    def send_notification(self, customer, message):
        print(f"Email sent to {customer}: {message}")
```

**Usage:**
```python
notifier = EmailAdapter()
facade = PizzaOrderingFacade(notifier=notifier)
```

### 3. Decorator

**File:** `domain/models/decorator.py`

**Description:**
The Decorator adds responsibilities (extra toppings, presentation tweaks) to pizza objects at runtime by wrapping them. This keeps base pizza implementations unchanged while enabling flexible composition.

**Key code (concept):**
```python
class ToppingDecorator:
    def __init__(self, pizza, topping):
        self.pizza = pizza
        self.topping = topping
    def __str__(self):
        return str(self.pizza) + f" + {self.topping}"
```

**Usage:**
```python
pizza = PizzaFactory.create_pizza("margherita")
pizza = ToppingDecorator(pizza, "olives")
```

---


## Behavioral Design Patterns Implemented
### 1. Observer Pattern
Notifies all registered observers (such as email and SMS channels) whenever a new pizza order is added to the system.

Relevant code:

```python
# domain/factory/singleton.py

class PizzaOrderManager:
    def __init__(self):
        self.orders = []
        self.observers = []

    def add_order(self, customer, pizza):
        order = {"customer": customer, "pizza": pizza}
        self.orders.append(order)
        self.notify_observers(order, "placed")

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, order, event_type):
        for observer in self.observers:
            observer.update(order, event_type)
```

```python
# domain/utilities/email_adapter.py

from domain.utilities.order_observer import OrderObserver

class EmailAdapter(OrderObserver):
    def update(self, order, event_type):
        print(f"Email sent to {order['customer']}: Your pizza order {event_type}.")
```

### 2. Command Pattern
Encapsulates pizza ordering requests as command objects, allowing actions to be executed, logged, and managed uniformly.

Relevant code:

```python
# domain/utilities/commands.py

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
        self.facade.order_custom_pizza(
            self.customer, self.size, self.crust, self.toppings
        )
```

```python
# client/main.py

from domain.utilities.commands import PlaceOrderCommand

commands = [
    PlaceOrderCommand(facade, "Bob", "Large", "Thin", ["pepperoni", "mushrooms"]),
]

for cmd in commands:
    cmd.execute()
```

### 3. Strategy Pattern
Keeps delivery options flexible by allowing runtime selection of different strategies (e.g. home delivery or pickup).

Relevant code:

```python
# domain/utilities/strategy.py

class DeliveryStrategy:
    def deliver(self, order):
        raise NotImplementedError

class HomeDeliveryStrategy(DeliveryStrategy):
    def deliver(self, order):
        print(f"Home delivery: Delivering pizza to {order['customer']}")

class PickupStrategy(DeliveryStrategy):
    def deliver(self, order):
        print(f"Pickup: {order['customer']} will pick up the pizza.")
```

```python
# domain/facade/pizza_ordering_facade.py

class PizzaOrderingFacade:
    # ...
    def set_delivery_strategy(self, strategy):
        self.delivery_strategy = strategy

    def deliver_order(self, customer):
        order = next((o for o in self.manager.list_orders() if o["customer"] == customer), None)
        if order and self.delivery_strategy:
            self.delivery_strategy.deliver(order)
```

```python
# client/main.py

from domain.utilities.strategy import HomeDeliveryStrategy, PickupStrategy

facade.set_delivery_strategy(HomeDeliveryStrategy())
facade.deliver_order("Bob")

facade.set_delivery_strategy(PickupStrategy())
facade.deliver_order("Alice")
```

---
## Example Output

```
Email sent to Bob: Your pizza order placed.
SMS sent to Bob: Your pizza order placed.
Email sent to Alice: Your pizza order placed.
SMS sent to Alice: Your pizza order placed.

Current Pizza Orders:
Order 1
 Customer: Bob
 Pizza: Pizza(size=Large, crust=Thin, toppings=) + pepperoni + mushrooms
------------------------------
Order 2
 Customer: Alice
 Pizza: Pizza(size=Medium, crust=Classic, toppings=mozzarella, basil)
------------------------------
Home delivery: Delivering pizza to Bob
Pickup: Alice will pick up the pizza.
```

---

## How to Run

Run the application **from the project root**:

   ```sh
     python3 client/main.py
   ```


---

## Summary

This project presents a classical application of creational design patterns together with structural patterns:
- **Singleton** for central management,
- **Builder** for flexible instantiation,
- **Factory** for type-based creation,
- **Facade** to expose a simple client API and orchestrate subsystems,
- **Adapter** to provide pluggable notification channels,
- **Decorator** to add runtime composition of pizza features,
- **Observer** for automatic notifications—multiple observers (like email and SMS) are updated whenever a pizza order is placed 
- **Command** for encapsulating user actions—order requests are represented as command objects, allowing flexible execution and management 
- **Strategy** for flexible delivery—enables runtime selection of delivery methods (home delivery, pickup, etc.) for pizza orders

These patterns collectively help achieve a maintainable, extensible, and modular pizza ordering system in Python, ensuring clean communication between entities and keeping the client code focused on high-level use cases.
