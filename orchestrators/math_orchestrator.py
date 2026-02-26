import azure.durable_functions as df
from functions_app import durable_app


@durable_app.orchestration_trigger(context_name="context")
def math_orchestrator(context: df.DurableOrchestrationContext):

    retry_options = df.RetryOptions(first_retry_interval_in_milliseconds=5000, max_number_of_attempts=3)

    sum_result = yield context.call_activity_with_retry(
        "add_numbers",
        retry_options,
        {"a": 15, "b": 25}
    )

    multiply_result = yield context.call_activity(
        "multiply_numbers",
        {"a": sum_result, "b": 2}
    )

    return {
        "sum": sum_result,
        "double_sum": multiply_result
    }