from config import db

class Winner(db.Model):
    __tablename__ = 'winners'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    auction_id = db.Column(db.Integer, db.ForeignKey('auctions.id'), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    final_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    auction = db.relationship('Auction', backref='winners', lazy=True)
    winner = db.relationship('User', backref='winners', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'auction': {
                'id': self.auction.id,
                'item': self.auction.item.to_dict(),
            },
            'winner': {
                'id': self.winner.id,
                'name': self.winner.name,
                },
            'final_price': self.final_price,
            'created_at': self.created_at,
        }