from config import db

class Auction(db.Model):
    __tablename__ = 'auctions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    close_biding = db.Column(db.DateTime, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('open', 'closed', name='auction_status'), default='open', nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    item = db.relationship('Item', backref='auctions', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user': {
                'id': self.item.user_id,
                'name': self.item.user.name,
                'email': self.item.user.email
            },
            'item':{
                'id': self.item.id,
                'name': self.item.name,
                'description': self.item.description,
                'starting_price': self.item.starting_price,
                'image_url': self.item.image_url,
            },
            'status': self.status,
            'close_biding': self.close_biding,
            'current_price': self.current_price,
            'created_at': self.created_at,
        }