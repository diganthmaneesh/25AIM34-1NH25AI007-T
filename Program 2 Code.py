def logical_left_shift(binary, positions):
    print("Original binary:", binary)

    for i in range(positions):
        binary = binary[1:] + '0'
        print("After left shift", i + 1, ":", binary)

    print("Final result:", binary)


def logical_right_shift(binary, positions):
    print("Original binary:", binary)

    for i in range(positions):
        binary = '0' + binary[:-1]
        print("After right shift", i + 1, ":", binary)

    print("Final result:", binary)


print("Case (a): Logical Left Shift")
logical_left_shift("10110110", 2)

print("\nCase (b): Logical Right Shift")
logical_right_shift("11010100", 2)
