import os
import time

from storage import load_data
from parking_display import display_parking_status
from parking_actions import book_parking_slot, release_parking_slot


def main():
    data = load_data()

    while True:
        display_parking_status(data)

        action = input("\nEnter 'book', 'release', or 'exit': ").strip().lower()

        if action == "exit":
            os.system("cls" if os.name == "nt" else "clear")
            break

        elif action in ["book", "release"]:
            slot = input("Enter slot: ").strip().upper()

            if action == "book":
                book_parking_slot(data, slot)
            else:
                release_parking_slot(data, slot)

        else:
            print("Invalid action. Please enter 'book', 'release', or 'exit'.")
            print("Please wait ...")
            time.sleep(2)


if __name__ == "__main__":
    main()
