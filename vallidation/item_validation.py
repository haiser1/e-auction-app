from marshmallow import fields, validate
from . import ma

class CreateItemValidation(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, error="name cannot be empty"))
    description = fields.String(required=True, validate=validate.Length(min=1, error="description cannot be empty"))
    starting_price = fields.Float(required=True, validate=validate.Range(min=0, error="starting price cannot be negative"))