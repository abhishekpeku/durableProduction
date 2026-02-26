from app_setup import durable_app


@durable_app.activity_trigger(input_name="order_data")
def validate_order(order_data: dict):
    return True


@durable_app.activity_trigger(input_name="order_data")
def process_payment(order_data: dict):
    return f"Payment of {order_data['amount']} successful"


@durable_app.activity_trigger(input_name="order_data")
def update_inventory(order_data: dict):
    return "Inventory updated"


@durable_app.activity_trigger(input_name="order_data")
def send_confirmation(order_data: dict):
    return f"Confirmation sent for {order_data['order_id']}"