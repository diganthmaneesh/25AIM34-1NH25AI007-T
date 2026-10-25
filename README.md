# 8-Bit Binary Arithmetic and Logical Shift Operations in Python


## Program 1: Signed Binary Arithmetic Using 8-Bit 2's Complement
<img width="392" height="289" alt="image" src="https://github.com/user-attachments/assets/7b52cc77-d1e7-4d22-82ea-e9664fabc88e" />

### Description

An 8-bit 2's complement number uses the most significant bit as the sign bit:

- `0` indicates a non-negative number.
- `1` indicates a negative number.

The representable signed integer range is **-128 to +127**.

For a negative number, its 2's complement representation is obtained by inverting the bits of its positive binary representation and adding 1.

The program performs these expressions:

- **(a)** `25 + (+18)`
- **(b)** `(-25) + (-18)`

For each expression, the program displays the operands in 8-bit binary, performs the addition, displays the result in binary and decimal, and reports whether overflow occurs.

### Manual Calculation

#### Case (a): 25 + (+18)

Convert both positive integers to 8-bit binary:

```text
25  = 00011001
+18 = 00010010
```

Add the binary numbers:

```text
   00011001
 + 00010010
 -----------
   00101011
```

The binary result `00101011` represents decimal **43**.

**Overflow check:** No overflow occurs because 43 is within the 8-bit signed range of -128 to +127.

#### Case (b): (-25) + (-18)

First, find the 2's complement representation of each negative number.

For -25:

```text
+25       = 00011001
Invert    = 11100110
Add 1     = 11100111
```

Therefore, `-25 = 11100111`.

For -18:

```text
+18       = 00010010
Invert    = 11101101
Add 1     = 11101110
```

Therefore, `-18 = 11101110`.

Add the two 8-bit numbers:

```text
    11100111
  + 11101110
  -----------
  1 11010101
```

Discard the carry beyond the 8-bit result:

```text
11010101
```

The most significant bit is `1`, so the result is negative. Find its magnitude by taking the 2's complement:

```text
11010101
Invert    = 00101010
Add 1     = 00101011 = 43
```

Therefore, `11010101` represents decimal **-43**.

**Overflow check:** No overflow occurs because -43 is within the 8-bit signed range.

### Expected Results

| Expression | Operand 1 | Operand 2 | Result (8-bit binary) | Decimal result | Overflow |
|---|---|---|---|---:|---|
| `25 + (+18)` | `00011001` | `00010010` | `00101011` | 43 | No |
| `(-25) + (-18)` | `11100111` | `11101110` | `11010101` | -43 | No |

### How to Run

Open a terminal in the folder containing the file and run:

```bash
python signed_binary_arithmetic.py
```

The program prints the binary operands, binary addition, final 8-bit result, decimal result, and overflow status.

---

## Program 2: Logical Left and Right Shift Operations


<img width="390" height="164" alt="image" src="https://github.com/user-attachments/assets/ee7323c3-b7ad-444a-a88d-f4129f08d57a" />

### Description

A logical shift moves the bits of a binary number by a specified number of positions. Vacant positions are filled with `0`, and bits shifted beyond the 8-bit boundary are discarded.

The program demonstrates:

- **(a)** Logical left shift of `10110110` by 2 positions.
- **(b)** Logical right shift of `11010100` by 2 positions.

Each intermediate step and the final 8-bit result are displayed.

### Manual Calculation

#### Case (a): Logical Left Shift

Original number:

```text
10110110
```

Shift left by one position. Drop the leftmost bit and insert `0` on the right:

```text
10110110  ->  01101100
```

Shift left by one more position:

```text
01101100  ->  11011000
```

Final result: **`11011000`**

#### Case (b): Logical Right Shift

Original number:

```text
11010100
```

Shift right by one position. Drop the rightmost bit and insert `0` on the left:

```text
11010100  ->  01101010
```

Shift right by one more position:

```text
01101010  ->  00110101
```

Final result: **`00110101`**

### Expected Results

| Operation | Original 8-bit number | After 1 shift | After 2 shifts |
|---|---|---|---|
| Logical left shift | `10110110` | `01101100` | `11011000` |
| Logical right shift | `11010100` | `01101010` | `00110101` |

### How to Run

Run the following command in the terminal:

```bash
python logical_shift_operations.py
```

The program displays the original number, the result after each shift, and the final 8-bit result.

---

## Verification and Conclusion

The program results match the manual calculations:

- `25 + (+18) = 43`, represented by `00101011`. No overflow occurs.
- `(-25) + (-18) = -43`, represented by `11010101`. No overflow occurs.
- Logical left shift of `10110110` by 2 positions produces `11011000`.
- Logical right shift of `11010100` by 2 positions produces `00110101`.

All shift results are displayed using exactly 8 bits. The arithmetic examples also demonstrate how signed values are represented and how overflow is checked against the 8-bit 2's complement range.

