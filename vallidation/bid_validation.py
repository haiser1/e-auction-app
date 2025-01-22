from marshmallow import fields, validate
from . import ma

class CreateBidValidation(ma.Schema):
    bid_amount = fields.Float(required=True, validate=validate.Range(min=1, error="bid amount cannot be negative or zero"))