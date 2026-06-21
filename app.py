import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello! My web service is live on Render!"

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "online",
        "platform": "Render",
        "message": "API is responding perfectly."
    })

# This part ensures Render can pass its own PORT variable to your app
if __name__ == '__main__':
    # Render injects the PORT environment variable automatically
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 so the app is accessible externally
    app.run(host='0.0.0.0', port=port)
