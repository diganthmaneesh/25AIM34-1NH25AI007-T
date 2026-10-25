def to_binary(n):
    return format(n & 0xFF, '08b')


def signed_value(n):
    if n >= 128:
        return n - 256
    return n


def add_binary(a, b):
    bin_a = to_binary(a)
    bin_b = to_binary(b)

    result = (a + b) & 0xFF
    decimal_result = a + b

    print("First operand  :", bin_a)
    print("Second operand :", bin_b)

    print("Binary addition:")
    print(" ", bin_a)
    print("+", bin_b)
    print("----------")
    print(" ", to_binary(result))

    print("Result in binary :", to_binary(result))
    print("Result in decimal:", signed_value(result))

    if decimal_result < -128 or decimal_result > 127:
        print("Arithmetic Overflow: Yes")
    else:
        print("Arithmetic Overflow: No")


print("Case (a): 25 + (+18)")
add_binary(25, 18)

print("\nCase (b): (-25) + (-18)")
add_binary(-25, -18)
