# Pizza Ordering System — Design Patterns Lab

## Overview

This directory demonstrates implementations of common design patterns in Python using a simple pizza-ordering domain.

Code is organized into modules and packages (client interface, domain models, factories, etc.) to maintain a clear separation of concerns and modular design.

In this project we implemented the following design patterns: Singleton, Builder, Factory Method, Facade, Adapter, and Decorator.

---

## Project Structure

```
Labs-Pizza-Ordering/
├── client/
│   └── main.py
├── domain/
│   ├── factory/
│   │   ├── pizza_factory.py
│   │   └── singleton.py
│   ├── models/
│   │   ├── pizza.py
│   │   ├── decorator.py
│   │   └── builder.py   
│   ├── facade/
│   │   └── pizza_ordering_facade.py
│   ├── utilities/
│   │   ├── notification_interface.py
│   │   ├── email_adapter.py
│   │   └── sms_adapter.py
│   └── builder.py
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

### Structural Patterns (added)

To complement the creational patterns above, the following structural patterns were added to simplify the client API and enable extensibility.

#### Facade

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

#### Adapter

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

#### Decorator

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

## Example Output

```
Email sent to Bob: Your custom pizza order is confirmed!
Email sent to Alice: Your classic pizza order is confirmed!
Current Pizza Orders:
Order 1:
  Customer: Bob
  Pizza: Pizza(size=Large, crust=Thin, toppings=) + pepperoni + mushrooms
------------------------------
Order 2:
  Customer: Alice
  Pizza: Pizza(size=Medium, crust=Classic, toppings=mozzarella, basil)
------------------------------
```

---

## How to Run

Run the application **from the project root**:

   ```sh
   python3 -m client.main
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

These patterns help achieve a maintainable and extensible pizza ordering system in Python while keeping the client code focused on use cases.
