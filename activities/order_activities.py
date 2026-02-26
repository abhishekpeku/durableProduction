from app_setup import app


@app.activity_trigger(input_name="input")
def validate_order(input: dict):
    return f"Order for {input['item']} validated"


@app.activity_trigger(input_name="input")
def process_payment(input: dict):
    return f"Payment of {input['price']} processed"