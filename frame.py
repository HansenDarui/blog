from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(12), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=True)
    bio = db.Column(db.String(200), nullable=True)
    occupation = db.Column(db.String(64), nullable=True)





def connect_to_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    db.drop_all()
    db.create_all()
    connect_to_db(app)
    print("Connected to DB.")

