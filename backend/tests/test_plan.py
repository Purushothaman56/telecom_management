# tests/test_plan.py
from flask import json

def test_create_plan(test_app):
    # Test data for a new plan
    plan_data = {
        'plan_name': 'Platinum365',
        'plan_cost': 1000.0,
        'validity_days': 365
    }

    with test_app.test_client() as client:
        # Create a new plan
        response = client.post('/plans', json=plan_data)
        assert response.status_code == 201

        data = json.loads(response.data)
        assert data['message'] == 'Plan created successfully'

        # Retrieve all plans to verify the new plan is created
        response = client.get('/plans')
        assert response.status_code == 200
        plans = json.loads(response.data)
        assert len(plans) == 1
        assert plans[0]['plan_name'] == 'Platinum365'
