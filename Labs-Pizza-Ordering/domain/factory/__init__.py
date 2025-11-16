# domain.factory package initializer
from .pizza_factory import PizzaFactory
from .singleton import PizzaOrderManager

__all__ = ["PizzaFactory", "PizzaOrderManager"]

