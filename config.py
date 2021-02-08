import pymongo
from app import application
from flask_pymongo import PyMongo
import pyAudioAnalysis , ffmpeg, pymongo, pydub, os, uuid, io, datetime

class Config(object):
    DEBUG= False
    TESTING = False

    SECRET_KEY = b'\x0b\xc8\xe1\xd9\xf7\xf6\xa9\xd9\xba\xd3\xfb\xa0\x16\x87\x80\xe4'
    DB_NAME = "production-db"
    
    #DEFAULT VARIABLES
    MAX_AUDIO_FILESIZE = 300000000
    SEPARATED_FOLDER = "../Flasklast/separatedfiles/"
    UPLOAD_FOLDER = "../Flasklast/audiofiles/"
    SPEC_FOLDER = "../Flasklast/spectrograms/"
    MEL_FOLDER = "../Flasklast/melspectrograms/"
    CHANNEL_FOLDER = "../Flasklast/channels/"
    TEMPO_FOLDER = "../Flasklast/tempographs/"
    QUALITY_FOLDER = "../Flasklast/QualitySpectrograms/"
    MONGO_URI = "mongodb+srv://Krisztian:Password1@flaskappcluster.5akml.mongodb.net/<dbname>?retryWrites=true&w=majority"

    
#DATABASE
application.config['MONGO_URI'] = "mongodb+srv://Krisztian:Password1@flaskappcluster.5akml.mongodb.net/Audiofiles?retryWrites=true&w=majority"
mongo = PyMongo(application)


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG= True
    TESTING = False

    SECRET_KEY = b'\x0b\xc8\xe1\xd9\xf7\xf6\xa9\xd9\xba\xd3\xfb\xa0\x16\x87\x80\xe4'
    DB_NAME = "production-db"
    #DATABASE
    client = pymongo.MongoClient("mongodb+srv://Krisztian:Password1@flaskappcluster.5akml.mongodb.net/<dbname>?retryWrites=true&w=majority")
    #DEFAULT VARIABLES
    MAX_AUDIO_FILESIZE = 300000000

class TestingConfig(Config):
    TESTING = True