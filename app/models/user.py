from app import app, db

# Definisikan model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    __tablename__ = 'users'

    def __repr__(self):
        return f'<User {self.name}>'