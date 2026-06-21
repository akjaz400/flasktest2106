pip install flask

from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(Akjflask)

# Endpoint 1: A simple GET request that returns text
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my Python Web Service!"

# Endpoint 2: A GET request that returns JSON data
@app.route('/api/user', methods=['GET'])
def get_user():
    user_data = {
        "id": 101,
        "name": "Alice",
        "role": "Developer",
        "status": "Active"
    }
    return jsonify(user_data)

# Endpoint 3: A POST request that accepts user input
@app.route('/api/greet', methods=['POST'])
def greet_user():
    # Get the JSON payload sent by the user
    data = request.get_json()
    
    # Extract the 'name' field, default to 'Guest' if missing
    username = data.get('name', 'Guest')
    
    return jsonify({"message": f"Hello, {username}! Welcome to our service."})

# Run the server locally
if __name__ == '__main__':
    app.run(debug=True, port=5000)
