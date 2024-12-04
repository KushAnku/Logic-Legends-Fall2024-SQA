# Activity 4b :Fuzzing with fuzz.py
The `fuzz.py` script automatically fuzzes 5 Python methods to identify any bugs, crashes, or unexpected behavior.

## How it Works
- Fuzzes 5 Python methods by generating random inputs and testing edge cases.
- Reports any discovered bugs or unexpected behavior during the fuzzing process.
- Logs the results of the fuzz testing, including any issues found, into a `fuzz_report.log` file for review.

### Methods Being Fuzzed

#### str.upper()
- Converts all characters in a string to uppercase.
- Fuzzing tests include:
  - Empty strings.
  - Special characters.
  - Long strings with a mix of uppercase, lowercase, and non-alphanumeric characters.

#### str.lower()
- Converts all characters in a string to lowercase.
- Fuzzing tests include:
  - Strings with a mix of uppercase and lowercase letters.
  - Strings with special characters and numbers.
  - Edge cases like empty strings.

#### str.replace()
- Replaces substrings in a string.
- Fuzzing tests include:
  - Replacing substrings that don’t exist.
  - Replacing with `None` or empty strings.
  - Using unusual replacement patterns or very long substrings.

#### max()
- Returns the largest element from a list.
- Fuzzing tests include:
  - Lists with mixed data types (e.g., strings and integers).
  - Lists with only one element.
  - Lists with invalid elements or empty lists.

#### min()
- Returns the smallest element from a list.
- Fuzzing tests include:
  - Lists with mixed data types.
  - Random lists with negative and positive integers.
  - Edge cases like empty lists or invalid input elements.

### Results
The fuzzing results, including any identified bugs, crashes, or unexpected behavior, are saved in the `fuzz_report.log` file.
This log can be reviewed to identify and address potential vulnerabilities or inconsistencies in the methods.

<img width="680" alt="fuzzz" src="https://github.com/user-attachments/assets/ceb72ddb-6a5c-4223-a7b6-61e7de60e1c0">

<img width="824" alt="fuzz1" src="https://github.com/user-attachments/assets/504fd760-6463-4589-b551-fe346972c590">


