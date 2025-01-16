from flask import request
from service.auth_service import register_service, login_service

def register_controller():
    request_data = request.get_json()
    response_data = register_service(request_data)
    return response_data

def login_controller():
    request_data = request.get_json()
    response_data = login_service(request_data)
    return response_data