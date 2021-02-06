from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


web_app = Flask(__name__)
socketio = SocketIO(web_app)
web_app.debug = True
web_app.config['SECRET_KEY'] = 'xZxM5GMQ37CQw9kf6SRS33LadZTpSKt6'
web_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
database = SQLAlchemy(web_app)
from .main import main as main_blueprint
web_app.register_blueprint(main_blueprint)
# socketio.init_app(web_app)
