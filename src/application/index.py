from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.configuration import db_config
from flask import jsonify, request
from service import transaction_type
from service import transaction

application = Flask(__name__)
db_configuration = db_config()
application.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://' + db_configuration.user_name + ':' + db_configuration.password + '@' + db_configuration.host + '/' + db_configuration.database
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(application)
application.app_context().push()

@application.route("/transaction_type/<int:id>",methods=['GET'])
def get_transaction_type(id):
	data = transaction_type.get(id)
	return jsonify(data), 200

@application.route("/transaction_type",methods=['GET'])
def get_all_transaction_types():
	print("checkkkkk")
	data = transaction_type.get_all()
	return jsonify(data)

@application.route("/transaction_type",methods=['POST'])
def post_transaction_type():
	data = request.get_json()
	updated_data = transaction_type.save(data)
	return jsonify(updated_data), 201

@application.route("/transaction_type/<int:id>",methods=['PUT'])
def update_transaction_type(id):
	data = request.get_json()
	updated_data = transaction_type.update(id, data)
	return jsonify(updated_data), 200

@application.route("/transaction_type/<int:id>",methods=['DELETE'])
def delete_transaction_type(id):
	result = transaction_type.delete(id)
	if result == True:
		return jsonify({"message":"Deleted"}), 204
	else:
		return jsonify({"message":"There is a problem"}), 500
	

@application.route("/transaction/<int:id>",methods=['GET'])
def get_transaction(id):
	data = transaction.get(id)
	return jsonify(data), 200

@application.route("/transaction",methods=['GET'])
def get_all_transactions():
	data = transaction.get_all()
	return jsonify(data)

@application.route("/transaction",methods=['POST'])
def post_transaction():
	data = request.get_json()
	updated_data = transaction.save(data)
	return jsonify(updated_data), 201

@application.route("/transaction/<int:id>",methods=['PUT'])
def update_transaction(id):
	data = request.get_json()
	transaction_data = transaction.update(id, data)
	return jsonify(transaction_data), 200

@application.route("/transaction/<int:id>",methods=['DELETE'])
def delete_transaction(id):
	result = transaction.delete(id)
	if result == True:
		return jsonify({"message":"Deleted"}), 204
	else:
		return jsonify({"message":"There is a problem"}), 500

@application.errorhandler(404)
def not_found(error):
	return jsonify({"message":"Resource not found"}),  404

@application.errorhandler(500)
def internal_server(error):
	return jsonify({"message":"Internal Server Error"}),  500

if __name__ == "__main__":
	application.run(debug=True)
