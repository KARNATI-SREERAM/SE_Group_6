def info(data):
    total, available, occupied = 0, 0, 0

    for row in data.values():
        total += len(row)
        for val in row.values():
            available += val["status"]

    occupied = total - available
    return total, available, occupied


def validate_slot(data, slot):
    return len(slot) >= 2 and slot[0] in data and slot in data[slot[0]]
