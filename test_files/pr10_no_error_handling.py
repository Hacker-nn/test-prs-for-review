def process_payment(amount, card_number):
    charge = amount * 1.1
    result = payment_gateway.charge(card_number, charge)
    return result