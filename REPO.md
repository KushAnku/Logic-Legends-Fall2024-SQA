# **Project Activity Report**

## **Part A - [Ankush Singh ]**

### **1. Activities Done**
   - **Research and Planning**: Conducted background research on secure coding practices and explored Git hooks for automating security checks.
   - **Implementation of Pre-Commit Hook**: Developed a `pre-commit` Git hook to automate security scans using the `bandit` tool, ensuring Python files are analyzed for vulnerabilities before commits.
   - **Testing the Hook**: Validated the pre-commit hook on multiple Python scripts, adjusting configurations to minimize false positives and improve accuracy.
   - **Created Documentation**: Developed a README file detailing the project setup, workflow instructions, and usage examples to assist team members in understanding the project.

### **2. Lessons Learned**
   - **Value of Automation**: Leveraging automation tools like pre-commit hooks improved efficiency and reduced potential security risks in the codebase.
   - **Challenges with False Positives**: Encountered false positives during security scans, highlighting the importance of balancing automation with manual review processes.

---

## **Part B - [Aparana Pant]**

### **1. Activities Done**
   - **Created `fuzz.py` Script**: Implemented a Python script (`fuzz.py`) to automatically fuzz 5 Python methods:
     - `str.upper()`
     - `str.lower()`
     - `str.replace()`
     - `max()`
     - `min()`
   - **Test Coverage**: Chose methods that covered string manipulations, numerical comparisons, and edge case handling to ensure robust testing.
   - **Logging Results**: Configured the script to log all test details, including inputs, outputs, and exceptions, into `fuzz_report.log`.

### **2. Lessons Learned**
   - **Bug Discovery and Documentation**: Successfully identified edge cases and bugs, particularly with mixed data types and invalid inputs.
   - **Handling Complex Test Scenarios**: Observed that certain bugs were inconsistent and required deeper analysis to reproduce.
   - **Scalability**: Realized the potential of extending fuzz testing to additional methods or modules for broader coverage.

---

## **Part C - [Parishruthi Ganesh]**

### **1. Activities Done**
   - **Enhanced Fuzz Testing for Forensics**: Modified `fuzz.py` to test five new Python functionalities:
     - String joining (`str.join()`)
     - List element popping (`list.pop()`)
     - Dictionary updating (`dict.update()`)
     - List extension (`list.extend()`)
     - Floating-point number conversion (`float()`)
   - **Forensics Integration**: Enhanced the script to log forensic-level details, such as timestamps, method names, inputs, outputs, and exceptions, into `fuzz_forensics.log`.
   - **Bug Tracking**: Consolidated identified bugs into `fuzz_report.log` for analysis and debugging.

### **2. Lessons Learned**
   - **Importance of Edge Case Testing**: Realized that testing edge cases (e.g., `None`, empty inputs, invalid data types) is critical for uncovering hidden issues.
   - **Detailed Logs for Debugging**: Comprehensive forensic logs made it easier to identify, reproduce, and address bugs.
   - **Advanced Logging Practices**: Implemented structured logging for better clarity and analysis.

---

## **Part D - [Disharee Bhowmick]**

### **1. Activities Done**
   - **Integrated Continuous Integration (CI)**: Configured a GitHub Actions workflow to automate fuzz testing and code quality analysis:
     - **Fuzz Testing**: Integrated the `fuzz.py` script into the CI pipeline to automatically test Python methods and log results upon every push or pull request.
     - **Codacy Analysis CLI**: Configured Codacy Analysis CLI in the workflow to provide automated feedback on code quality.
   - **Created Workflow File**: Developed `.github/workflows/CLI.yml` to define the CI pipeline, including steps for:
     - Checking out the repository.
     - Setting up the Python environment.
     - Running `fuzz.py` for automated testing.
     - Running Codacy Analysis CLI for code quality checks.

### **2. Lessons Learned**
   - **Benefits of Continuous Integration**: Automating code testing and analysis ensures consistency and reduces manual effort.
   - **Tool Configuration**: Gained practical experience in setting up GitHub Actions workflows and using Codacy for automated code quality assessments.
   - **Real-Time Feedback**: The CI workflow provided immediate insights into code quality and testing results, streamlining the development process.

---

