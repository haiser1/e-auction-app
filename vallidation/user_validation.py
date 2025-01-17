from marshmallow import fields, validate
from . import ma

class UpdateUserValidation(ma.Schema):
        name = fields.String(required=False)
        email = fields.Email(required=False)
        old_password = fields.String(required=False)
        new_password = fields.String(required=False)
