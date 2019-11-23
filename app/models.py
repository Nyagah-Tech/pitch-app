from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200))
    pass_code_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('you cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_code_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_code_secure,password)

    def __repr__(self):
        return f'User {self.username}'