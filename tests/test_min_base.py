from palindrome.palindrome import min_base


class TestMinBase:
    """minimum base related tests."""

    def test_single_digit_min_base(self):
        """Test single digit min base."""
        expected = 2
        digit = 1

        assert expected == min_base(digit)

    def test_digit_12_min_base(self):
        """Test digit 12 min base."""
        expected = 5
        digit = 12

        assert expected == min_base(digit)

    def test_digit_14_min_base(self):
        """Test digit 14 min base."""
        expected = 6
        digit = 14

        assert expected == min_base(digit)
