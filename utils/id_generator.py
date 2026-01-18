def generate_id(data, id_field):

    if not data:
        return 1

    max_id = 0

    for item in data:

        numeric_part = int(item[id_field].split("_")[1])
        if numeric_part > max_id:
            max_id = numeric_part

    return max_id + 1
