from contents import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(90), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    results = db.relationship('TestResult', backref='patient', lazy=True)

    def __repr__(self):
        return f"Users('{self.name}')"


class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(100), nullable=False)
    date_test = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"TestResult('{self.result}', '{self.date_test}')"

