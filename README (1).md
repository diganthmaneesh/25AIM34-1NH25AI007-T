# 8-Bit Binary Arithmetic and Logical Shift Operations in Python

## Project Overview

This project demonstrates signed binary arithmetic using the **8-bit 2's complement representation** and logical shift operations on 8-bit binary numbers. Python programs are used to perform the operations, display the intermediate steps, and verify the results through manual calculations.

The project contains two Python programs:

1. `signed_binary_arithmetic.py` — performs signed addition using 8-bit 2's complement representation and checks for arithmetic overflow.
2. `logical_shift_operations.py` — performs logical left and right shifts and displays each step while maintaining an 8-bit result.

## Objectives

- Represent positive and negative integers using 8-bit 2's complement.
- Perform binary addition and display the result in binary and decimal formats.
- Identify whether signed arithmetic overflow occurs.
- Perform logical left and right shifts on 8-bit binary numbers.
- Display each shift operation step by step.
- Verify the program results using manual binary calculations.

## Requirements

- Python 3.x
- Any Python editor or IDE, such as IDLE, VS Code, or PyCharm

No external libraries are required.

---

## Program 1: Signed Binary Arithmetic Using 8-Bit 2's Complement

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

## Repository Structure

```text
.
├── README.md
├── signed_binary_arithmetic.py
└── logical_shift_operations.py
```

## Author

Created as a Python programming exercise on 8-bit binary arithmetic and logical shift operations.
