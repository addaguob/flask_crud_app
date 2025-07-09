python test_app.py

=== Testing CRUD Operations ===

1. Creating a new user...
Status Code: 201
Response: {'id': '686e0777797713c13ea8ea2f', 'message': 'User created successfully'}
Created user with ID: 686e0777797713c13ea8ea2f

2. Reading the created user...
Status Code: 200
User Data: {'age': 30, 'email': 'test@example.com', 'name': 'Test User'}

3. Updating the user...
Status Code: 200
Update Response: {'message': 'User updated successfully'}

4. Verifying update - User Data: {'age': 31, 'email': 'updated@example.com', 'name': 'Test User'}

5. Listing all users...
Status Code: 200
All Users: [{'age': 31, 'email': 'updated@example.com', 'name': 'Test User'}]

6. Deleting user 686e0777797713c13ea8ea2f...
Status Code: 200
Delete Response: {'message': 'User deleted successfully'}

7. Verifying deletion - Status Code: 404
Response: {'error': 'User not found'}