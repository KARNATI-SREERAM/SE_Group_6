from parking_utils import validate_slot

def test_valid_slot():
    data = {
        "A": {
            "A1": {"status": True}
        }
    }
    assert validate_slot(data, "A1") is True


def test_invalid_row():
    data = {
        "A": {
            "A1": {"status": True}
        }
    }
    assert validate_slot(data, "B1") is False


def test_invalid_slot_in_row():
    data = {
        "A": {
            "A1": {"status": True}
        }
    }
    assert validate_slot(data, "A2") is False


def test_empty_slot_input():
    data = {
        "A": {
            "A1": {"status": True}
        }
    }
    assert validate_slot(data, "") is False
