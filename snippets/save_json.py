import json


def save_json_output(new_data, filename):
    """
    Saves data into json format with the given filename.
    """
    json_object = json.dumps(new_data, indent=4)
    with open(filename, "w") as outfile:
        outfile.write(json_object)
    with open(filename) as file:
        last_check_data = json.load(file)
        if new_data != last_check_data:
            raise "Data did not save error"
