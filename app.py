from flask import Flask
from flask_restful import Api

from db import db
from resources.url import Url, Urlet

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "SEKRET_KEY"

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Url, "/url")
api.add_resource(Urlet, '/<string:urlet>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

