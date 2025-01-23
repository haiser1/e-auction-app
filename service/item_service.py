import datetime
import logging
from models.item import Item
from vallidation.item_validation import CreateItemValidation, GetItemPaginationValidation, UpdateItemByAdminValidation, UpdateItemByUserValidation
from base_response.base_response import BaseResponse
from flask import jsonify
from config import db
from marshmallow import ValidationError

def create_item(request_data, user_id):
    try:
        data = CreateItemValidation().load(request_data)
        find = Item.query.filter_by(name=data['name'],user_id=user_id, deleted_at=None).first()
        if find is not None:
            return jsonify(BaseResponse.response_error('Item already exists')), 400

        data_item = Item(name=data['name'],description=data['description'], starting_price=data['starting_price'], user_id=user_id)

        db.session.add(data_item)
        db.session.commit()
        return jsonify(BaseResponse.response_success(data_item.to_dict())), 201
    
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    

def get_item_by_user_pagination_service(page, limit, user_id):
    try:
        data = GetItemPaginationValidation().load({'page': page, 'limit': limit})
        items = Item.query.filter_by(user_id=user_id,deleted_at=None).order_by(Item.created_at.desc()).paginate(page=data['page'], per_page=data['limit'], error_out=False)
        return jsonify(BaseResponse.response_success({'items': [item.to_dict() for item in items.items], 'total': items.total, 'page': page, 'limit': limit})), 200
    
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def get_item_by_id_service(item_id, user_id):
    try:
        item = Item.query.filter_by(id=item_id,user_id=user_id, deleted_at=None).first()
        if item is None:
            return jsonify(BaseResponse.response_error('Item not found')), 404
        return jsonify(BaseResponse.response_success(item.to_dict())), 200
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500

def update_item_by_user_service(item_id, request_data, user_id):
    try:
        data = UpdateItemByUserValidation().load(request_data)
        item = Item.query.filter_by(id=item_id, user_id=user_id, deleted_at=None).first()
        if item is None:
            return jsonify(BaseResponse.response_error('Item not found')), 404
        if data.get('name'):
            item.name = data['name']
        if data.get('description'):
            item.description = data['description']
        if data.get('starting_price'):
            item.starting_price = data['starting_price']
        db.session.commit()
        return jsonify(BaseResponse.response_success(item.to_dict())), 200
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def delete_item_by_user_service(item_id, user_id):
    try:
        item = Item.query.filter_by(id=item_id, user_id=user_id, deleted_at=None).first()
        if item is None:
            return jsonify(BaseResponse.response_error('Item not found')), 404
        item.deleted_at = datetime.datetime.now()
        db.session.commit()
        return jsonify(BaseResponse.response_success({'message': 'Data item deleted successfuly'}))
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500

def get_item_by_admin_pagination_service(page, limit):
    try:
        data = GetItemPaginationValidation().load({'page': page, 'limit': limit})
        items = Item.query.filter_by(deleted_at=None).order_by(Item.created_at.desc()).paginate(page=data['page'], per_page=data['limit'], error_out=False)
        return jsonify(BaseResponse.response_success({'items': [item.to_dict() for item in items.items], 'total': items.total, 'page': page, 'limit': limit})), 200
    
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def get_item_by_id_admin_service(item_id):
    try:
        item = Item.query.filter_by(id=item_id, deleted_at=None).first()
        if item is None:
            return jsonify(BaseResponse.response_error('Item not found')), 404
        return jsonify(BaseResponse.response_success(item.to_dict())), 200
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500

def update_item_by_admin_service(item_id, request_data):
    try:
        data = UpdateItemByAdminValidation().load(request_data)
        item = Item.query.filter_by(id=item_id, deleted_at=None).first()
        if item is None:
            return jsonify(BaseResponse.response_error('Item not found')), 404
        if data.get('name'):
            item.name = data['name']
        if data.get('description'):
            item.description = data['description']
        if data.get('starting_price'):
            item.starting_price = data['starting_price']
        if data.get('status'):
            item.status = data['status']
        db.session.commit()
        return jsonify(BaseResponse.response_success(item.to_dict())), 200
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def delete_item_by_admin_service(item_id):
    try:
        item = Item.query.filter_by(id=item_id, deleted_at=None).first()
        if item is None:
            return jsonify(BaseResponse.response_error('Item not found')), 404
        item.deleted_at = datetime.datetime.now()
        db.session.commit()
        return jsonify(BaseResponse.response_success({'message': 'Data item deleted successfuly'}))
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500