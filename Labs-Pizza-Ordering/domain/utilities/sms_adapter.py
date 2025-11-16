from ..utilities.notification_interface import NotificationService

class SMSAdapter(NotificationService):
    def send_notification(self, customer, message):
        # Simulate sending SMS (stub)
        print(f"SMS sent to {customer}: {message}")