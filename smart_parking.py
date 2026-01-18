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
    green = "🟢"
    red = "🔴"
    total, available, occupied = info(parking_lot)
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
        return
    if parking_lot[slot[0]].get(slot):
        parking_lot[slot[0]][slot] = False
        print(f"Slot {slot} successfully booked!")
    else:
        print(f"Slot {slot} is already occupied.")


# Function to release a slot
def release_parking_slot(slot):
    if not validate_slot(slot):
        print(f"Error: Slot '{slot}' does not exist.")
        return
    if not parking_lot[slot[0]].get(slot):
        parking_lot[slot[0]][slot] = True
        print(f"Slot {slot} has been released.")
    else:
        print(f"Slot {slot} is already available.")


# Main program
if __name__ == "__main__":
    print("===========================================")
    print("        SMART PARKING SYSTEM - v1.0        ")
    print("===========================================")
    while True:
        display_parking_status()
        action = input("\nEnter 'book', 'release', or 'exit':").strip().lower()
        if action == "exit":
            break
        elif action in ["book", "release"]:
            slot = input("Enter slot: ").strip()
            if action == "book":
                book_parking_slot(slot)
            elif action == "release":
                release_parking_slot(slot)
            else:
                print("Invalid action. Please enter 'book', 'release', or 'exit'.")
