from flask_restful import Resource, Api
from index import application
from service.transaction_type import TransactionTypeService
from flask import jsonify, request

api = Api(application)

class TransactionTypeRoute(Resource):
	def get(id):	
		data = TransactionTypeService.get(id)
		return jsonify(data), 200
	def get_all():
		data = TransactionTypeService.get_all()
		return jsonify(data)
	def post():
		data = request.get_json()
		updated_data = TransactionTypeService.save(data)
		return jsonify(updated_data), 201
	def put(id):
		data = request.get_json()
		updated_data = TransactionTypeService.update(id, data)
		return jsonify(updated_data), 200
	def delete(id):
		result = TransactionTypeService.delete(id)
		if result == True:
			return jsonify({"message":"Deleted"}), 204
		else:
			return jsonify({"message":"There is a problem"}), 500
		
api.add_resource(TransactionTypeRoute, '/transaction_type','/transaction_type/<string:id>')