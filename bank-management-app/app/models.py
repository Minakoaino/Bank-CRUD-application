from app import db

class Bank(db.Model):
    __tablename__ = 'Banks'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
