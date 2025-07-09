# Flask CRUD App with Pymongo

This is a simple, beginner-friendly Flask application that provides CRUD (Create, Read, Update, Delete) endpoints for managing users in a MongoDB database.

## Prerequisites
- Install Python 3 and pip.
- Install MongoDB and ensure it's running (start with `mongod` in a terminal).
- Verify MongoDB connection with `mongo --version`.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`
3. Access the API endpoints via a tool like curl or Postman. For example:
   - Create a user: POST to http://127.0.0.1:5000/users with JSON body {"name": "John", "age": 30}
   - Get all users: GET http://127.0.0.1:5000/users
   - Get/Update/Delete a user: Use the user ID returned from create.

## Endpoints
- **POST /users**: Create a new user
- **GET /users**: Retrieve all users
- **GET /users/<id>**: Retrieve a single user by ID
- **PUT /users/<id>**: Update a user by ID
- **DELETE /users/<id>**: Delete a user by ID

Feel free to modify the code to add more features!
