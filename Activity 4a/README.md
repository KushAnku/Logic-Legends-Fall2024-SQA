# Activity 4a: Pre-Commit Hook for Security Analysis

## Overview
This activity involves the creation of a **Git pre-commit hook** that automatically scans Python files for potential security weaknesses using the `Bandit` static analysis tool. The findings are saved in a **CSV report** (`security_findings.csv`), and commits are blocked if any issues of high or medium severity are detected.

Additionally, the `frequency.py` file was intentionally modified to include insecure code to test the effectiveness of the pre-commit hook.

---

## Implementation Details

### Pre-Commit Hook
The pre-commit hook script performs the following tasks:
- **Identify staged Python files** during a commit process.
- **Run `Bandit`** to scan these files for security vulnerabilities.
- **Generate a CSV report** (`security_findings.csv`) with details such as:
  - File name
  - Severity level
  - Line number
  - Issue description
- **Block the commit** if high or medium severity issues are found.
- **Perform additional checks** for non-ASCII file names and whitespace errors.

### Edited File: `frequency.py`
The `frequency.py` file was modified to include intentionally insecure code for testing the hook:
```python
def insecure_exec():
    # Example of user input that could lead to security issues
    user_input = "print('Hello, insecure world!')"  # Simulates unsafe dynamic execution
    exec(user_input)  # Bandit will flag this for using exec()

# Call the insecure function
insecure_exec()


### Terminal Output

When attempting to commit changes with insecure code, the pre-commit hook scans the staged Python files for potential security risks. If high or medium severity issues are detected, the commit is blocked, and a summary is displayed in the terminal. Below is an example of the output:

![image](https://github.com/user-attachments/assets/2e7fd59d-c747-4bed-bfc1-7352c0dcba17)


#### In this screenshot:
- The hook scans the Python files in the project.
- It identifies multiple files with high or medium severity issues, including `frequency.py`.
- The commit is blocked, and the user is instructed to resolve the issues before proceeding.
- The full scan report is saved in `security_findings.csv`.
