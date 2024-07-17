from storage import list_videos_in_date_range
from flask_cors import CORS
from camera import Camera
from flask import Flask, request, jsonify
from notification import send_notification


app = Flask(__name__)
CORS(app)

camera = Camera()

@app.route('/motion_detected', methods=['POST'])
def motion_detected():
    data = request.get_json

    if 'url' in data:
        print("URL: ", data['url'])
        send_notification(data["url"])
    else:
        print("'url' not in incoming data")

    return jsonify({}), 201