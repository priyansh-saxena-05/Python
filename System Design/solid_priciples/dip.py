"""Dependency Inversion Principle (DIP):
Consider a scenario where we have a class called NotificationService
responsible for sending notifications to users.
Initially, NotificationService directly depends on the EmailSender class to send email notifications:
"""

class EmailSender:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()
    
    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, message)

notification_service = NotificationService()
notification_service.send_notification("example@example.com", "Hello!")


"""
In this design, NotificationService has a concrete dependency on EmailSender.
While this may work fine initially, it violates the Dependency Inversion Principle because NotificationService depends on the implementation details of EmailSender.
To adhere to the Dependency Inversion Principle, we need to introduce an abstraction (interface) between NotificationService and EmailSender. This abstraction allows NotificationService
to depend on an interface rather than a concrete implementation.
Here's how we can refactor the code to follow DIP:
"""

from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass

class EmailSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

class NotificationService:
    def __init__(self, message_sender):
        self.message_sender = message_sender
    
    def send_notification(self, recipient, message):
        self.message_sender.send_message(recipient, message)

email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("example@example.com", "Hello!")
