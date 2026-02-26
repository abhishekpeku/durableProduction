from app_setup import durable_app


@durable_app.activity_trigger(input_name="input_data")
def add_numbers(input_data: dict):
    return input_data["a"] + input_data["b"]


@durable_app.activity_trigger(input_name="input_data")
def multiply_numbers(input_data: dict):
    return input_data["a"] * input_data["b"]