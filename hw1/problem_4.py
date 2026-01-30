def flip_bit(num, bit_position):
    return num ^ (1 << bit_position)


# Do not change or remove the code below this point
def main():
    print(flip_bit(8, 1))  # Expected Output: 10
    print(flip_bit(10, 1))  # Expected Output: 8


if __name__ == "__main__":
    main()
