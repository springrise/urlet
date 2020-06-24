from flask import redirect
from flask_restful import Resource, reqparse
from models.url import UrlModel
import secrets
import string


class Url(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url',
                            type=str,
                            required=True,
                            help="This field can not be blank."
                            )
        data = parser.parse_args()

        urlet = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(7))

        url = UrlModel(data['url'], urlet)

        try:
            url.save_to_db()
        except:
            return {'message': 'An error occurred inserting the url.'}, 500

        return url.json(), 201


class Urlet(Resource):

    def get(self, urlet):
        urlet = UrlModel.find_by_urlet(urlet)
        if not urlet:
            return {'message': 'urlet not found.'}
        url = urlet.url
        return redirect(url, code=302)


