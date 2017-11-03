from palindrome.palindrome import palindrome


class TestPalindrome:
    """palindrome related tests."""

    def test_single_digit(self):
        """Test if single digit is true."""
        expected = True
        digit = str(1)

        assert expected == palindrome(digit)

    def test_two_digits_true(self):
        """Test if string with two digits is true."""
        expected = True
        digit = str(11)

        assert expected == palindrome(digit)

    def test_two_digits_false(self):
        """Test if string with two digits is false."""
        expected = False
        digit = str(10)

        assert expected == palindrome(digit)
