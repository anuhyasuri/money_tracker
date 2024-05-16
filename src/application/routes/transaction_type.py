from flask_restful import Resource
from service.transaction_type import TransactionTypeService
from flask import request

class TransactionTypeRoute(Resource):
	def get(self, id):
		data = TransactionTypeService.get(id)
		return data, 200
	
	def put(self, id):
		data = request.get_json()
		updated_data = TransactionTypeService.update(id, data)
		return updated_data, 200
	
	def delete(self, id):
		result = TransactionTypeService.delete(id)
		if result == True:
			return {"message":"Deleted"}, 204
		else:
			return {"message":"There is a problem"}, 500