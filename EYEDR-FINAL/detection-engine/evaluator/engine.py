def evaluate_condition(event, condition):
    field = condition["field"]
    operator = condition["operator"]
    expected = condition["value"]

    actual = event.get(field)

    if actual is None:
        return False

    actual = str(actual).lower()

    if operator == "equals":
        return actual == str(expected).lower()

    elif operator == "contains":
        return str(expected).lower() in actual

    elif operator == "contains_any":
        return any(
            str(value).lower() in actual
            for value in expected
        )

    elif operator == "starts_with":
        return actual.startswith(str(expected).lower())

    elif operator == "ends_with":
        return actual.endswith(str(expected).lower())

    return False


def evaluate_rule(event, rule):
    conditions = rule.get("conditions", [])

    for condition in conditions:
        if not evaluate_condition(event, condition):
            return False

    return True