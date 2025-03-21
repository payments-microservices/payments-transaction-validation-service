def validate_transaction(data):
    amount = data['payment_details']['amount']
    currency = data['payment_details']['currency']
    payer_location = data['metadata']['payer_account_location']
    receiver_location = data['metadata']['receiver_account_location']

    if amount > 10000:
        status = "REJECT"
    elif amount > 5000:
        status = "MANUAL_REVIEW_NEEDED"
    elif payer_location != receiver_location:
        status = "MANUAL_REVIEW_NEEDED"
    else:
        status = "VALID"

    return {
        "id": data['id'],
        "status": status
    }
