# **Integrate forensics by modifying 5 Python methods of choice in fuzz.py**
The `fuzz.py` script automatically fuzzes 5 Python methods to identify any bugs, crashes, or unexpected behavior.

---

## **Purpose of the Code**
The code performs fuzz testing on five Python methods or functionalities:

1. **String joining (`join`).**
2. **List element popping (`pop`).**
3. **Dictionary updating (`update`).**
4. **List extension (`extend`).**
5. **Floating-point number conversion (`float`).**

The program logs each test's details (timestamp, test ID, method name, inputs, output, or exceptions) into `fuzz_report.log` for analysis.

---

## **Methods Being Fuzzed**

### **fuzz_join**
- **Tests:** `str.join()` with random lists and separators.
- **Scenarios Tested:**
  - Lists with mixed elements (e.g., strings, integers, or `None`).
  - Separators including `None`, space, and special characters.
- **Logs:** Both successful outputs and exceptions (e.g., `TypeError` for invalid list elements).

---

### **fuzz_pop**
- **Tests:** `list.pop()` with random lists and indices.
- **Scenarios Tested:**
  - Randomized indices, including out-of-range values and `None`.
  - Lists with varying sizes, including empty lists.
- **Logs:** Outputs or exceptions (e.g., `IndexError` for invalid indices).

---

### **fuzz_update**
- **Tests:** `dict.update()` with random dictionaries and updates.
- **Scenarios Tested:**
  - Updating with valid dictionaries, `None`, or invalid iterable structures.
  - Mixing incompatible types.
- **Logs:** Successful updates or exceptions (e.g., `TypeError` for invalid updates).

---

### **fuzz_extend**
- **Tests:** `list.extend()` with random lists and extensions.
- **Scenarios Tested:**
  - Extending with valid iterables (e.g., lists) and invalid values (e.g., strings, `None`).
  - Lists with mixed data types.
- **Logs:** Outputs or exceptions (e.g., `TypeError` when attempting to extend with non-iterable objects).

---

### **fuzz_float**
- **Tests:** `float()` with random strings and numeric inputs.
- **Scenarios Tested:**
  - Valid floating-point strings (e.g., `"123.456"`).
  - Invalid strings, `None`, and random non-numeric values.
- **Logs:** Outputs or exceptions (e.g., `ValueError` for invalid float conversion).

---

## **Results**
- Any bugs or unexpected behavior discovered during fuzz testing will be logged into the `fuzz_forensics.log` file.
- Each log entry includes details like the method name, inputs, outputs, and exceptions encountered for easier debugging and analysis.

<img width="730" alt="for" src="https://github.com/user-attachments/assets/4fe8c021-1902-4e63-8795-0cf3b26712cc">
