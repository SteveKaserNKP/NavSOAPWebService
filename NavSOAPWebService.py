import requests
from requests_ntlm import HttpNtlmAuth
from zeep import Client
from zeep.transports import Transport

class NavSOAPWebService:
    def __init__(self,web_service_url,user,password):
        self.url = web_service_url
        self.session = requests.Session()
        self.session.auth = HttpNtlmAuth(user,password)
        self.client = Client(web_service_url,transport=Transport(session=self.session)).service

if __name__ == '__main__':
    from dotenv import dotenv_values

    config = dotenv_values('.env')
    cu_50000 = NavSOAPWebService(config['URL_CU_50000'], config['USER'], config['PASS'])
    sales_orders = cu_50000.client.GetAllSalesOrders().split('|')
    print(sales_orders)