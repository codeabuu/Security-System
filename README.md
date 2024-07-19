# Security-System

This is a python security system that uses OpenCV and a basic person detection model to record and save video. It features the following:

### Features
- **Person Detection:** Utilizes a pre-trained model to detect persons in the camera feed.
- **Video Storage:** Saves recorded video to Google Cloud Object-Storage.
- **Text Notifications:** Uses Twilio to send notifications to your phone upon person detection.
- **Arming & Disarming:**  Allows the system to be armed or disarmed remotely.
- **Activity Logs:** Maintains logs of all activities and detections.

## Installation

### Prerequisites

Before starting, ensure you have the following installed:
* Pyhton 3.9+
* Node.js
* ffmpeg

### Backend Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/codeabuu/Security-System.git
    cd Security-System
    ```
2. Install python dependencies:
    ```bash
    pip install -r requiremnts.txt
    ```
### Frontend Installation

1. Navigate to the frontend directory and install the dependencies:
```bash
cd frontend
npm install
```

## Running the system

### Running backend

To start the backend, navigate to the backend directory and run the main.py file:

```bash
cd backend
python main.py
```

### Running frontend

To start the frontend, navigate to the frontend directory and run:
```bash
npm start
```

## Configuration

### Google Cloud Storage

Ensure you have configured Google Cloud Storage for video storage. Set up your Google Cloud credentials and update the necessary configurations in the `storage.py` file.

Here is step-by-step (guide)[https://g.co/gemini/share/152a62030ff7] on how to onfigure Google Cloud-credentials.

### Notifications

Configure your text notification service, which in our case is Twilio, by providing the necessary API keys and phone numbers in the configuration file, `.env`.

## Usage

### Arming and Disarming the System

Use the frontend interface to arm and disarm the system. When armed, the system will continuously monitor the camera feed for person detection.

### Viewing Logs

Access the activity logs through the frontend interface to review all detection events and system activities.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## Acknowledgements

* OpenCV for the powerful computer vision library.
* Google Cloud for the cloud storage services.
* Node.js and npm for the frontend framework.


