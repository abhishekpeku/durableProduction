import logging
from functions_app import durable_app


@durable_app.activity_trigger(input_name="input_data")
def add_numbers(input_data: dict):
    a = input_data["a"]
    b = input_data["b"]
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")
    return result


@durable_app.activity_trigger(input_name="input_data")
def multiply_numbers(input_data: dict):
    a = input_data["a"]
    b = input_data["b"]
    result = a * b
    logging.info(f"Multiplying {a} * {b} = {result}")
    return result