# Automate Cybersecurity Tasks with Python

**Project: Python Scripting for Security Automation**

This project was completed as part of **Course 7** of the Google Cybersecurity Professional Certificate. I developed Python scripts to automate common security tasks such as log analysis, file updates, regex pattern matching, and device identification.

## Project Overview

I wrote and tested several Python scripts to streamline security operations, including parsing logs, updating access lists, and extracting patterns using regular expressions.

## Skills Demonstrated
- File handling (`open()`, `read()`, `write()`)
- Regular Expressions (`re` module)
- String manipulation and parsing
- Automation of security workflows
- Clean code documentation and output formatting

## Key Scripts

- **`regex-log-analyzer.py`** – Extracts IP addresses from logs and flags suspicious ones
- **`device-id-extractor.py`** – Uses regex to find devices requiring updates (IDs starting with "r15")
- **`update-files.py`** – Updates allow lists by removing unauthorized IP addresses
- **`log-file-parser.py`** – Reads and parses security log files

## Screenshots & Evidence

![Regex Log Analyzer](./images/regex-log-analyzer.png)  
**IP Address Extraction & Analysis** – Used regular expressions to identify and flag suspicious IPs.

![Device ID Extractor](./images/device-id-extractor.png)  
**Device ID Pattern Matching** – Extracted device IDs starting with "r15" for system updates.

![File Update Script](./images/update-files.png)  
**Allow List Update** – Automated removal of unauthorized IPs from access list.

![Log File Parser](./images/log-file-parser.png)  
**Log Parsing** – Read and structured security log data.

## Key Learnings
- How to effectively use Python’s `re` module for pattern matching in security logs
- Automating file updates and access control list maintenance
- Parsing and analyzing log files to support incident response
- Writing clean, reusable scripts that improve security efficiency

**Tools & Technologies:**
- Python 3
- `re` module (Regular Expressions)
- File I/O operations
- VS Code / Jupyter Notebook

---

[← Back to Main Portfolio](../README.md)
