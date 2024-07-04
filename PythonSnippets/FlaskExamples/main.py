from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data (simulating a shopping cart)
cart = [
    {"id": 1, "product": "Apple", "quantity": 3},
    {"id": 2, "product": "Banana", "quantity": 4},
    {"id": 3, "product": "Orange", "quantity": 7}
]
next_id = 4  # To simulate auto-incrementing IDs


# GET all items in the cart
@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart), 200


# GET a specific item in the cart by ID
@app.route('/cart/<int:item_id>', methods=['GET'])
def get_cart_item(item_id):
    item = next((item for item in cart if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        abort(404, f"Item with id {item_id} not found in cart")


# POST to add a new item to the cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    global next_id
    if not request.json or 'product' not in request.json or 'quantity' not in request.json:
        abort(400, "Invalid request, 'product' and 'quantity' are required")
    new_item = {
        'id': next_id,
        'product': request.json['product'],
        'quantity': request.json['quantity']
    }
    cart.append(new_item)
    next_id += 1
    return jsonify(new_item), 201


# PUT to update an existing item in the cart
@app.route('/cart/<int:item_id>', methods=['PUT'])
def update_cart_item(item_id):
    item = next((item for item in cart if item['id'] == item_id), None)
    if not item:
        abort(404, f"Item with id {item_id} not found in cart")
    if not request.json:
        abort(400, "Invalid request, JSON data expected")
    item['product'] = request.json.get('product', item['product'])
    item['quantity'] = request.json.get('quantity', item['quantity'])
    return jsonify(item), 200


# PATCH to update quantity of an existing item in the cart
@app.route('/cart/<int:item_id>', methods=['PATCH'])
def update_cart_quantity(item_id):
    item = next((item for item in cart if item['id'] == item_id), None)
    if not item:
        abort(404, f"Item with id {item_id} not found in cart")
    if not request.json:
        abort(400, "Invalid request, JSON data expected")
    if 'quantity' in request.json:
        item['quantity'] = request.json['quantity']
    return jsonify(item), 200


# DELETE an item from the cart by ID
@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    global cart
    cart = [item for item in cart if item['id'] != item_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)