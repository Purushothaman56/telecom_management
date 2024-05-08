# tests/test_customer.py
from flask import json

def test_create_customer(test_app):
    # Test data for customer registration
    customer_data = {
        'name': 'John Doe',
        'dob': '1990-01-01',
        'email': 'johndoe@example.com',
        'aadhar_number': '123456789012',
        'assigned_mobile_number': '9876543210'
    }

    with test_app.test_client() as client:
        # Register a new customer
        response = client.post('/customers', json=customer_data)
        assert response.status_code == 201  # Expected status code for successful creation

        # Verify the response message
        data = json.loads(response.data)
        assert data['message'] == 'Customer created successfully'

        # Retrieve the customer and verify its details
        response = client.get('/customers')
        assert response.status_code == 200
        customers = json.loads(response.data)
        assert len(customers) == 1
        assert customers[0]['name'] == 'John Doe'
