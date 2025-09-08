# Problem
Suppose we are designing a notification system that initially sends messages only via email. Over time, new requirements arrive: send notifications via SMS, Slack, Facebook, etc. 

# Naive Approach:
A naive solution is to create subclasses for every new channel or their combinations, such as EmailSMSNotifier, EmailSlackNotifier, etc. This quickly becomes unmanageable, rigid, and error-prone as combinations grow. The problems with this approach are:
- Every new channel or combination requires a new class. We may end up with a lot of classes
- Common logic across different notifiers leads to duplicated code. DRY is violated.
- SRP is violated since subclasses mix core notification logic with multiple responsibilities.
- OCP is violated as every new channel requires modifying or adding many subclasses.
- DIP is violated because client depends directly on concrete notification subclasses.

# Solution: Decorator Pattern
Introduce decorator classes that dynamically add behaviors to a base notifier.
- Define a Notifier interface with send(message).
- Implement a base notifier for email.
- Add decorators like SMSNotifierDecorator, SlackNotifierDecorator, each wrapping a notifier and extending functionality.
- Decorators can be stacked at runtime, e.g., base email + SMS + Slack, in any order.
- SRP fixed as each class has a single responsibility.
- OCP fixed as new notification channels added via decorators, no changes to existing code.
- DIP fixed as client depends on abstraction, not concrete decorators.