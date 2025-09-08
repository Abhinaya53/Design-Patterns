from MediatorInterface import MediatorInterface

class Checkbox:
    def __init__(self, mediator: MediatorInterface):
        self.__mediator = mediator
        self.uncheck()

    def check(self):
        print("\nCheckbox Checked")
        self.__mediator.checkbox_checked()

    def uncheck(self):
        print("\nCheckbox Unchecked")
        self.__mediator.checkbox_unchecked()