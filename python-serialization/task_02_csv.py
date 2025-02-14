import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file named data.json.

    :param csv_filename: The name of the CSV file to convert
    :return: True if conversion is successful, False otherwise
    """
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
