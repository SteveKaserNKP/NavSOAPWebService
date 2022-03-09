from dotenv import dotenv_values
from NavSOAPWebService import NavSOAPWebService

config = dotenv_values('.env')
cu_50000 = NavSOAPWebService(config['URL_CU_50000'], config['USER'], config['PASS'])
sales_orders = cu_50000.client.GetAllSalesOrders().split('|')
print(sales_orders)