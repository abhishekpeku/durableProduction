from app_setup import app


@app.activity_trigger(input_name="input")
def add_numbers(input: dict):
    return input["a"] + input["b"]


@app.activity_trigger(input_name="input")
def multiply_numbers(input: dict):
    return input["a"] * input["b"]