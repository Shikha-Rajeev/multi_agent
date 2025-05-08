import json

def load_kpi_data(filepath):
    with open(filepath, "r") as file:
        return json.load(file)
