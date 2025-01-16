from config import db

class Auction(db.Model):
    __tablename__ = 'auctions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', back_populates='auctions')
    item = db.relationship('Item', back_populates='auctions')
    bids = db.relationship('Bid', back_populates='auction')
    transaction = db.relationship('Transaction', back_populates='auction', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user': {
                'id': self.user.id,
                'name': self.user.name,
                'email': self.user.email
            },
            'item': self.item.to_dict(),
            'created_at': self.created_at,
        }