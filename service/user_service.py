from bcrypt import checkpw, gensalt, hashpw
from models.user import User
from vallidation.user_validation import UpdateUserValidation
from base_response.base_response import BaseResponse
from flask import jsonify
import logging
from marshmallow import ValidationError
from config import db

def get_user_current_service(user_id):
    try:
        user = User.query.filter_by(id=user_id, deleted_at=None).first()

        if user is None:
            return jsonify(BaseResponse.response_error('User not found')), 404
        return jsonify(BaseResponse.response_success(user.to_dict())), 200
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400

    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def update_user_service(user_id, request_data):
    try:
        data = UpdateUserValidation().load(request_data)
        user = User.query.filter_by(id=user_id, deleted_at=None).first()

        if user is None:
            return jsonify(BaseResponse.response_error('User not found')), 404
        if data.get('name'):
            user.name = data['name']
        if data.get('email'):
            user.email = data['email']
        if data.get('new_password'):
            if not data.get('old_password'):
                return jsonify(BaseResponse.response_error('Old password is required')), 400
            if not checkpw(data['old_password'].encode('utf-8'), user.password.encode('utf-8')):
                return jsonify(BaseResponse.response_error('Old password is incorrect')), 400
            user.password = hashpw(data['new_password'].encode('utf-8'), gensalt()).decode('utf-8')
        db.session.commit()
        return jsonify(BaseResponse.response_success(user.to_dict())), 200
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400

    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def get_all_user_service():
    try:
        users = User.query.filter_by(role='user',deleted_at=None).all()
        return jsonify(BaseResponse.response_success([user.to_dict() for user in users])), 200
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500