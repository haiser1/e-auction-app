from marshmallow import validate
from marshmallow import fields, ValidationError, validates
from datetime import datetime
from . import ma

class CustomDateField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            # Parse tanggal dalam format "DD-MM-YYYY"
            return datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise ValidationError("Invalid date format. Expected format: DD-MM-YYYY")

class CreateAuctionValidation(ma.Schema):
    item_id = fields.Integer(required=True, validate=validate.Range(min=1, error="item id cannot be negative or zero"))
    close_biding = CustomDateField(required=True)

    @validates("close_biding")
    def validate_future_date(self, value):
        if value < datetime.now():
            raise ValidationError("close biding must be a future date")