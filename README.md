# **Flask REST API**

This repository contains a basic REST API built using Flask and Flask-RESTful. The API demonstrates CRUD (Create, Read, Update, Delete) operations and serves as a simple example for getting started with REST APIs in Python.

## **Features**
- CRUD operations for managing data.
- Error handling for API requests.
- Basic endpoint authentication.
- JSON responses for easy integration with front-end applications

## **Prerequisites**
Python 3.6 or higher, Flask and Flask-RESTful

## **Project Structure**
**'main.py'**: Initializes the Flask application and defines the REST API routes and methods.
**'test.py'**: Contains test calls for each of the API methods defined in main.py.

## **Installation**
1. Clone the repository:
```bash
git clone https://github.com/shreej2302/RestApi.git 
cd RestApi
 ```

2. Install the required packages:
```bash
pip install -r setup_requirements.txt
```

## **Running the Project**
1. Start the Flask server by running main.py:
```python
python main.py
```
This will start the server, making the API available at http://localhost:5000.

2. Run test.py in a separate terminal to make requests to the API:
```python
 python test.py
```
**Note**: test.py is set up to call the methods in main.py. Ensure main.py is running before executing test.py.

## **API Endpoints**

| Method | Endpoint           | Description           |
|--------|---------------------|-----------------------|
| GET    | /api/resource       | Retrieve data         |
| POST   | /api/resource       | Create new data       |
| PUT    | /api/resource/<id>  | Update existing data  |
| DELETE | /api/resource/<id>  | Delete data           |


