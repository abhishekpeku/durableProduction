import logging
from functions_app import durable_app


@durable_app.activity_trigger(input_name="order_data")
def validate_order(order_data: dict):
    logging.info(f"Validating order {order_data['order_id']}")
    return True


@durable_app.activity_trigger(input_name="order_data")
def process_payment(order_data: dict):
    logging.info(f"Processing payment of {order_data['amount']}")
    return "Payment successful"


@durable_app.activity_trigger(input_name="order_data")
def update_inventory(order_data: dict):
    logging.info(f"Updating inventory for {order_data['order_id']}")
    return "Inventory updated"


@durable_app.activity_trigger(input_name="order_data")
def send_confirmation(order_data: dict):
    logging.info(f"Sending confirmation for {order_data['order_id']}")
    return "Confirmation sent"