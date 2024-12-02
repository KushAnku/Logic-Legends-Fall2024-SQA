# Logic-Legends-Fall2024-SQA

## Project Overview
The objective of this project is to integrate software quality assurance activities into an existing Python project. The focus is on applying techniques and tools learned during workshops, such as static analysis, dynamic analysis, and quality assurance automation, to improve the overall software quality of the `MLForensics` project.

---

## Team Members

| Name                 | Email                   |
|----------------------|-------------------------|
| Ankush Singh         | ans0148@auburn.edu      |
| Aparana Pant         | azp0200@auburn.edu      |
| Disharee Bhowmick    | dzb0110@auburn.edu      |
| Parishruthi Ganesh   | pzg0050@auburn.edu      |

---

## Project Highlights

### Objective
The project focuses on integrating Software Quality Assurance (SQA) practices into an existing Python project. It involves implementing and automating SQA tasks to ensure code quality, security, and functionality.

### Activities
The project incorporates the following key SQA activities:

#### Git Hooks for Security Analysis
A Git Hook will automatically run security analysis tools on Python files upon changes and commit, generating a CSV file with identified security weaknesses.

#### Fuzz Testing
A `fuzz.py` script will perform fuzz testing on five Python methods, identifying potential bugs and edge cases. The fuzzing process will be integrated into GitHub Actions.

#### Forensics Integration
Modifications to five Python methods will include forensics techniques to enhance traceability and debugging.

#### Continuous Integration (CI)
CI is integrated with GitHub Actions to automate testing and ensure consistent quality checks for every code change.

