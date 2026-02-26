import azure.durable_functions as df
from app_setup import app


@app.orchestration_trigger(context_name="context")
def order_orchestrator(context: df.DurableOrchestrationContext):

    order = {
        "item": "Laptop",
        "price": 50000
    }

    validation = yield context.call_activity("validate_order", order)
    payment = yield context.call_activity("process_payment", order)

    return {
        "validation": validation,
        "payment": payment
    }