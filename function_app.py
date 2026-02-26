import azure.functions as func
import azure.durable_functions as df
import logging

app = func.FunctionApp()
durable_app = df.DurableApp()

# Import modules so decorators get registered
import orchestrators.math_orchestrator
import orchestrators.order_orchestrator
import activities.math_activities
import activities.order_activities


# =========================
# HTTP Starter - Math Workflow
# =========================
@app.route(route="start-math", methods=["POST"])
@durable_app.client_input(client_name="client")
async def start_math(req: func.HttpRequest, client):
    instance_id = await client.start_new("math_orchestrator")
    logging.info(f"Started Math Orchestration: {instance_id}")
    return client.create_check_status_response(req, instance_id)


# =========================
# HTTP Starter - Order Workflow
# =========================
@app.route(route="start-order", methods=["POST"])
@durable_app.client_input(client_name="client")
async def start_order(req: func.HttpRequest, client):
    instance_id = await client.start_new("order_orchestrator")
    logging.info(f"Started Order Orchestration: {instance_id}")
    return client.create_check_status_response(req, instance_id)