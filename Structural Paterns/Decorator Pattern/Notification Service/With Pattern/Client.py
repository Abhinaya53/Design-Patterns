from EmailNotifier import EmailNotifier
from FacebookDecorator import FacebookDecorator
from SlackDecorator import SlackDecorator

notifier = EmailNotifier()
notifier = FacebookDecorator(notifier)
notifier = SlackDecorator(notifier)
notifier.send("Alert!")