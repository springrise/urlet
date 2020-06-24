from db import db


class UrlModel(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    urlet = db.Column(db.String)

    def __init__(self, url, urlet):
        self.url = url
        self.urlet = urlet

    def json(self):
        return {
            'url': self.url,
            'urlet': self.urlet
        }

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_urlet(cls, urlet):
        return cls.query.filter_by(urlet=urlet).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

