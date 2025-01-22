import logging
from marshmallow import ValidationError
from vallidation.auction_validation import CreateAuctionValidation, GetAuctionPaginationValidation
from models.auction import Auction
from models.item import Item
from base_response.base_response import BaseResponse
from flask import jsonify
from config import db

def create_auction_service(request_data):
    try:
        data = CreateAuctionValidation().load(request_data)
        item = Item.query.filter_by(id=data['item_id'], deleted_at=None).first()
        if item is None:
            return jsonify(BaseResponse.response_error('Item not found')), 404
        if item.status != 'available':
            return jsonify(BaseResponse.response_error('Item is not available')), 400
        auction = Auction(
            item_id=item.id,
            current_price=item.starting_price,
            close_biding=data['close_biding']
        )
        item.status = 'reserved'
        db.session.add(auction)
        db.session.commit()
        return jsonify(BaseResponse.response_success(auction.to_dict())), 201
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def get_auction_pagination_service(page, limit):
    try:
        data = GetAuctionPaginationValidation().load({'page': page, 'limit': limit})
        auctions = Auction.query.filter_by(deleted_at=None).order_by(Auction.created_at.desc()).paginate(page=data['page'], per_page=data['limit'], error_out=False)
        return jsonify(BaseResponse.response_success({'auctions': [auction.to_dict() for auction in auctions.items], 'total': auctions.total, 'page': page, 'limit': limit})), 200
    
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500