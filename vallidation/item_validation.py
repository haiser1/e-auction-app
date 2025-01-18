from marshmallow import fields, validate
from . import ma

class CreateItemValidation(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, error="name cannot be empty"))
    description = fields.String(required=True, validate=validate.Length(min=1, error="description cannot be empty"))
    starting_price = fields.Float(required=True, validate=validate.Range(min=0, error="starting price cannot be negative"))

class GetItemPagginationValidation(ma.Schema):
    page = fields.Integer(required=False, default=1, validate=validate.Range(min=1, error="page cannot be negative"))
    limit = fields.Integer(required=False, default=10, validate=validate.Range(min=1, error="limit cannot be negative"))
    