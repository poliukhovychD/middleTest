import os
import pytest
from main import write_to_file

@pytest.mark.parametrize("input_string", [
    "This is a test string to write to file.",
    "Another string for testing.",
    "1234",
    "",
])
def test_write_to_file(input_string):
    write_to_file(input_string)
    assert os.path.exists('filtered.txt')

    with open('filtered.txt', 'r') as f:
        contents = f.read()
    assert contents == input_string
