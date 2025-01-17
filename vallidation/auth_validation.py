from marshmallow import fields, validate
from . import ma

class RegisterValidation(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, error="name cannot be empty"))
    email = fields.Email(required=True, validate=validate.Length(min=1, error="Email cannot be empty"))
    password = fields.String(required=True, validate=validate.Length(min=1, error="Password cannot be empty"))

class LoginValidation(ma.Schema):
    email = fields.Email(required=True, validate=validate.Length(min=1, error="Email cannot be empty"))
    password = fields.String(required=True, validate=validate.Length(min=1, error="Password cannot be empty"))