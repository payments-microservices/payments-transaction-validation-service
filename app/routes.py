from flask import request, jsonify
from app import app
from app.validation import validate_transaction

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    response = validate_transaction(data)
    return jsonify(response)
