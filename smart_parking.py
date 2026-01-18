import os
import time

# Sample parking lot data
parking_lot = {
    "A": {"A1": False, "A2": True, "A3": False},
    "B": {"B1": True, "B2": False, "B3": True},
}  # True = Available, False = Occupied


# Function to calculate the occupied, available and total slots
def info(data):
    total, available, occupied = 0, 0, 0
    for row in data.values():
        total += len(row)
        available += sum(row.values())
    occupied = total - available
    return (total, available, occupied)


# Function to display parking status
def display_parking_status():
    os.system("cls" if os.name == "nt" else "clear")
    green = "🟢"
    red = "🔴"
    total, available, occupied = info(parking_lot)
    print("===========================================")
    print("        SMART PARKING SYSTEM - v1.0        ")
    print("===========================================")
    print(f"\nParking Lot Status ({green} = Available | {red} = Occupied):\n")
    for row_number, row in parking_lot.items():
        temp = ""
        for slot, status in row.items():
            temp += f"[{slot}: {green if status else red}] "
        print(f"Row {row_number}: {temp}")
    print(f"\nTotal Slots: {total} | Available: {available} | Occupied: {occupied}")


# Function to validate slot input
def validate_slot(slot):
    return slot[0] in parking_lot and slot in parking_lot[slot[0]]


# Function to book a slot
def book_parking_slot(slot):
    if not validate_slot(slot):
        print(f"Error: Slot '{slot}' does not exist.")
        print("Please wait ...")
        time.sleep(2)
        return
    if parking_lot[slot[0]].get(slot):
        val = input(f"Are you sure you want to book Slot {slot}? (y/n): ").lower()
        if val == "y":
            parking_lot[slot[0]][slot] = False
            print(f"Slot {slot} successfully booked!")
        else:
            print(f"Slot {slot} booking cancelled!")
    else:
        print(f"Slot {slot} is already occupied.")
    print("Please wait ...")
    time.sleep(2)


# Function to release a slot
def release_parking_slot(slot):
    if not validate_slot(slot):
        print(f"Error: Slot '{slot}' does not exist.")
        print("Please wait ...")
        time.sleep(2)
        return
    if not parking_lot[slot[0]].get(slot):
        val = input(f"Are you sure you want to release Slot {slot}? (y/n): ").lower()
        if val == "y":
            parking_lot[slot[0]][slot] = True
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
        display_parking_status()
        action = input("\nEnter 'book', 'release', or 'exit':").strip().lower()
        if action == "exit":
            os.system("cls" if os.name == "nt" else "clear")
            break
        elif action in ["book", "release"]:
            slot = input("Enter slot: ").strip()
            if action == "book":
                book_parking_slot(slot)
            elif action == "release":
                release_parking_slot(slot)
        else:
            print("Invalid action. Please enter 'book', 'release', or 'exit'.")
            print("Please wait ...")
            time.sleep(2)
