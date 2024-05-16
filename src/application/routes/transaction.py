from flask_restful import Resource, Api
from index import application
from service.transaction import TransactionService
from flask import jsonify, request

api = Api(application)

class TransactionRoute(Resource):
	def get(id):	
		print("inside get")
		data = TransactionService.get(id)
		return jsonify(data), 200
	def get_all():
		data = TransactionService.get_all()
		return jsonify(data)
	def post():
		data = request.get_json()
		updated_data = TransactionService.save(data)
		return jsonify(updated_data), 201
	def put(id):
		data = request.get_json()
		updated_data = TransactionService.update(id, data)
		return jsonify(updated_data), 200
	def delete(id):
		result = TransactionService.delete(id)
		if result == True:
			return jsonify({"message":"Deleted"}), 204
		else:
			return jsonify({"message":"There is a problem"}), 500
		
api.add_resource(TransactionRoute, '/transaction','/transaction/<string:id>')