class OrderObserver:
    def update(self, order, event_type):
        raise NotImplementedError("Observer subclasses must implement update()")
