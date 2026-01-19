import os
import time
import json
from datetime import datetime


def save_date(data):
    with open("./data/data.json", "w") as file:
        json.dump(data, file, indent=2)
        file.close()


try:
    with open("./data/data.json", "r") as file:
        data = json.load(file)
        file.close()
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
    save_date(data)


# Function to calculate the occupied, available and total slots
def info(data):
    total, available, occupied = 0, 0, 0
    for row in data.values():
        total += len(row)
        for val in row.values():
            available += val["status"]
    occupied = total - available
    return (total, available, occupied)


# Function to display parking status
def display_parking_status(data):
    os.system("cls" if os.name == "nt" else "clear")
    green = "🟢"
    red = "🔴"
    total, available, occupied = info(data)
    print("===========================================")
    print("        SMART PARKING SYSTEM - v1.0        ")
    print("===========================================")
    print(f"\nParking Lot Status ({green} = Available | {red} = Occupied):\n")
    for row_number, row in data.items():
        temp = ""
        for slot, details in row.items():
            temp += f"[{slot}: {green if details["status"] else red}] "
        print(f"Row {row_number}: {temp}")
    print(f"\nTotal Slots: {total} | Available: {available} | Occupied: {occupied}")


# Function to validate slot input
def validate_slot(data, slot):
    return slot[0] in data and slot in data[slot[0]]


# Function to book a slot
def book_parking_slot(data, slot):
    if not validate_slot(data, slot):
        print(f"Error: Slot '{slot}' does not exist.")
        print("Please wait ...")
        time.sleep(2)
        return
    if data[slot[0]].get(slot)["status"]:
        id = input("Enter Id: ")
        val = input(f"Are you sure you want to book Slot {slot}? (y/n): ").lower()
        if val == "y":
            data[slot[0]][slot]["status"] = False
            data[slot[0]][slot]["user_id"] = id
            data[slot[0]][slot]["last_updated"] = datetime.now().isoformat()
            save_date(data)
            print(f"Slot {slot} successfully booked!")
        else:
            print(f"Slot {slot} booking cancelled!")
    else:
        print(f"Slot {slot} is already occupied.")
    print("Please wait ...")
    time.sleep(2)


# Function to release a slot
def release_parking_slot(data, slot):
    if not validate_slot(data, slot):
        print(f"Error: Slot '{slot}' does not exist.")
        print("Please wait ...")
        time.sleep(2)
        return
    if not data[slot[0]].get(slot)["status"]:
        id = input("Enter Id: ")
        val = input(f"Are you sure you want to release Slot {slot}? (y/n): ").lower()
        if id != data[slot[0]][slot]["user_id"]:
            print("Invaild Id!")
        elif val == "y":
            data[slot[0]][slot]["status"] = True
            data[slot[0]][slot]["user_id"] = None
            data[slot[0]][slot]["last_updated"] = datetime.now().isoformat()
            save_date(data)
            print(f"Slot {slot} successfully released!")
        else:
            print(f"Slot {slot} releasing cancelled!")
    else:
        print(f"Slot {slot} is already available.")
    print("Please wait ...")
    time.sleep(2)


# Main program
if __name__ == "__main__":
    while True:
        display_parking_status(data)
        action = input("\nEnter 'book', 'release', or 'exit': ").strip().lower()
        if action == "exit":
            os.system("cls" if os.name == "nt" else "clear")
            break
        elif action in ["book", "release"]:
            slot = input("Enter slot: ").strip()
            if action == "book":
                book_parking_slot(data, slot)
            elif action == "release":
                release_parking_slot(data, slot)
        else:
            print("Invalid action. Please enter 'book', 'release', or 'exit'.")
            print("Please wait ...")
            time.sleep(2)
