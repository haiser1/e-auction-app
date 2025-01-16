from config import db
from bcrypt import hashpw, gensalt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'user', name='user_roles'), nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    items = db.relationship('Item', back_populates='user')
    auctions = db.relationship('Auction', back_populates='user')
    bids = db.relationship('Bid', back_populates='user')
    transactions = db.relationship('Transaction', back_populates='winner')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
        }
    