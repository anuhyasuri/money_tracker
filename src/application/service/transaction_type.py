from model.transaction_type import TransactionType
from schema.transaction_type_schema import TransactionTypeSchema
from index import db
from datetime import datetime, timezone

class TransactionTypeService():

	def get_all():
		transaction_types = TransactionType.get_all()
		serializer = TransactionTypeSchema(many = True)
		return serializer.dump(transaction_types)

	def get(id):
		transaction_type = TransactionType.get_by_id(id=id, cls=TransactionType)
		serializer = TransactionTypeSchema()
		return serializer.dump(transaction_type)
	
	def save(data):
		new_transactiontype = TransactionType(
			name = data.get('name')
		)
		new_transactiontype.save()
		serializer = TransactionTypeSchema()
		return serializer.dump(new_transactiontype)

	def update(id, data):
		transactiontype_to_update = TransactionType.get_by_id(id=id, cls=TransactionType)
		transactiontype_to_update.name = data.get("name")
		transactiontype_to_update.updated_date = datetime.now(timezone.utc)
		db.session.commit()
		serializer = TransactionTypeSchema()
		return serializer.dump(transactiontype_to_update)

	def delete(id):
		transactiontype_to_delete = TransactionType.get_by_id(id=id, cls=TransactionType)
		transactiontype_to_delete.delete()
		return True