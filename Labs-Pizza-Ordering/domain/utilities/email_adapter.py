from ..utilities.notification_interface import NotificationService

class EmailAdapter(NotificationService):
    def send_notification(self, customer, message):
        # Simulate sending email (stub)
        print(f"Email sent to {customer}: {message}")