from app.models import db
from datetime import datetime
from .products import Products

class Sales_product(db.Model):
    __tablename__ = 'sales_product'
    id = db.Column(db.Integer, primary_key=True)
    sales_id = db.Column(db.Integer, db.ForeignKey('sales.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship("Products")

    def __init__(self, product):
        self.product = product
        self.reserve_product()

    def reserve_product(self):
        self.product.amount -= 1

class Sales(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.Integer)
    total_price = db.Column(db.Float, nullable=True)
    products = db.relationship("Sales_product")

    salesman = db.Column(db.Integer, db.ForeignKey('employees.id'))
    sold_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, total_price, costumer = None):
        if costumer:
            self.customer = costumer
        self.total_price = total_price

    def calculate_total_price(self):
        total_price = 0
        if self.products:
            products = [sale_product.product for sale_product in self.products]
            for product in products:
                total_price += product.price
            self.total_price = round(total_price, 4)
            return {'Message':'Total price updated sucessfuly!'}
        return {'Message':'Total price is already up-to-date!'}

    def __repr__(self):
        return f'<Purchase of {costumer} on {sold_at}>'
