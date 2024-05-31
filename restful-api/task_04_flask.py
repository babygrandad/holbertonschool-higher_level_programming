# Import necessary modules from Flask
from flask import Flask, jsonify, request

# Instantiate the Flask app
app = Flask(__name__)

# Sample data stored in memory
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Define the root route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Define the /data route to show all usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))

# Define the /status route
@app.route('/status')
def status():
    return "OK"

# Define a dynamic route to fetch user details
@app.route('/users/<username>')
def user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Define the /add_user route to handle POST requests
@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    
    # Check if the username already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add new user to the dictionary
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data})

# Check if the script is the main program and run the server
if __name__ == "__main__":
    app.run(debug=True)  # Turn on debug mode for development purposes
