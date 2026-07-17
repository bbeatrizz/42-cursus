import sys


def check_inventory(args: list[str]) -> dict[str, int]:
    inventory = {}

    for arg in args:
        try:
            item, qty = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item in inventory:
            print(f"Redundant item {item} - discarding")
            continue

        try:
            inventory[item] = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

    return inventory


def statistic(inventory: dict[str, int]) -> None:
    total_item: int = len(inventory)
    total_qty: int = sum(inventory.values())

    print(f"Total quantity of the {total_item} items: {total_qty}")

    for item, qty in inventory.items():
        if total_qty > 0:
            item_p: float = qty / total_qty * 100
        else:
            item_p = 0
        print(f"Item {item} represents {round(item_p, 1)}%")
    if total_item > 0:
        first_item: bool = True
        max_name: str = ""
        max_qty: int = -1
        min_name: str = ""
        min_qty: int = -1
        for name, qty in inventory.items():
            if first_item:
                max_name = name
                max_qty = qty
                min_name = name
                min_qty = qty
                first_item = False
            else:
                if max_qty < qty:
                    max_qty = qty
                    max_name = name
                if min_qty > qty:
                    min_qty = qty
                    min_name = name
    print(
        f"Item most abundant: {max_name} with"
        f" quantity {max_qty}"
        )
    print(
        f"Item least abundant: {min_name} with"
        f" quantity {min_qty}"
        )


def ft_invetory_system() -> None:
    if len(sys.argv) > 1:
        print("=== Inventory System Analysis ===")

        inventory = check_inventory(sys.argv[1:])

        print(f"Got inventory: {inventory}")
        print(f"Item lists: {list(inventory.keys())}")
        statistic(inventory)

        inventory.update({"magic_item": 1})

        print(f"Updated inventory: {inventory}")
    else:
        print("Usage: python3 ft_inventory_system.py "
              "<item_name>:<quantity>...")


if __name__ == "__main__":
    ft_invetory_system()
