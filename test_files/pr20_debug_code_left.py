def process_order(order_id, amount):
    print(f"DEBUG: processing order {order_id}")
    print(f"DEBUG: amount = {amount}")
    result = charge_customer(amount)
    return result