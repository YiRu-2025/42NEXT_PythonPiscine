import math

def get_player_pos() -> tuple[float, float, float]:
    while True: # for repeatedly asking for input, ends when reaches a return
        coord = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coord.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue
        pos = []
        for part in parts: # detecting whether each param was successfully converted
            try:
                pos.append(float(part.strip())) # skip the space before and after, convert and store the param
            except ValueError as err:
                print(f"Error on parameter '{part}': {err}")
                break
        else:
            return tuple(pos)

def distance(p1: tuple[float, float, float], p2: tuple[float, float, float]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def main() -> None:
    print("=== Game Coordinate System ===")
    
    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    pos0 = [0,0,0]
    print(f"Distance to center: {round(distance(pos1, pos0), 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: {round(distance(pos2, pos1), 4)}")


if __name__ == "__main__":
    main()