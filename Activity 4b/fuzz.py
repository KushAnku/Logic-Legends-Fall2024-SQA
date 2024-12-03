import random
import string
import logging

# Set up logging to report bugs found
logging.basicConfig(filename="fuzz_report.log", level=logging.INFO)

def random_string(length=10):
    """Generate a random string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def fuzz_upper():
    test_string = random_string()
    try:
        result = test_string.upper()
    except Exception as e:
        logging.info(f"Bug in str.upper() with input '{test_string}': {e}")

def fuzz_lower():
    test_string = random_string()
    try:
        result = test_string.lower()
    except Exception as e:
        logging.info(f"Bug in str.lower() with input '{test_string}': {e}")

def fuzz_replace():
    test_string = random_string()
    old = random.choice([random_string(1), "", None])
    new = random.choice([random_string(1), "", None])
    try:
        result = test_string.replace(old, new)
    except Exception as e:
        logging.info(f"Bug in str.replace() with input '{test_string}', old='{old}', new='{new}': {e}")

def fuzz_max():
    test_list = [random.choice([random.randint(-1000, 1000), random_string()]) for _ in range(10)]
    try:
        result = max(test_list)
    except Exception as e:
        logging.info(f"Bug in max() with input '{test_list}': {e}")

def fuzz_min():
    test_list = [random.choice([random.randint(-1000, 1000), random_string()]) for _ in range(10)]
    try:
        result = min(test_list)
    except Exception as e:
        logging.info(f"Bug in min() with input '{test_list}': {e}")

if __name__ == "__main__":
    # Number of fuzz tests per method
    num_tests = 1000

    for _ in range(num_tests):
        fuzz_upper()
        fuzz_lower()
        fuzz_replace()
        fuzz_max()
        fuzz_min()

    print("Fuzz testing completed. Check 'fuzz_report.log' for bug reports.")
