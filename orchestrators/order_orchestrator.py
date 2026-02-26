import azure.durable_functions as df
from app_setup import durable_app


@durable_app.orchestration_trigger(context_name="context")
def order_orchestrator(context: df.DurableOrchestrationContext):

    order_data = {
        "order_id": "ORD1001",
        "amount": 5000
    }

    is_valid = yield context.call_activity("validate_order", order_data)

    if not is_valid:
        return {"status": "Validation Failed"}

    payment_status = yield context.call_activity("process_payment", order_data)

    inventory_status = yield context.call_activity("update_inventory", order_data)

    confirmation = yield context.call_activity("send_confirmation", order_data)

    return {
        "validation": "Passed",
        "payment": payment_status,
        "inventory": inventory_status,
        "confirmation": confirmation
    }