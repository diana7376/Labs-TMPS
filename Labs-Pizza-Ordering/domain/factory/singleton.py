class PizzaOrderManager:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.orders = []
            cls.instance.observers = []
        return cls.instance

    def add_order(self, customer, pizza):
        order = {"customer": customer, "pizza": pizza}
        self.orders.append(order)
        self.notify_observers(order, "placed")

    def list_orders(self):
        return self.orders

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, order, event_type):
        for observer in self.observers:
            observer.update(order, event_type)
