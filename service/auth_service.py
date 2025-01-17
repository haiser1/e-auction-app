import datetime
import logging
import jwt
from models.user import User
from vallidation.auth_validation import RegisterValidation, LoginValidation
from base_response.base_response import BaseResponse
from flask import jsonify
from bcrypt import hashpw, checkpw, gensalt
from config import db, JWT_SECRET_KEY
from marshmallow import ValidationError

def register_service(request_data):
    try:
        data = RegisterValidation().load(request_data)
        email = User.query.filter_by(email=data['email'], deleted_at=None).first()

        if email is not None:
            return jsonify(BaseResponse.response_error('Email already exists')), 400
        hash_password = hashpw(data['password'].encode('utf-8'), gensalt()).decode('utf-8')

        user = User(name=data['name'], email=data['email'], password=hash_password, role='user')
        db.session.add(user)
        db.session.commit()
        return jsonify(BaseResponse.response_success(user.to_dict())), 201
    
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400

    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500
    
def login_service(request_data):
    try:
        data = LoginValidation().load(request_data)
        user = User.query.filter_by(email=data['email'], deleted_at=None).first()

        if user is None:
            return jsonify(BaseResponse.response_error('Email or password is incorrect')), 400
        if not checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
            return jsonify(BaseResponse.response_error('Email or password is incorrect')), 400
        
        payload = {
            'id': user.id,
            'name': user.name,
            'role': user.role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        }
        token = jwt.encode(payload, str(JWT_SECRET_KEY), algorithm='HS256')


        return jsonify(BaseResponse.response_success({'token': token})), 200

    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400

    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500