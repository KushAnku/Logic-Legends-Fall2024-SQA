import random
import string
import logging

# Set up logging to report bugs found
logging.basicConfig(filename="fuzz_report.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def random_string(length=10):
    """Generate a random string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def log_forensics(method_name, inputs, output=None, error=None):
    """Log detailed forensic information for debugging."""
    if error:
        logging.error(f"Forensics - Method: {method_name}, Inputs: {inputs}, Error: {error}")
    else:
        logging.info(f"Forensics - Method: {method_name}, Inputs: {inputs}, Output: {output}")

def fuzz_join():
    test_list = [random.choice([random_string(5), None, 123]) for _ in range(5)]
    separator = random.choice(["-", " ", None])
    try:
        result = separator.join(test_list)
        log_forensics("str.join", {"list": test_list, "separator": separator}, output=result)
    except Exception as e:
        log_forensics("str.join", {"list": test_list, "separator": separator}, error=str(e))

def fuzz_pop():
    test_list = [random.randint(0, 100) for _ in range(random.randint(0, 10))]
    index = random.choice([random.randint(-10, 10), None])
    try:
        result = test_list.pop(index)
        log_forensics("list.pop", {"list": test_list, "index": index}, output=result)
    except Exception as e:
        log_forensics("list.pop", {"list": test_list, "index": index}, error=str(e))

def fuzz_update():
    test_dict = {random_string(5): random.randint(0, 100) for _ in range(5)}
    updates = random.choice([{random_string(5): random.randint(0, 100)}, None, [("key", "value")]])
    try:
        test_dict.update(updates)
        log_forensics("dict.update", {"dict": test_dict, "updates": updates}, output=test_dict)
    except Exception as e:
        log_forensics("dict.update", {"dict": test_dict, "updates": updates}, error=str(e))

def fuzz_extend():
    test_list = [random.randint(0, 100) for _ in range(5)]
    extension = random.choice([[random.randint(0, 100) for _ in range(5)], None, "string"])
    try:
        test_list.extend(extension)
        log_forensics("list.extend", {"list": test_list, "extension": extension}, output=test_list)
    except Exception as e:
        log_forensics("list.extend", {"list": test_list, "extension": extension}, error=str(e))

def fuzz_float():
    test_string = random.choice([random_string(), str(random.uniform(-1000, 1000)), None, "123.456"])
    try:
        result = float(test_string)
        log_forensics("float", {"input": test_string}, output=result)
    except Exception as e:
        log_forensics("float", {"input": test_string}, error=str(e))

if __name__ == "__main__":
    # Number of fuzz tests per method
    num_tests = 1000

    for _ in range(num_tests):
        fuzz_join()
        fuzz_pop()
        fuzz_update()
        fuzz_extend()
        fuzz_float()

    print("Fuzz testing with forensics completed. Check 'fuzz_report.log' for detailed logs.")
