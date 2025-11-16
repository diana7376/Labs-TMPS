class NotificationService:
    """Abstract notification interface for adapters.

    Subclasses should implement `send_notification(customer, message)`.
    """
    def send_notification(self, customer, message):
        raise NotImplementedError