from GraphNodes import City, Industry, Road, PowerLine
from ExportVisitor import ExportVisitor

nodes = [City("Springfield"), Industry("SteelWorks"), Road("Route 66"), PowerLine("NorthGrid")]
visitor = ExportVisitor()

for node in nodes:
    node.accept(visitor)
