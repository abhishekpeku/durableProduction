import azure.durable_functions as df
from app_setup import durable_app


@durable_app.orchestration_trigger(context_name="context")
def math_orchestrator(context: df.DurableOrchestrationContext):

    sum_result = yield context.call_activity(
        "add_numbers",
        {"a": 10, "b": 20}
    )

    multiply_result = yield context.call_activity(
        "multiply_numbers",
        {"a": sum_result, "b": 2}
    )

    return {
        "sum": sum_result,
        "double_sum": multiply_result
    }