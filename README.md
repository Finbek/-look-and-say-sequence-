## Look-and-Say Sequence

The Look-and-Say sequence is a fascinating integer sequence where each term is derived from the previous one by counting the frequency of consecutive digits. To obtain the next term, we state these frequencies and digits as a string. The sequence starts with "1" and continues as follows: "11", "21", "1211", "111221", "312211", and so on.

### Algorithm

The `lookAndSay` function generates the Look-and-Say sequence up to the nth term and returns the middle two digits of the nth term. The function takes an integer `n` as input, where `n` represents the index of the term to generate in the Look-and-Say sequence.

1. Start with the initial term "1" as `Seq`.
2. Iterate `n-1` times to generate the next terms in the sequence:
   - Initialize `freq` to 1, `numb` to the first digit in `Seq`, and an empty string `ans`.
   - Loop through each digit in `Seq`, starting from the second digit.
   - If the current digit is different from the previous one, append `freq` and `numb` to `ans`, reset `freq` to 1, and update `numb` to the current digit.
   - Otherwise, increment `freq` by 1.
   - After the loop, append the final `freq` and `numb` to `ans`.
   - Update `Seq` with the generated term (`ans`).
3. Calculate the middle position of the final term, and return the middle two digits.

### Speed (Time Complexity)

The time complexity of the `lookAndSay` function mainly depends on the input value `n`. Generating the Look-and-Say sequence requires iterating `n-1` times through the input sequence to produce the desired term. The time complexity can be expressed as O(n \* m), where `m` is the length of the sequence at each iteration. In most practical cases, the sequence grows exponentially, so the overall time complexity can be approximated as O(n \_ 2^n).

### Memory Usage

The space complexity of the `lookAndSay` function is O(m), where `m` represents the length of the sequence at each iteration. In this implementation, we use string variables to store the sequences. Since the sequence length grows exponentially with each iteration, the memory usage can increase significantly for larger values of `n`.

### How to Use

To use the `lookAndSay` function, you need to have Python installed on your system. If you don't have Python installed, follow these steps:

1. Visit the official Python website: [python.org](https://www.python.org/).
2. Download the latest version of Python suitable for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the installation instructions.

Once you have Python installed, you can use the `lookAndSay` function by providing an integer `n` as input, where `n` is the index of the desired term in the Look-and-Say sequence. The function will return the middle two digits of the nth term as a string.

To use the `lookAndSay` function, simply provide an integer `n` as input, where `n` is the index of the desired term in the Look-and-Say sequence. The function will return the middle two digits of the nth term as a string.

Unittest provided to check the correctness of the algorithm

Example usage:

```python
print(lookAndSay(5))  # Output: "12"
print(lookAndSay(7))  # Output: "12"
```

To run the tests, you can use `python LookAndSay.py`
