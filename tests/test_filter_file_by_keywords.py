import os
from main import filter_file_by_keywords

def test_filter_file_by_keywords(tmp_path):
    # Create a temporary file for testing
    input_filename = os.path.join(tmp_path, "input.txt")
    with open(input_filename, "w") as f:
        f.write("hello world\n")
        f.write("this is a test\n")
        f.write("lol this is funny\n")
        f.write("display this message\n")

    # Test with one keyword
    keywords = ["test"]
    filter_file_by_keywords(input_filename, keywords)
    with open("filtered.txt", "r") as f:
        assert f.read() == "this is a test\n"
    os.remove("filtered.txt")

    # Test with multiple keywords
    keywords = ["lol", "display"]
    filter_file_by_keywords(input_filename, keywords)
    with open("filtered.txt", "r") as f:
        assert f.read() == "lol this is funny\ndisplay this message\n"
    os.remove("filtered.txt")

    # Test with no keywords found
    keywords = ["not_found"]
    filter_file_by_keywords(input_filename, keywords)
    assert not os.path.exists("filtered.txt")
