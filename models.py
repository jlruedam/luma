from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<User {self.username}>"


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    tipo_doc = db.Column(db.String(100), nullable=False)
    num_doc = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    tel = db.Column(db.String(200), nullable=True)
    hotel = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    sales = db.relationship('Sale', back_populates='client')

    def __repr__(self):
        return f"<Client {self.num_doc}: {self.name}>"


class Agency(db.Model):
    __tablename__ = 'agencies'

    id = db.Column(db.Integer, primary_key=True)
    nit = db.Column(db.String(10), nullable=False)
    name_agency = db.Column(db.String(100), nullable=False)
    email_agency = db.Column(db.String(100), nullable=False)
    tel_agency = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    tours = db.relationship('Tour', back_populates='agency')

    def __repr__(self):
        return f"<Agency {self.nit}: {self.name_agency}>"


class Tour(db.Model):
    __tablename__ = 'tours'

    id = db.Column(db.Integer, primary_key=True)
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'), nullable=False)
    name_tour = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price_sale = db.Column(db.Float, nullable=False)
    price_total = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    agency = db.relationship('Agency', back_populates='tours')
    sales = db.relationship('Sale', back_populates='tour')

    def __repr__(self):
        return f"<Tour {self.name_tour}>"


class Vendor(db.Model):
    __tablename__ = 'vendors'

    id = db.Column(db.Integer, primary_key=True)
    type_doc = db.Column(db.String(10), nullable=False)
    num_doc = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    tel = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relaciones inversas no necesarias si no vas a usarlas directamente
    sales_vendor1 = db.relationship('Sale', foreign_keys='Sale.vendor1_id', back_populates='vendor1')
    sales_vendor2 = db.relationship('Sale', foreign_keys='Sale.vendor2_id', back_populates='vendor2')

    def __repr__(self):
        return f"<Vendor {self.num_doc}: {self.name}>"


class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    vendor1_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    vendor2_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    options_payment = db.Column(db.String(100), nullable=False)
    observations = db.Column(db.String(200), nullable=False, default='')
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relaciones explícitas
    tour = db.relationship('Tour', back_populates='sales')
    client = db.relationship('Client', back_populates='sales')
    payments = db.relationship('Payment', back_populates='sales')
    vendor1 = db.relationship('Vendor', foreign_keys=[vendor1_id], back_populates='sales_vendor1')
    vendor2 = db.relationship('Vendor', foreign_keys=[vendor2_id], back_populates='sales_vendor2')

    def __repr__(self):
        return f"<Sale {self.id}: Tour {self.tour_id}, Client {self.client_id}>"
    
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    id_sale = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relaciones explícitas
    sales = db.relationship('Sale', back_populates='payments')
    