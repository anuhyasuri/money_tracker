from marshmallow import Schema, fields

class TransactionSchema(Schema):
	id = fields.Integer()
	name = fields.String()
	type = fields.String()
	amount = fields.Float()
	created_date = fields.DateTime()
	updated_date = fields.DateTime()