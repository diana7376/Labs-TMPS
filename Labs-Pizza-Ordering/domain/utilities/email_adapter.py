from domain.utilities.order_observer import OrderObserver

class EmailAdapter(OrderObserver):
    def update(self, order, event_type):
        print(f"Email sent to {order['customer']}: Your pizza order {event_type}.")
