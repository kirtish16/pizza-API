# Pizza API
## About the project

A Django application to store information about order of different types of Pizza, interact with database using API interface.

A pizza order contains information about:
- Type : Regular, Square
- Size : Small , Medium, Large
- Toppings: User dependent(Example: Onion,Tomato,Cheese,Corn, Capsicum)

## Technology used

Database used: **MongoDB**




## Functionalities
- Get all orders list.
- Create an order.
- Get an order details.
- Update an order details.
- Delete an order.
- Filter orders by type
- Filter orders by size

## Installation
Clone this git repository:
```
git clone https://github.com/kirtish16/pizza-API.git
```
Go to the project folder:
```
cd pizza
```
Install the requirements:
```
pip install -r requirements.txt
```

Create a database named **'pizzadb'** on MongoDB Application

Run the migrations:
```
python manage.py migrate
```
Start the server:
```
python manage.py runserver
```
This will start the webserver on [localhost](http://127.0.0.1:8000/).

## Documentation
The API endpoints are:

| Endpoint   | Description |
|------------|-----------|
| /pizza-list/ | to list the orders from a customer |
| /pizza-detail/\<pizza id>/ | to get details about an order |
| /pizza-add | to create a new order |
| /pizza-update/\<pizza id>/ | to update an order |
| /pizza-delete/\<pizza id>/ | to delete an order |
| /pizza-filter/type/\<pizza id>/ | to filter orders by type |
| /pizza-filter/size/\<pizza id>/ | to filter orders by size |

## Screenshots

### Working
- Overview of all API

![API Overview](/screenshots/apiOverview.jpg)

- List of all pizza orders

![Pizza List](/screenshots/pizzaList.jpg)

- Adding pizza order

![Adding Data](/screenshots/addingData.jpg)
![Data Saved](/screenshots/dataSaved.jpg)

- Get pizza order details

![Pizza details](/screenshots/pizzaDetailid2.jpg)

- Update Order details 

![Update](/screenshots/pizzaUpdating.jpg)
![Result](/screenshots/pizzaUpdateResult.jpg)

- Delete order

![Delete Pizza order](/screenshots/pizzaDeleteSuccessfull.jpg)

- Filter pizza orders by Type

![Pizza List](/screenshots/filterbyType.jpg)

- Filter pizza orders by Size

![Pizza List](/screenshots/filterbySize.jpg)

### Error Handling

- Invalid pizza order id for getting order details 

![Invalid](/screenshots/orderNotFound.jpg)

- Invalid pizza type sent to API 

![Invalid](/screenshots/errorType.jpg)

- Invalid pizza size sent to API 

![Invalid](/screenshots/errorSize.jpg)

- Invalid filter options sent to API 

![Invalid](/screenshots/invalidFIlteroptions.jpg)

- Invalid pizza order id for deleting object

![Invalid](/screenshots/invalidpizzaDelete.jpg)

## License
[MIT](https://choosealicense.com/licenses/mit/)
