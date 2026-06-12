def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        info = f"{quantity} packets available"
    elif unit == "grams":
        info = f"{quantity} grams total"
    elif unit == "area":
        info = f"covers {quantity} square meters"
    else:
        info = "Unknown unit type"
    print(f"{seed_type} seeds: {info}")
