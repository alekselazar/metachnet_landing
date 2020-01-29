from sqlalchemy.ext.hybrid import hybrid_property

from app import db

class Subscribed(db.Model):

    __tablename__ = 'subscribed'
    name = db.Column(db.String)
    fname = db.Column(db.String)
    email = db.Column(db.String, primary_key = True)

    def get_email(self):
        return self.email

    def get_name(self):
    	return self.name

    def get_fname(self):
    	return self.fname

db.create_all()
