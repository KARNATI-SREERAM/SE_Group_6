import time
from datetime import datetime

from src.parking_utils import validate_slot
from src.storage import save_data


def book_parking_slot(data, slot):
    if not validate_slot(data, slot):
        print(f"Error: Slot '{slot}' does not exist.")
        print("Please wait ...")
        time.sleep(2)
        return

    if data[slot[0]][slot]["status"]:
        user_id = input("Enter Id: ")
        val = input(f"Are you sure you want to book Slot {slot}? (y/n): ").lower()

        if val == "y":
            data[slot[0]][slot]["status"] = False
            data[slot[0]][slot]["user_id"] = user_id
            data[slot[0]][slot]["last_updated"] = datetime.now().isoformat()
            save_data(data)
            print(f"Slot {slot} successfully booked!")
        else:
            print(f"Slot {slot} booking cancelled!")
    else:
        print(f"Slot {slot} is already occupied.")

    print("Please wait ...")
    time.sleep(2)


def release_parking_slot(data, slot):
    if not validate_slot(data, slot):
        print(f"Error: Slot '{slot}' does not exist.")
        print("Please wait ...")
        time.sleep(2)
        return

    if not data[slot[0]][slot]["status"]:
        user_id = input("Enter Id: ")
        val = input(f"Are you sure you want to release Slot {slot}? (y/n): ").lower()

        if user_id != data[slot[0]][slot]["user_id"]:
            print("Invalid Id!")
        elif val == "y":
            data[slot[0]][slot]["status"] = True
            data[slot[0]][slot]["user_id"] = None
            data[slot[0]][slot]["last_updated"] = datetime.now().isoformat()
            save_data(data)
            print(f"Slot {slot} successfully released!")
        else:
            print(f"Slot {slot} releasing cancelled!")
    else:
        print(f"Slot {slot} is already available.")

    print("Please wait ...")
    time.sleep(2)
