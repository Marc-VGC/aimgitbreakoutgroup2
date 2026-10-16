def swap_values(a, b):
    """
    Swap two values and return them.
    """
    return b, a


def main():
    print("=== Swap Lab ===")
    # Get inputs from the user
    x = input("Enter first value: ")
    y = input("Enter second value: ")

    print(f"\nBefore swap: x = {x}, y = {y}")
    x, y = swap_values(x, y)
    print(f"After swap:  x = {x}, y = {y}")


if __name__ == "__main__":
    main()
