from marshmallow import Schema, fields

class TransactionTypeSchema(Schema):
	id = fields.Integer()
	name = fields.String()
	created_date = fields.DateTime()
	updated_date = fields.DateTime()