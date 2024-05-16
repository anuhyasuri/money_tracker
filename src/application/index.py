from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.configuration import db_config

application = Flask(__name__)
db_configuration = db_config()
application.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://' + db_configuration.user_name + ':' + db_configuration.password + '@' + db_configuration.host + '/' + db_configuration.database
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(application)
application.app_context().push()
	
if __name__ == "__main__":
	application.run(debug=True)
