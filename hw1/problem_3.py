def special_generator(n):
    for i in range(1, n + 1):
        if i % 12 == 0:
            yield "QuadHex"
        elif i % 4 == 0:
            yield "Quad"
        elif i % 6 == 0:
            yield "Hex"
        else:
            yield i


# Do not change or remove the code below this point
def main():
    gen = special_generator(15)
    print(list(gen))  # Expected Output: [1, 2, 3, 'Quad', 5, 'Hex', 7, 'Quad', 9, 10, 11, 'QuadHex', 13, 14, 15]


if __name__ == "__main__":
    main()
