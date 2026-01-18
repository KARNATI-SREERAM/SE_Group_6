# smart_parking.py

# Sample parking lot data
parking_lot = {"A1": False, "A2": True, "B1": True, "B2": False}
# True = Available, False = Occupied


# Function to display parking status
def display_parking_status():
    print("\nParking Lot Status:")
    for slot, status in parking_lot.items():
        print(f"Slot {slot}: {'Available' if status else 'Occupied'}")


# Function to validate slot input
def validate_slot(slot):
    return slot in parking_lot


# Function to book a slot
def book_parking_slot(slot):
    if not validate_slot(slot):
        print(f"Error: Slot '{slot}' does not exist.")
        return
    if parking_lot.get(slot):
        parking_lot[slot] = False
        print(f"Slot {slot} successfully booked!")
    else:
        print(f"Slot {slot} is already occupied.")


# Function to release a slot
def release_parking_slot(slot):
    if not validate_slot(slot):
        print(f"Error: Slot '{slot}' does not exist.")
        return
    if not parking_lot.get(slot):
        parking_lot[slot] = True
        print(f"Slot {slot} has been released.")
    else:
        print(f"Slot {slot} is already available.")


# Main program
if __name__ == "__main__":
    print("=== Smart Parking System ===")
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
