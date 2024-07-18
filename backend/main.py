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

@app.route('/arm', methods=['POST'])
def arm():
    camera.arm()
    return jsonify(message="System armed"), 200

@app.route('/disarm', methods=['POST'])
def disarm():
    camera.disarm()
    return jsonify(message='System disarmed'), 200

@app.route('/get-armed', methods=['GET'])
def get_armed():
    return jsonify(armed=camera.armed), 200

@app.route('/get-logs')
def get_logs():
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')

    logs = list_videos_in_date_range(start_date, end_date)
    return jsonify ({'logs': logs}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)