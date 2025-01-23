import logging
from flask import jsonify
from models.winner import Winner
from models.auction import Auction
from models.bid import Bid
from models.item import Item
from base_response.base_response import BaseResponse
from config import db


def create_winner_service(auction_id):
    try:
        with db.session.begin_nested():
            auction = Auction.query.filter_by(id=auction_id, deleted_at=None).first()
            find = Winner.query.filter_by(auction_id=auction_id, deleted_at=None).first()
            if find is not None:
                return jsonify(BaseResponse.response_error('Winner already exists')), 400
            if auction is None:
                return jsonify(BaseResponse.response_error('Auction not found')), 404
            if auction.status != 'closed':
                return jsonify(BaseResponse.response_error('Auction is not closed')), 400
            
            # Check for the bid with the current price
            bid = Bid.query.filter_by(auction_id=auction_id, deleted_at=None, bid_amount=auction.current_price).first()
            if bid is None:
                return jsonify(BaseResponse.response_error('No valid bid found for the current price')), 400
            
            # Create the winner
            winner = Winner(auction_id=auction_id, final_price=auction.current_price, winner_id=bid.user_id)

            # Update the item status
            item = Item.query.filter_by(id=auction.item_id, deleted_at=None).first()
            if item is None:
                return jsonify(BaseResponse.response_error('Item not found')), 404
            item.status = 'sold'
            db.session.add(item)
            db.session.add(winner)
        db.session.commit()
        
        return jsonify(BaseResponse.response_success(winner.to_dict())), 201
    except Exception as ex:
        logging.error(ex, exc_info=True)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    

def get_all_winner_service():
    try:
        winners = Winner.query.filter_by(deleted_at=None).all()
        return jsonify(BaseResponse.response_success([winner.to_dict() for winner in winners])), 200
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500