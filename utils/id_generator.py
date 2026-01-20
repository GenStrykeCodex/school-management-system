def generate_id(data, id_field, prefix="ID_"):

    if not data:
        return f"{prefix}1"

    max_id = 0

    for item in data:

        numeric_part = int(item[id_field].split("_")[1])
        if numeric_part > max_id:
            max_id = numeric_part

    return f"{prefix}{str(max_id + 1)}"
