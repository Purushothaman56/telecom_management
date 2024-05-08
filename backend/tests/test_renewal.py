# tests/test_renewal.py
from flask import json
from datetime import datetime

def test_create_renewal(test_app):
    # Test data for plan and customer
    plan_data = {
        'plan_name': 'Silver90',
        'plan_cost': 300.0,
        'validity_days': 90
    }

    customer_data = {
        'name': 'Jane Doe',
        'dob': '1995-01-01',
        'email': 'janedoe@example.com',
        'aadhar_number': '123456789011',
        'assigned_mobile_number': '9876543211'
    }

    with test_app.test_client() as client:
        # Create a new plan
        response = client.post('/plans', json=plan_data)
        assert response.status_code == 201

        # Register a new customer
        response = client.post('/customers', json=customer_data)
        assert response.status_code == 201

        # Test data for renewal
        renewal_data = {
            'customer_id': 1,
            'new_plan_id': 1
        }

        # Create a new renewal
        response = client.post('/renewals', json=renewal_data)
        assert response.status_code == 201

        data = json.loads(response.data)
        assert data['message'] == 'Renewal created successfully'
