from StockMarket import StockMarket
from InvestorA import InvestorA
from InvestorB import InvestorB

market = StockMarket(5.34)

investor1 = InvestorA("Abhinaya", "abhi@gmail.com")
market.register_observer(investor1)

investor2 = InvestorA("Akshay", "akshay@gmail.com")
market.register_observer(investor2)

investor3 = InvestorB("Abhinaya", "abhi@gmail.com")
market.register_observer(investor3)

investor4 = InvestorB("Akshay", "akshay@gmail.com")
market.register_observer(investor4)

market.set_stock_price("ABC", 10.22, 10.22)
market.set_stock_price("XYZ", 10.22, 50.04)
market.set_stock_price("ABC", 150.22, 88.04)

market.remove_observer(investor4)

market.set_stock_price("DEF", 100.22, 320.04)