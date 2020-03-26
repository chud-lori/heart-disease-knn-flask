from . import db
from corpe import db, login_manager
from flask_login import UserMixin

class Dataset(db.Model):
    """Model for datasets."""

    __tablename__ = 'datasets'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.SmallInteger, nullable=False)
    cp = db.Column(db.SmallInteger, nullable=False)
    trestbps = db.Column(db.Integer, nullable=False)
    chol = db.Column(db.Integer, nullable=False)
    fbs = db.Column(db.SmallInteger, nullable=False)
    restecg = db.Column(db.SmallInteger, nullable=False)
    thalach = db.Column(db.Integer, nullable=False)
    exang = db.Column(db.SmallInteger, nullable=False)
    oldpeak = db.Column(db.Float, nullable=False)
    slope = db.Column(db.SmallInteger, nullable=False)
    ca = db.Column(db.SmallInteger, nullable=False)
    thal = db.Column(db.SmallInteger, nullable=False)
    target = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Age {}>'.format(self.age)

@login_manager.user_loader
def load_user(user_id):
	return Admin.query.get(int(user_id))
class Admin(db.Model, UserMixin):
    """Model for admin"""

    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<Username {}>'.format(self.username)