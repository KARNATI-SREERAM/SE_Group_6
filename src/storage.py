import json

DATA_PATH = "./data/data.json"


def save_data(data):
    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent=2)


def load_data():
    try:
        with open(DATA_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        data = {
            "A": {
                "A1": {"status": True, "last_updated": None, "user_id": None},
                "A2": {"status": True, "last_updated": None, "user_id": None},
                "A3": {"status": True, "last_updated": None, "user_id": None},
            },
            "B": {
                "B1": {"status": True, "last_updated": None, "user_id": None},
                "B2": {"status": True, "last_updated": None, "user_id": None},
                "B3": {"status": True, "last_updated": None, "user_id": None},
            },
            "C": {
                "C1": {"status": True, "last_updated": None, "user_id": None},
                "C2": {"status": True, "last_updated": None, "user_id": None},
                "C3": {"status": True, "last_updated": None, "user_id": None},
            },
        }
        save_data(data)
        return data
