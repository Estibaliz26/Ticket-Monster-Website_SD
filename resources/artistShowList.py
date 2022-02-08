from flask import Flask, g
from flask_restful import Resource, Api, reqparse
from datetime import datetime
from db import db, secret_key
from flask_migrate import Migrate
from models.artist import ArtistModel
from models.orders import OrdersModel
from models.accounts import AccountsModel
from models.orders import OrdersModel
from models.show import ShowModel  # also import table created with many-to-many relationship
from models.place import PlaceModel
from models.disciplines import DisciplineModel
from flask_cors import CORS
from flask import render_template
from decouple import config as config_decouple
from config import config


class ArtistShowsList(Resource):
    def get(self, id_artist):
        artist = ArtistModel.find_by_id(id_artist)
        if artist:
            shows = [show.json() for show in ShowModel.query.all() for artist in show.get_artists_from_show if
                     artist.id == id]
            if shows:
                return {'shows': shows}, 200
            else:
                return {'message': "No shows found"}, 404
        else:
            return {'message': 'Artist not found'}, 404
