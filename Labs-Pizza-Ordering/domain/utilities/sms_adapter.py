from domain.utilities.order_observer import OrderObserver

class SMSAdapter(OrderObserver):
    def update(self, order, event_type):
        print(f"SMS sent to {order['customer']}: Your pizza order {event_type}.")
