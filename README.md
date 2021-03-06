# Basic Usage

``` python
from dotenv import dotenv_values
from NavSOAPWebService import NavSOAPWebService

config = dotenv_values('.env')
cu_50000 = NavSOAPWebService(config['URL_CU_50000'], config['USER'], config['PASS'])
sales_orders = cu_50000.client.GetAllSalesOrders().split('|')
print(sales_orders)
```

## Nav SOAP Web Service

1. To use this class, you'll need to create a web service for a codeunit object in Navision.  The functions in the codeunit will need to be set with `Local=No` and `FunctionVisibility=External` in the properties of each function in order to be visibile from the web service. For this example, codeunit `50000` has been created with a function called `GetAllSalesOrders`.  The code creates a pipe-separated list of all the `Sales Header`'s `No.`s.

>``` C/AL
>[External] GetAllSalesOrders() rSalesOrders : Text
>rSalesOrders := '';
>lSH.RESET;
>IF lSH.FINDSET THEN BEGIN
>  REPEAT
>    IF rSalesOrders = '' THEN BEGIN
>      rSalesOrders := lSH."No.";
>    END ELSE BEGIN
>      rSalesOrders += '|' + lSH."No.";
>    END;
>  UNTIL lSH.NEXT = 0;
>END;
>```

2. You'll also need to create a `.env` file that stores your credentials and, optionally, your web service URLs.

>Example .env file:

>``` dotenv
>USER=my_user_name
>PASS=my_password
>URL_5000=http://SERVER.domain.com:PORT/DB/WS/CompanyName/ObjType/ObjName
>```

3. *Optional* - Create a virtual environment and activate it

4. Install the `requirements.txt` file

>``` bat
>pip install -r requirements.txt
>```

5. Import the `NavSOAPWebService` class into a Python file

>``` python
>from NavSOAPWebService import NavSOAPWebService
>```

6. Import the `dotenv_values` function from the `dotenv` package

>``` python
>from dotenv import dotenv_values
>```

7. Read your .env file

>``` python
>config = dotenv_values('.env')
>```

8. Connect to the web service

>``` python
>cu_50000 = NavSOAPWebService(config['URL_CU_50000'], config['USER'], config['PASS'])
>```

9. Call functions from your codeunit

>``` python
>sales_orders = cu_50000.client.GetAllSalesOrders().split('|')
>print(sales_orders)
>```

>`['SH00000001', 'SH00000002']`
