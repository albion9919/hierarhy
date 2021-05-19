def handler_t(column_name, decision_function, **kwargs):
    for pet, name in kwargs.items():
        print(f"{pet}: {name}")
    return 'x'
