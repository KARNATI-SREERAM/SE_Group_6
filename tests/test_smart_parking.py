import pytest
from unittest.mock import patch
from src.parking_utils import validate_slot, info
from src.parking_actions import book_parking_slot, release_parking_slot


@pytest.fixture
def clean_data():
    return {
        "A": {
            "A1": {"status": True, "last_updated": None, "user_id": None},
            "A2": {
                "status": False,
                "last_updated": "2026-01-22",
                "user_id": "user_old",
            },
        },
        "B": {"B1": {"status": True, "last_updated": None, "user_id": None}},
    }


def test_validate_slot_valid(clean_data):
    assert validate_slot(clean_data, "A1") is True


def test_validate_slot_invalid(clean_data):
    assert validate_slot(clean_data, "Z9") is False


@patch("src.parking_actions.save_data")
def test_book_available_slot(mock_save, clean_data, monkeypatch):
    inputs = iter(["user1", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    book_parking_slot(clean_data, "A1")

    # Assertions for memory
    assert clean_data["A"]["A1"]["status"] is False
    assert clean_data["A"]["A1"]["user_id"] == "user1"

    # Assert that save_data was "called" without actually touching the disk
    assert mock_save.called


def test_book_occupied_slot(clean_data, monkeypatch):
    book_parking_slot(clean_data, "A2")
    assert clean_data["A"]["A2"]["status"] is False
    assert clean_data["A"]["A2"]["user_id"] == "user_old"


@patch("src.parking_actions.save_data")
def test_release_occupied_slot(mock_save, clean_data, monkeypatch):
    inputs = iter(["user_old", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    release_parking_slot(clean_data, "A2")
    assert clean_data["A"]["A2"]["status"] is True
    assert clean_data["A"]["A2"]["user_id"] is None

    # Assert that save_data was "called" without actually touching the disk
    assert mock_save.called


def test_release_wrong_id(clean_data, monkeypatch):
    inputs = iter(["wrong_user", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    release_parking_slot(clean_data, "A2")
    assert clean_data["A"]["A2"]["status"] is False


def test_info_counts(clean_data):
    total, available, occupied = info(clean_data)
    assert total == 3
    assert available == 2
    assert occupied == 1


def test_info_empty_data():
    empty_data = {}
    total, available, occupied = info(empty_data)
    assert total == 0
    assert available == 0
    assert occupied == 0
