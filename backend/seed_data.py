# seed_data.py
from datetime import datetime
from app import create_app, db
from app.models import Customer, Plan, Renewal

# Create the Flask application
app = create_app()

# Initialize the app context for database operations
with app.app_context():
    # Drop and create all tables to start fresh (optional, for development purposes)
    db.drop_all()
    db.create_all()

    # Sample plans
    platinum_plan = Plan(plan_name="Platinum365", plan_cost=1000.0, validity_days=365)
    gold_plan = Plan(plan_name="Gold180", plan_cost=600.0, validity_days=180)
    silver_plan = Plan(plan_name="Silver90", plan_cost=300.0, validity_days=90)

    db.session.add_all([platinum_plan, gold_plan, silver_plan])
    db.session.commit()

    # Sample customers
    customer1 = Customer(
        name="John Doe",
        dob=datetime.strptime("1990-01-01", "%Y-%m-%d"),
        email="john.doe@example.com",
        aadhar_number="123456789012",
        assigned_mobile_number="9876543210",
        current_plan_id=platinum_plan.plan_id
    )
    
    customer2 = Customer(
        name="Jane Doe",
        dob=datetime.strptime("1995-01-01", "%Y-%m-%d"),
        email="jane.doe@example.com",
        aadhar_number="987654321098",
        assigned_mobile_number="9876543211",
        current_plan_id=silver_plan.plan_id
    )

    db.session.add_all([customer1, customer2])
    db.session.commit()

    # Sample renewals
    renewal1 = Renewal(
        customer_id=customer1.customer_id,
        new_plan_id=platinum_plan.plan_id,
        renewal_date=datetime.now(),
        old_plan_id=None
    )
    
    renewal2 = Renewal(
        customer_id=customer2.customer_id,
        new_plan_id=silver_plan.plan_id,
        renewal_date=datetime.now(),
        old_plan_id=None
    )

    db.session.add_all([renewal1, renewal2])
    db.session.commit()

    print("Sample data seeded successfully!")
