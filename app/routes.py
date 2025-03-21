from flask import request, jsonify
from app import app
from app.validation import validate_transaction

@app.route('/validate', methods=['POST'])
def validate():
    # Check if content type is application/json
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type. Content-Type must be application/json"}), 415
    
    data = request.get_json()
    
    # Check if request body is present
    if not data:
        return jsonify({"error": "Request body is missing"}), 400
    
    # Extract id if present
    id = data.get("id", None)
    
    # Check for required fields
    required_fields = ["id", "payment_details", "metadata"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required", "id": id}), 400
    
    # Check for required fields in payment_details
    payment_details = data.get("payment_details", {})
    required_payment_fields = ["account_holder_payer", "account_holder_receiver", "amount", "currency"]
    for field in required_payment_fields:
        if field not in payment_details:
            return jsonify({"error": f"'payment_details.{field}' is required", "id": id}), 400
    
    # Check for required fields in metadata
    metadata = data.get("metadata", {})
    required_metadata_fields = ["timestamp", "payer_account_location", "receiver_account_location"]
    for field in required_metadata_fields:
        if field not in metadata:
            return jsonify({"error": f"'metadata.{field}' is required", "id": id}), 400
    
    response = validate_transaction(data)
    return jsonify(response)
