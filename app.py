from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

# Create the Flask app instance
app = Flask(__name__)

# Connect to MongoDB; we assume a local MongoDB server is running on the default port
# Let us make sure MongoDB is installed and started; you can check with 'mongod --version' in the terminal
client = MongoClient("mongodb://localhost:27017/")
db = client[
    "user_database"
]  # We use a database named 'user_database' for storing user data
users_collection = db[
    "users"
]  # We define a collection named 'users' to hold user documents


# CRUD Endpoint: Create a new user (POST request)
# We use POST because it's standard for creating resources in RESTful APIs
@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json  # Get user data from the request body
    result = users_collection.insert_one(user_data)  # Insert the data into MongoDB
    return (
        jsonify(
            {"id": str(result.inserted_id), "message": "User created successfully"}
        ),
        201,
    )


# CRUD Endpoint: Read all users (GET request)
# We use GET to retrieve data; this returns all users in the collection
@app.route("/users", methods=["GET"])
def get_users():
    users = list(
        users_collection.find({}, {"_id": 0})
    )  # Fetch all users, excluding the ObjectId for simplicity
    return jsonify(users)


# CRUD Endpoint: Read a single user by ID (GET request)
# We use path parameters to specify which user to retrieve; let us handle the ObjectId conversion
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)}, {"_id": 0})
        if user:
            return jsonify(user)
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return (
            jsonify({"error": "Invalid ID format"}),
            400,
        )  # We add error handling for invalid ObjectIds


# CRUD Endpoint: Update a user by ID (PUT request)
# We use PUT for updating resources; it replaces or updates the user data
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    user_data = request.json  # Get updated data from the request body
    try:
        result = users_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": user_data}
        )
        if result.matched_count > 0:
            return jsonify({"message": "User updated successfully"})
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": "Invalid ID format"}), 400


# CRUD Endpoint: Delete a user by ID (DELETE request)
# We use DELETE to remove resources; this deletes the user from the database
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        result = users_collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count > 0:
            return jsonify({"message": "User deleted successfully"})
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": "Invalid ID format"}), 400


# Run the app; we use debug mode for auto-reloading during development
if __name__ == "__main__":
    app.run(debug=True, port=5005)
