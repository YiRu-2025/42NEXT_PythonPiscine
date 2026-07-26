import sys

def parse_input(lines: list[str]) -> dict[str: int]:
    inventory = {}
    for pairs in lines:
        try:
            key, val = pairs.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{pairs}'")
            continue
        try:
            value = int(val)
        except ValueError as e:
            print(f"Quantity error for 'key': {e}")
            continue
        if value <= 0:
            print("Quantity error: quantity can't be less than 0")
            continue
        if key not in inventory.keys():
            inventory[key] = value
        else:
            print(f"Redundant item '{key}' - discarding")
            continue
    return inventory
        
def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print(f"No input parameter")
        return

    inventory = parse_input(sys.argv[1:])
    if not inventory:
        print("No valid input for inventory")
        return

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_score = sum(v for v in inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_score}")

    least = list(inventory.items())[0]
    most = list(inventory.items())[0]
    for k, v in inventory.items():
        weight = float(v / total_score * 100)
        if v < least[1]:
            least = (k, v)
        if v > most[1]:
            most = (k, v)
        print(f"Item {k} represents {round(weight, 1)}%")
    print(f"Item most abundant: {most[0]} with quantity {most[1]}")
    print(f"Item least abundant: {least[0]} with quantity {least[1]}")
    inventory.update({'magic_item' : 1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()