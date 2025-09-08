from functools import singledispatchmethod
from GraphNodes import City, Industry, Road, PowerLine
from VisitorInterface import VisitorInterface

class ExportVisitor(VisitorInterface):
    @singledispatchmethod
    def visit(self, node):
        raise NotImplementedError(f"No export logic for {type(node).__name__}")

    @visit.register
    def _(self, node: City):
        print(f"< City name='{node.name}' />")

    @visit.register
    def _(self, node: Industry):
        print(f"< Industry name='{node.name}' />")

    @visit.register
    def _(self, node: Road):
        print(f"< Road name='{node.name}' />")

    @visit.register
    def _(self, node: PowerLine):
        print(f"< PowerLine name='{node.name}' />")


"""
Python does not support true method overloading by argument type. 
So, we are simulating it using functools.singledispatchmethod (Python 3.8+).
"""