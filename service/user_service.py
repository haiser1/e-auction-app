from models.users import User
from vallidation.user_validation import UpdateUserValidation
from base_response.base_response import BaseResponse
from flask import jsonify
import logging
from marshmallow import ValidationError

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