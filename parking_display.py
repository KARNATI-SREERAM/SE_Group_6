import os
from parking_utils import info

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
            temp += f"[{slot}: {green if details['status'] else red}] "
        print(f"Row {row_number}: {temp}")

    print(f"\nTotal Slots: {total} | Available: {available} | Occupied: {occupied}")
