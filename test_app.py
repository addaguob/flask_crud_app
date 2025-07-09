import requests

# Base URL for the Flask app
BASE_URL = "http://localhost:5006"


def test_crud_operations():
    print("\n=== Testing CRUD Operations ===")

    # Test Create
    print("\n1. Creating a new user...")
    new_user = {"name": "Test User", "age": 30, "email": "test@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    user_id = response.json().get("id")

    if user_id:
        print(f"Created user with ID: {user_id}")

        # Test Read (Single)
        print("\n2. Reading the created user...")
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        print(f"Status Code: {response.status_code}")
        print(f"User Data: {response.json()}")

        # Test Update
        print("\n3. Updating the user...")
        update_data = {"age": 31, "email": "updated@example.com"}
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=update_data)
        print(f"Status Code: {response.status_code}")
        print(f"Update Response: {response.json()}")

        # Verify Update
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        print(f"\n4. Verifying update - User Data: {response.json()}")

        # Test Read All
        print("\n5. Listing all users...")
        response = requests.get(f"{BASE_URL}/users")
        print(f"Status Code: {response.status_code}")
        print(f"All Users: {response.json()}")

        # Test Delete
        print(f"\n6. Deleting user {user_id}...")
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        print(f"Status Code: {response.status_code}")
        print(f"Delete Response: {response.json()}")

        # Verify Deletion
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        print(f"\n7. Verifying deletion - Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    else:
        print("Failed to create user")


if __name__ == "__main__":
    test_crud_operations()
