# Flask-Chat-App

Demonstration of a Flask application with live chat functionality.  Comments are added to the page for all connected clients, and the page views automatically updates as well.

- **Live chat:**  Using Javascript, `SocketIO`, and `JQuery`.  All messages are sent to the Python web server, and then broadcast back to all clients.
- **Persistent chat:** Utilizing `flask-sqlalchemy`, all chat messages are saved and are added to the page for any other people joining the chat page.
- **Bad word filtering:** Submitted names and messages are sent through a filter to screen for bad language.  The sanitized strings are then broacast to connected clients, and saved to the database.
- **Admin backend:** Go to /super-secret-admin-page, and you'll have plenty of settings to configure the front page.  You can change the home page title, color, media image displayed (supports both images and video), enable and disable chat, and even reset page views and comments.
- **Robust:** Each message sent only results in a single write to the database, and zero reads.  Can support a large amount of simultaneous users.

# How to use
Included is `requirements.txt` to quickly install all dependencies using the command `pip install -r requirements.txt`. Using the Flask development server, simply run `run.py`.  You're set!
