from config import db

class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    auction_id = db.Column(db.Integer, db.ForeignKey('auctions.id'), nullable=False)
    bid_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', backref='bids', lazy=True)
    auction = db.relationship('Auction', backref='bids', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user': {
                'id': self.user.id,
                'name': self.user.name,
                'email': self.user.email
            },
            'auction': {
                'id': self.auction.id,
                'item': self.auction.item.to_dict(),
            },
            'bid_amount': self.bid_amount,
            'created_at': self.created_at,
        }