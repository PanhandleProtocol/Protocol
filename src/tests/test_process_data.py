import unittest

def process_data(data):
    """Processes the input data and returns a list of results."""
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    return [x * 2 for x in data]

class TestProcessData(unittest.TestCase):
    """Unit tests for the process_data function."""

    def test_process_data_valid(self):
        """Test with valid input."""
        self.assertEqual(process_data([1, 2, 3]), [2, 4, 6])

    def test_process_data_empty(self):
        """Test with empty input."""
        self.assertEqual(process_data([]), [])

    def test_process_data_invalid(self):
        """Test with invalid input type."""
        with self.assertRaises(ValueError):
            process_data("not a list")

if __name__ == '__main__':
    unittest.main()