

# Pizza Ordering System — Creational Design Patterns Lab

## Overview

This directory demonstrates the implementation of three major **creational design patterns** in Python. The domain area chosen is a simple pizza ordering system.

All code is organized into modules/packages according to their responsibilities (client interface, domain models, pattern factories, etc.), enabling clear separation of concerns and modular design.

---

## Project Structure

```
Lab1-Pizza-Ordering/
├── client/
│   └── main.py
├── domain/
│   ├── factory/
│   │   ├── pizza_factory.py
│   │   └── singleton.py
│   ├── models/
│   │   └── pizza.py
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

## Example Output

```
Current Pizza Orders:
Order 1:
  Customer: Alice
  Pizza: Pizza(size=Medium, crust=Classic, toppings=mozzarella, basil)
------------------------------
Order 2:
  Customer: Bob
  Pizza: Pizza(size=Large, crust=Classic, toppings=mushrooms, chicken)
------------------------------
```

---

## How to Run

Run the application **from the project root**:

   ```sh
   python -m client.main
   ```


---

## Summary

This project presents a classical application of creational design patterns:
- **Singleton** for central management,
- **Builder** for flexible instantiation,
- **Factory** for type-based creation,
helping achieve a maintainable and extensible pizza ordering system in Python.

