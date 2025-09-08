from InventoryReport import InventoryReport
from SalesReport import SalesReport
from EmployeeReport import EmployeeReport

report1 = InventoryReport()
report2 = SalesReport()
report3 = EmployeeReport()

report1.generate_report()
report2.generate_report()
report3.generate_report()