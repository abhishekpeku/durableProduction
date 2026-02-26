import azure.durable_functions as df
from functions_app import durable_app


@durable_app.orchestration_trigger(context_name="context")
def order_orchestrator(context: df.DurableOrchestrationContext):

    order_data = {
        "order_id": "ORD123",
        "amount": 5000
    }

    validation = yield context.call_activity("validate_order", order_data)

    if not validation:
        return "Order validation failed"

    payment_status = yield context.call_activity("process_payment", order_data)

    inventory_status = yield context.call_activity("update_inventory", order_data)

    notification = yield context.call_activity("send_confirmation", order_data)

    return {
        "payment": payment_status,
        "inventory": inventory_status,
        "notification": notification
    }