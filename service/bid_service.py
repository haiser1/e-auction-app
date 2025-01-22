import logging
from models.auction import Auction
from vallidation.bid_validation import CreateBidValidation
from models.bid import Bid
from base_response.base_response import BaseResponse
from flask import jsonify
from config import db
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError


def create_bid_service(request_data, auction_id, user_id):
    try:
        data = CreateBidValidation().load(request_data)
        with db.session.begin_nested():
            auction = Auction.query.filter_by(id=auction_id, deleted_at=None).first()
            if auction is None:
                return jsonify(BaseResponse.response_error('Auction not found')), 404

            if auction.status != 'open':
                return jsonify(BaseResponse.response_error('Auction is not open')), 400

            if data['bid_amount'] <= auction.current_price:
                return jsonify(BaseResponse.response_error('Bid amount must be greater than current price')), 400

            bid = Bid(auction_id=auction_id, user_id=user_id, bid_amount=data['bid_amount'])
            auction.current_price = data['bid_amount']

            db.session.add(bid)
            db.session.add(auction)
        
        db.session.commit()
        
        return jsonify(BaseResponse.response_success(bid.to_dict())), 201

    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    
    except SQLAlchemyError as ex:
        db.session.rollback()
        logging.error(f"Database error: {ex}")
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
    except Exception as ex:
        logging.error(f"Unexpected error: {ex}")
        return jsonify(BaseResponse.response_error('Internal server error')), 500

def get_history_bid_service(auction_id):
    try:
        bids = Bid.query.filter_by(auction_id=auction_id, deleted_at=None).order_by(Bid.created_at.desc()).all()
        return jsonify(BaseResponse.response_success([bid.to_dict() for bid in bids])), 200
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500