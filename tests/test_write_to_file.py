import os
from main import write_to_file

def test_write_to_file():
    string = "This is a test string to write to file."
    write_to_file(string)
    assert os.path.exists('filtered.txt')

    with open('filtered.txt', 'r') as f:
        contents = f.read()
    assert contents == string
