import azure.durable_functions as df
from app_setup import app


@app.orchestration_trigger(context_name="context")
async def math_orchestrator(context: df.DurableOrchestrationContext):

    result1 = await context.call_activity("add_numbers", {"a": 10, "b": 20})
    result2 = await context.call_activity("multiply_numbers", {"a": result1, "b": 5})

    return {
        "addition": result1,
        "multiplication": result2
    }