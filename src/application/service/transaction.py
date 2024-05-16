from model.transaction import Transaction
from schema.transaction_schema import TransactionSchema
from index import db
from datetime import datetime, timezone

class TransactionService():

	def get_all():
		transactions = Transaction.get_all()
		serializer = TransactionSchema(many = True)
		return serializer.dump(transactions)

	def get(id):
		transaction = Transaction.get_by_id(id=id, cls=Transaction)
		serializer = TransactionSchema()
		return serializer.dump(transaction)

	def save(data):
		new_transaction = Transaction(
			name = data.get('name'),
			type = data.get('type'),
			amount = data.get('amount')
		)
		new_transaction.save()
		serializer = TransactionSchema()
		return serializer.dump(new_transaction)

	def update(id, data):
		transaction_to_update = Transaction.get_by_id(id=id, cls=Transaction)
		if data.get("name") != None:
			transaction_to_update.name = data.get("name")
		if data.get("type") != None:
			transaction_to_update.type = data.get("type")
		if data.get("amount") != None:
			transaction_to_update.amount = data.get("amount")
		transaction_to_update.updated_date = datetime.now(timezone.utc)
		db.session.commit()
		serializer = TransactionSchema()
		return serializer.dump(transaction_to_update)

	def delete(id):
		transaction_to_delete = Transaction.get_by_id(id=id, cls=Transaction)
		transaction_to_delete.delete()
		return True