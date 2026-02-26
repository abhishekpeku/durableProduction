import azure.durable_functions as df
from app_setup import app


@app.orchestration_trigger(context_name="context")
def math_orchestrator(context: df.DurableOrchestrationContext):

    result1 = yield context.call_activity("add_numbers", {"a": 10, "b": 20})
    result2 = yield context.call_activity("multiply_numbers", {"a": result1, "b": 5})

    return {
        "addition": result1,
        "multiplication": result2
    }