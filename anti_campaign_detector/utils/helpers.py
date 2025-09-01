def pretty_print(title, data):
    print(f"\n==== {title} ====")
    if isinstance(data, list) or isinstance(data, dict):
        print(data)
    else:
        print(str(data))
