import unittest

MAX_N = 100
MIN_N = 3


def lookAndSay(n: int) -> str:
    """
    Generate the Look-and-Say sequence up to the nth term and return the middle two digits of the nth term.

    Args:
        n (int): The index of the term to generate in the Look-and-Say sequence.

    Returns:
        str: The middle two digits of the nth term in the Look-and-Say sequence.

    Note:
        The Look-and-Say sequence starts with "1" and each subsequent term is obtained by reading
        the previous term and counting the frequency of consecutive digits. The next term is formed
        by stating these frequencies and digits. For example, the sequence begins as follows:
        "1", "11", "21", "1211", "111221", "312211", and so on.
    """
    if MIN_N > n or MAX_N < n:
        return "Values expected to be in range {} - {}".format(MIN_N, MAX_N)

    Seq = "1"
    for i in range(1, n):
        freq = 1
        numb = Seq[0]
        ans = ''
        for k in range(1, len(Seq)):
            if Seq[k - 1] != Seq[k]:
                ans += str(freq) + numb
                freq = 1
                numb = Seq[k]
            else:
                freq += 1
        ans += str(freq) + numb
        Seq = ans

    middle = len(Seq) // 2
    return Seq[middle - 1: middle + 1]


class TestLookAndSaySequence(unittest.TestCase):
    """
    Test cases for the LookAndSay function.
    """

    def test_case_1(self):
        """
        Test for n = 5, the expected output is "12". Provided
        """
        self.assertEqual(lookAndSay(5), "12")

    def test_case_2(self):
        """
        Test for n = 7, the expected output is "12". Provided
        """
        self.assertEqual(lookAndSay(7), "12")

    tests = [
        {"input": 0,
            "output": "Values expected to be in range {} - {}".format(MIN_N, MAX_N)},
        {"input": 4, "output": "21"},
        {"input": 6, "output": "22"},
        {"input": 8, "output": "21"},
        {"input": 9, "output": "11"},
        {"input": 10, "output": "23"},
        {"input": 11, "output": "12"},
        {"input": 12, "output": "11"},
        {"input": 13, "output": "31"},
        {"input": 14, "output": "21"},
        {"input": 15, "output": "21"},
        {"input": 16, "output": "22"},
    ]

    def test_look_and_say_sequence(self):
        """
        Test the LookAndSay function with various test cases.
        """
        for test in self.tests:
            with self.subTest(test=test):
                self.assertEqual(lookAndSay(test["input"]), test["output"])


if __name__ == "__main__":
    unittest.main()
