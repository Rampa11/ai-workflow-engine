def evaluate_condition(condition, data):
    if condition == "status == HOT":
        return data.get("status") == "HOT"
    return False


from app.actions import send_email_action, log_action


def execute_actions(actions, data):
    results = []

    for action in actions:
        if action == "send_email":
            results.append(send_email_action(data))
        elif action == "log":
            results.append(log_action(data))

    return results


def run_workflow(workflow, data):
    if evaluate_condition(workflow["condition"], data):
        return execute_actions(workflow["actions"], data)

    return ["No action taken"]