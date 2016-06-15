# Vue + Flask + websockets

This is a simple proof of concept for a web app using Vue for the front-end and Flask for the back-end and communicating with websockets.

## Running the app

1. Clone the repository
2. Install the Python prerequisites (into a virtualenv): `pip install -r back/requirements.txt`
3. Install the JavaScript prerequisites: `cd front && node install`
4. Run the back-end: `nohup back/app.py &`
5. Run the front-end: `cd front && npm run dev`
