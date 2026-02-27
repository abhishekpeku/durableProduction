import azure.durable_functions as df
from app_setup import app


@app.orchestration_trigger(context_name="context")
async def order_orchestrator(context: df.DurableOrchestrationContext):

    order = {
        "item": "Laptop",
        "price": 50000
    }

    validation = await context.call_activity("validate_order", order)
    payment = await context.call_activity("process_payment", order)

    return {
        "validation": validation,
        "payment": payment
    }