#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

from release_config import ReleaseConfig


app = Flask(__name__)
api = Api(app)
app.config.from_object(ReleaseConfig)
db = SQLAlchemy(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
	from resources.user import UserApi
	from resources.history import HistoryApi
	from resources.favourites import FavouritesApi

	api.add_resource(UserApi, '/api/user')
	api.add_resource(HistoryApi, '/api/history')
	api.add_resource(FavouritesApi, '/api/favourites')
	app.run(host=app.config['HOST_IP'])
