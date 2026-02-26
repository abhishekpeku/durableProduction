import logging
import azure.functions as func
from app_setup import app

# Import all modules so decorators register
import orchestrators.math_orchestrator
import orchestrators.order_orchestrator
import activities.math_activities
import activities.order_activities


# =========================
# HTTP STARTER - MATH
# =========================
@app.route(route="start-math", methods=["POST"])
@app.durable_client_input(client_name="client")
async def start_math(req, client):
    instance_id = await client.start_new("math_orchestrator", None, None)
    logging.info(f"Started Math Orchestration: {instance_id}")
    return client.create_check_status_response(req, instance_id)


# =========================
# HTTP STARTER - ORDER
# =========================
@app.route(route="start-order", methods=["POST"])
@app.durable_client_input(client_name="client")
async def start_order(req, client):
    instance_id = await client.start_new("order_orchestrator", None, None)
    logging.info(f"Started Order Orchestration: {instance_id}")
    return client.create_check_status_response(req, instance_id)