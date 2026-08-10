# Project 1 – File Management, Log Parsing and Automation

## 📌 Project Overview

This project is a Python-based automation system developed to perform common file management tasks, analyze log files, and automate repetitive operations.

The project demonstrates how Python can be used to reduce manual work and efficiently process files and system logs.

## 🎯 Objectives

- Automate file organization based on file types.
- Parse log files and identify different types of messages.
- Count INFO, WARNING, and ERROR messages.
- Generate an automated log analysis report.
- Combine multiple tasks into a single automated workflow.

## 🚀 Features

### 1. File Management

The file management script automatically organizes files into folders based on their extensions.

Supported categories include:

- Images
- Documents
- Audio
- Videos
- Archives
- Others

### 2. Log Parsing

The log parser reads a log file and counts:

- INFO messages
- WARNING messages
- ERROR messages

### 3. Automated Reporting

The program generates a `log_report.txt` file containing the results of the log analysis.

### 4. Complete Automation

The `main.py` file runs the complete workflow automatically.

## 🛠️ Technologies Used

- Python
- File Handling
- OS Module
- Shutil Module
- Log Parsing
- Automation
- Git
- GitHub

## 📂 Project Structure

```text
PROJECT1/
│
├── main.py
├── file_manager.py
├── log_parser.py
├── automation.py
├── sample.log
├── log_report.txt
└── .gitignore