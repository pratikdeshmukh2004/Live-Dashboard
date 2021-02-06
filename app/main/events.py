from better_profanity import profanity
from flask_socketio import emit, send

from datetime import datetime
import json

from .. import database, socketio
from .models import Meals


# Faster to initialize variable here vs doing it every function call, per library documentation.
profanity.load_censor_words()

@socketio.on('message')
def handle_message(msg):
    global profane
    name = msg['name']
    content = msg['content']
    image = msg['image']

    name_cleaned = profanity.censor(name)
    content_cleaned = profanity.censor(content)

    now = datetime.now().strftime('%A %I:%M:%S %p').lstrip("0").replace(" 0", " ")

    message_object = Meals(name=name_cleaned, content=content_cleaned, image=image)
    database.session.add(message_object)
    database.session.commit()

    json_data = {
        'name' : name_cleaned,
        'content' : content_cleaned,
        'image' : image
    }

    send({'json_data' : json_data}, broadcast=True)