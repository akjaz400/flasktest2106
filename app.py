import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello! My web service is live on Render!"
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Render Web Service</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f7f6;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                text-align: center;
            }
            .btn {
                background-color: #ff4757;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                transition: background 0.2s;
            }
            .btn:hover {
                background-color: #e84118;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello! My web service is live on Render!</h1>
            <p>Click the button below to fetch live data from our API.</p>
            <!-- Clicking this button takes the user to the status endpoint -->
            <button class="btn" onclick="window.location.href='/api/status'">Check API Status</button>
        </div>
    </body>
    </html>
    """
    return html_content

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
