from ..models.pizza import Margherita, Pepperoni

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "margherita":
            return Margherita()
        elif pizza_type == "pepperoni":
            return Pepperoni()
        else:
            raise ValueError("Unknown pizza type")
