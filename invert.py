"""
Write a program to read dictionary items from a file and then write the inverted dictionary to a file. Ensure the program includes the following components: 

1.The input file for your original dictionary (with at least six items). 

2. The Python program you used to read from a file, invert the dictionary, and write to a different file. (You need to create a dictionary file and invert it into another file). 


3. The output file for your inverted dictionary. 

4. Provide a technical explanation for the code and its output in a minimum of 200 words
"""
import json
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./invert.py <input file> <output file> <inverted output file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    inverted_output_file = sys.argv[3]
    with open(input_file, 'r') as f:
        data = json.load(f)
    inverted = {}
    for key, value in data.items():
        inverted.setdefault(value, []).append(key)
    with open(output_file, 'w') as f:
        json.dump(inverted, f)
    with open(inverted_output_file, 'w') as f:
        for key, value in inverted.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()

"""
Explanation:
This Python script reads a JSON file, inverts its key-value pairs, and writes the inverted dictionary back to two output files. Here's a step-by-step explanation:

1. The script expects three command-line arguments: the input file, the output file for the inverted JSON, and another output file for the inverted JSON in a different format. If the number of arguments is not correct, it prints a usage message and exits.

```python
if len(sys.argv) != 4:
    print("Usage: ./invert.py <input file> <output file> <inverted output file>")
    sys.exit(1)
```

2. It reads the input file, which should be a JSON file, and loads it into a Python dictionary.

```python
with open(input_file, 'r') as f:
    data = json.load(f)
```

3. It creates a new dictionary, `inverted`, where each value in the original dictionary becomes a key, and the corresponding key becomes a value. If the same value appears multiple times in the original dictionary, all corresponding keys are collected into a list.

```python
inverted = {}
for key, value in data.items():
    inverted.setdefault(value, []).append(key)
```

4. It writes the `inverted` dictionary to the output file in JSON format.

```python
with open(output_file, 'w') as f:
    json.dump(inverted, f)
```

5. It also writes the `inverted` dictionary to the second output file, but in a different format: each key-value pair is written as a line of text, with the key and value separated by a colon.

```python
with open(inverted_output_file, 'w') as f:
    for key, value in inverted.items():
        f.write(f"{key}: {value}\n")
```


"""
