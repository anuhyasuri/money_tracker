from index import db
from datetime import datetime

class TransactionType(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	name = db.Column(db.String(255),nullable=False)
	created_date = db.Column(db.DateTime(timezone=True), default = datetime.now(), nullable = False)
	updated_date = db.Column(db.DateTime(timezone=True), default = datetime.now(), nullable = False)

	def __repr__(self):
		return self.name
	
	@classmethod
	def get_all(cls):
		return cls.query.all()
	
	def get_by_id(cls,id):
		return cls.query.get_or_404(id)
	
	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()
