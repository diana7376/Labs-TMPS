class DeliveryStrategy:
    def deliver(self, order):
        raise NotImplementedError

class HomeDeliveryStrategy(DeliveryStrategy):
    def deliver(self, order):
        print(f"Home delivery: Delivering pizza to {order['customer']}")

class PickupStrategy(DeliveryStrategy):
    def deliver(self, order):
        print(f"Pickup: {order['customer']} will pick up the pizza.")