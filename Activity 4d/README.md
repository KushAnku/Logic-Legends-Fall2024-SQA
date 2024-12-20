# **Integrate Continuous Integration with GitHub Actions**

## **Objective**
Automate code quality checks and fuzz testing using GitHub Actions and Codacy Analysis CLI to ensure consistent code analysis and maintain high standards in the codebase.

---

## **Implementation**

### **GitHub Actions Workflow**
The CI process is implemented through a GitHub Actions workflow file named `CLI.yml`, which performs the following steps:

 **Checkout Code:**
   - Pulls the latest code from the repository to the GitHub Actions runner environment.

 **Execute Fuzz Testing (`fuzz.py`):**
   - Runs the fuzz testing script located in `Activity 4d/fuzz.py` to identify bugs and log results in `fuzz_report.log`.

 **Upload Logs as Artifacts:**
   - Archives the `fuzz_report.log` file for review, enabling detailed tracking of fuzz testing results.


---

## **Results**
The integrated workflow ensures:
- **Automated Code Analysis:** Codacy provides immediate feedback on code quality with detailed issue reports.
- **Bug Identification:** Fuzz testing identifies crashes and unexpected behavior in methods, with results logged for debugging.
- **Clear Visibility:** Logs and analysis are accessible for review in the GitHub Actions interface and Codacy dashboard.

<img width="919" alt="4d(2)" src="https://github.com/user-attachments/assets/b61996ba-dbbe-41db-97cb-aeeeb3da8e7d">

<img width="950" alt="4d(3)" src="https://github.com/user-attachments/assets/f20189a9-4b3e-4906-9cc3-ef06b135482f">

