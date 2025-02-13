import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    :param data: Dictionary to serialize
    :param filename: Output JSON file
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    :param filename: Input JSON file
    :return: Deserialized Python dictionary
    """
    with open(filename, 'r') as file:
        return json.load(file)
