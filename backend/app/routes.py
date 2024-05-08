# app/routes.py
from flask import Blueprint, request, jsonify
from . import db
from .models import Customer, Plan, Renewal
from datetime import datetime

bp = Blueprint('main', __name__)

# Register new customer
@bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    name = data.get('name')
    dob = datetime.strptime(data.get('dob'), "%Y-%m-%d")
    email = data.get('email')
    aadhar_number = data.get('aadhar_number')
    assigned_mobile_number = data.get('assigned_mobile_number')
    current_plan_id = data.get('current_plan_id')

    customer = Customer(
        name=name,
        dob=dob,
        email=email,
        aadhar_number=aadhar_number,
        assigned_mobile_number=assigned_mobile_number,
        current_plan_id=current_plan_id
    )

    db.session.add(customer)
    db.session.commit()

    return jsonify({"message": "Customer created successfully"}), 201

# Get all customers
@bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    customer_list = [
        {
            "customer_id": c.customer_id,
            "name": c.name,
            "dob": c.dob.strftime("%Y-%m-%d"),
            "email": c.email,
            "aadhar_number": c.aadhar_number,
            "assigned_mobile_number": c.assigned_mobile_number,
            "registration_date": c.registration_date.strftime("%Y-%m-%d"),
            "current_plan_id": c.current_plan_id,
        }
        for c in customers
    ]
    return jsonify(customer_list), 200

# Update customer information
@bp.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)

    data = request.json
    customer.name = data.get("name", customer.name)
    customer.email = data.get("email", customer.email)
    customer.assigned_mobile_number = data.get("assigned_mobile_number", customer.assigned_mobile_number)

    db.session.commit()

    return jsonify({"message": "Customer updated successfully"}), 200

# Delete a customer
@bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)

    db.session.delete(customer)
    db.session.commit()

    return jsonify({"message": "Customer deleted successfully"}), 200

# Get all plans
@bp.route('/plans', methods=['GET'])
def get_plans():
    plans = Plan.query.all()
    plan_list = [
        {
            "plan_id": p.plan_id,
            "plan_name": p.plan_name,
            "plan_cost": p.plan_cost,
            "validity_days": p.validity_days,
        }
        for p in plans
    ]
    return jsonify(plan_list), 200

# Create a new plan
@bp.route('/plans', methods=['POST'])
def create_plan():
    data = request.json
    plan_name = data.get("plan_name")
    plan_cost = data.get("plan_cost")
    validity_days = data.get("validity_days")

    plan = Plan(
        plan_name=plan_name,
        plan_cost=plan_cost,
        validity_days=validity_days,
    )

    db.session.add(plan)
    db.session.commit()

    return jsonify({"message": "Plan created successfully"}), 201

# Create a new renewal record
@bp.route('/renewals', methods=['POST'])
def create_renewal():
    data = request.json
    customer_id = data.get("customer_id")
    new_plan_id = data.get("new_plan_id")
    renewal_date = datetime.now()  # Use current time for renewal
    old_plan_id = data.get("old_plan_id")

    renewal = Renewal(
        customer_id=customer_id,
        new_plan_id=new_plan_id,
        old_plan_id=old_plan_id,
        renewal_date=renewal_date
    )

    db.session.add(renewal)
    db.session.commit()

    return jsonify({"message": "Renewal created successfully"}), 201
