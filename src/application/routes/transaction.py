from flask_restful import Resource
from service.transaction import TransactionService
from flask import request

class TransactionRoute(Resource):
	def get(self, id):
		data = TransactionService.get(id)
		return data, 200
	
	def put(self, id):
		data = request.get_json()
		updated_data = TransactionService.update(id, data)
		return updated_data, 200
	
	def delete(self, id):
		result = TransactionService.delete(id)
		if result == True:
			return {"message":"Deleted"}, 204
		else:
			return {"message":"There is a problem"}, 500
