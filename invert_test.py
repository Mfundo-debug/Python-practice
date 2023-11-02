import json
import os
import pytest
import sys
from invert import main

@pytest.fixture
def input_file(tmp_path):
    file_path = tmp_path / "input.json"
    data = {"key1": "value1", "key2": "value2", "key3": "value1"}
    with open(file_path, "w") as f:
        json.dump(data, f)
    return file_path

@pytest.fixture
def output_file(tmp_path):
    return tmp_path / "output.json"

@pytest.fixture
def inverted_output_file(tmp_path):
    return tmp_path / "inverted_output.txt"

def test_main(input_file, output_file, inverted_output_file):
    sys.argv = ["./invert.py", str(input_file), str(output_file), str(inverted_output_file)]
    main()
    with open(output_file, "r") as f:
        output_data = json.load(f)
    assert output_data == {"value1": ["key1", "key3"], "value2": ["key2"]}
    with open(inverted_output_file, "r") as f:
        inverted_output_data = f.read()
    assert inverted_output_data == "value1: ['key1', 'key3']\nvalue2: ['key2']\n"