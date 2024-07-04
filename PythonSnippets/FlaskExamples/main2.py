from flask import Flask, jsonify, request, abort

app = Flask(__name__)

dog = {
    'name': 'clifford',
    'color': 'red',
    'friends': ['bentley', 'emily', 'jax'],
}

@app.route('/get-dog', methods=['GET'])
def get_dog():
    return dog

@app.route('/get-dog-name', methods=['GET'])
def get_dog_name():
    return dog['name']

@app.route('/get-dog-color', methods=['GET'])
def get_dog_color():
    return dog['color']

@app.route('/change-dog-color', methods=['POST'])
def change_dog_color():
    newColor = request.json['color']
    dog['color'] = newColor
    return jsonify(dog['color']), 201

@app.route('/get-dog-friends', methods=['GET'])
def get_dog_friends():
    return jsonify(dog['friends']), 200

@app.route('/add-friend', methods=['POST'])
def add_friend():
    ## your code here
    return None

@app.route('/delete-dog-friend', methods=['DELETE'])
def delete_dog_friend():
    ## your code here
    return None

if __name__ == '__main__':
    app.run(debug=True, port=4000)