from users_app import db


class Users(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    street = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    zipcode = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(40), nullable=True)

    def __repr__(self):
        return f"<User {self.user_id}: {self.name}, {self.city}, {self.zipcode}, {self.status}>"
