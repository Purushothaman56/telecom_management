# app/models.py
from datetime import datetime
from . import db


class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)
    assigned_mobile_number = db.Column(db.String(10), unique=True, nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    current_plan_id = db.Column(db.Integer, db.ForeignKey('plans.plan_id'), nullable=True)


class Plan(db.Model):
    __tablename__ = 'plans'
    plan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_name = db.Column(db.String(50), unique=True, nullable=False)
    plan_cost = db.Column(db.Float, nullable=False)
    validity_days = db.Column(db.Integer, nullable=False)


class Renewal(db.Model):
    __tablename__ = 'renewals'
    renewal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    renewal_date = db.Column(db.DateTime, default=datetime.utcnow)
    new_plan_id = db.Column(db.Integer, db.ForeignKey('plans.plan_id'), nullable=False)
    old_plan_id = db.Column(db.Integer, db.ForeignKey('plans.plan_id'), nullable=True)
