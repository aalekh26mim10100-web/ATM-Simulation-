# ATM Simulation System

A beginner-level, command-line **ATM Simulation System** developed in pure Python as part of the **Python Essentials** course (First-Year B.Tech Computer Science & Engineering).

---

## 1. Project Description

The **ATM Simulation System** is a realistic console-based banking application designed to simulate standard Automated Teller Machine (ATM) workflows. It provides an authentic banking experience where users can authenticate with a secure 4-digit PIN (limited to 3 attempts), inspect their account balance and profile details, deposit money in standard currency denominations, withdraw cash with denomination breakdown, update their security PIN, and review a complete transaction history with numerical session metrics.

This project is built strictly using fundamental Python constructs taught in a foundational programming curriculum, avoiding over-engineering, external packages, graphic user interfaces, web frameworks, or databases.

---

## 2. Project Objective

- To implement core programming principles and foundational problem-solving in Python.
- To demonstrate practical, real-world application of all topics covered in the Python Essentials syllabus.
- To model banking entities using beginner-level Object-Oriented Programming (encapsulation with classes, attributes, and methods).
- To practice robust input validation and defensive programming without relying on complex exception-handling frameworks.
- To build a clean, interactive command-line interface that runs on any standard Python installation.

---

## 3. Key Features

- **Card Insertion & PIN Authentication**: Pre-configured demo account with 4-digit PIN authentication (`1234`) and a 3-attempt security lockout.
- **Account Inquiry**: View account holder details, account number, branch, account type, and real-time available balance.
- **Cash Deposit**: Add funds to the account in valid ATM multiples (Rs. 100 notes), automatically updating the balance and recording the transaction.
- **Cash Withdrawal**: Withdraw money with balance checks, daily limit enforcement (Rs. 20,000/day), denomination checks (multiples of 100), and an automatic currency notes breakdown (e.g., Rs. 2000, 500, 200, 100).
- **PIN Update**: Securely change the 4-digit PIN after verifying the existing PIN.
- **Transaction History**: Chronological log of all session activities stored as immutable transaction records.
- **Session Metrics**: Computes total transaction volume, transaction count, and average transaction amount using Python's native `array` module and mixed-type division.

---

## 4. Technologies Used

- **Language**: Python 3 (3.8+)
- **Libraries**: Python Standard Library only (`array`, `sys`, `os`)
- **Third-Party Packages**: None (Zero external dependencies)
- **Database / File Storage**: None (In-memory simulation)
- **User Interface**: Pure Command-Line Interface (CLI / Terminal)

---

## 5. Python Concepts Used (Syllabus Mapping)

Every feature in this project directly implements a topic from the first-year Python Essentials course:

| # | Course Topic | Implementation in Project |
| :---: | :--- | :--- |
| **1** | Python Fundamentals | Variables, comments, consistent indentation, PEP-8 naming conventions. |
| **2** | Input & Output Operations | `input()` for reading user commands and values; `print()` for menus and receipts. |
| **3** | `type()` Function | Inspecting and displaying variable data types in account details (`type(balance)`). |
| **4** | Type Conversion | `float()` for amounts, `int()` for notes calculations, and `str()` for PIN handling. |
| **5** | Arithmetic Operators | `+`, `-`, `*`, `/`, `//` (integer division for note counts), `%` (modulo for multiples of 100). |
| **6** | Assignment Operators | `=`, `+=` (balance increment, counters), `-=` (balance deduction). |
| **7** | Relational Operators | `==`, `!=`, `<`, `>`, `<=`, `>=` (PIN checking, limit comparisons, balance checks). |
| **8** | Logical `and` Operator | Checking compound conditions (e.g., `amount > 0 and amount <= self.balance`). |
| **9** | Logical `or` Operator | Validating multiple input conditions or character checks. |
| **10** | Logical `not` Operator | Guard conditions such as `not is_valid_numeric_string(raw_input)`. |
| **11** | Membership Operators | `in` and `not in` checking menu selection against `VALID_MENU_CHOICES`. |
| **12** | Identity Operators | `is None` and `is not None` verifying if transaction history has any entries. |
| **13** | Bitwise Operators | Bitwise flag masks (`&`, `|`, `~`) managing active ATM service permissions. |
| **14** | Mixed-Type Division | Division of `float` total volume by `int` transaction count to compute average transaction size. |
| **15** | Operator Precedence | Daily limit calculation: `remaining = daily_limit - (total_withdrawn + amount)`. |
| **16** | Lists | `self.transaction_history = []` dynamically storing chronological activity records. |
| **17** | Tuples | Fixed accepted denominations `(2000, 500, 200, 100)` and transaction log records. |
| **18** | Sets | `VALID_MENU_CHOICES = {"1", "2", "3", "4", "5", "6"}` for set-based validation. |
| **19** | Dictionaries | `self.account_info` storing structured account holder profile details. |
| **20** | Frozen Sets | `VALID_TRANSACTION_TYPES = frozenset(...)` defining immutable valid transaction categories. |
| **21** | Control Flow Statements | `if`, `elif`, `else` conditionals; `while` for loops; `for` loops; `break` and `continue`. |
| **22** | Functions | Modular procedures (`display_menu()`, `is_valid_numeric_string()`, `get_positive_amount()`). |
| **23** | Modules & Packages | Structured into `atm.py` (business logic) and `main.py` (CLI interface). |
| **24** | Array Data Structure | Native `array.array('d')` storing raw transaction amounts for numerical summaries. |
| **25** | Object-Oriented Programming | `ATM` class encapsulating account balance, data structures, and banking methods. |

---

## 6. Project Structure

```text
ATM-Simulation/
│
├── atm.py               # Core ATM class, data structures, and banking logic
├── main.py              # CLI user interface, input validation, and main loop
├── tests/
│   └── test_project.py  # Standalone assertion test suite (zero external test frameworks)
├── README.md            # Project documentation, concepts, and usage instructions
└── project_report.md    # Academic project report for course submission
```

---

## 7. Requirements & Prerequisites

- **Python Version**: Python 3.8 or higher.
- **Operating System**: Windows, macOS, or Linux.
- **Dependencies**: None. Only standard library built-ins are required.

---

## 8. Installation & Setup Instructions

1. **Clone or Download** the project folder onto your local computer.
2. Open a terminal or command prompt (`PowerShell`, `cmd`, or `bash`).
3. Navigate to the project directory:
   ```bash
   cd path/to/ATM-Simulation
   ```

---

## 9. How to Run the Project

### Running the Application
Execute the following command in your terminal:
```bash
python main.py
```

### Running the Test Suite
To verify that all banking logic, calculations, and assertions pass:
```bash
python tests/test_project.py
```

---

## 10. Example Usage & Sample Session

```text
==================================================
               WELCOME TO APEX BANK               
             AUTOMATED TELLER MACHINE             
==================================================

Please insert your ATM card (Simulated).
Default demo PIN is: 1234

Enter your 4-digit PIN: 1234

>> PIN accepted. Login successful!

------------------ ATM MAIN MENU -----------------
  1. Check Balance & Account Details
  2. Deposit Cash
  3. Withdraw Cash
  4. Change Security PIN
  5. View Transaction History & Metrics
  6. Exit ATM
--------------------------------------------------
Enter your choice (1-6): 1

---------------- ACCOUNT DETAILS -----------------
Account Holder   : Avika Sharma
Account Number   : 1001020304
Account Type     : Savings
Branch           : Campus Main Branch
Available Balance: Rs. 10000.00
--------------------------------------------------
Metadata Info    : Balance type is float
--------------------------------------------------

------------------ ATM MAIN MENU -----------------
  1. Check Balance & Account Details
  2. Deposit Cash
  3. Withdraw Cash
  4. Change Security PIN
  5. View Transaction History & Metrics
  6. Exit ATM
--------------------------------------------------
Enter your choice (1-6): 3

---------------- CASH WITHDRAWAL -----------------
Accepted denominations: (2000, 500, 200, 100)
Daily withdrawal limit: Rs. 20000.00
Available Balance     : Rs. 10000.00
Enter amount to withdraw: Rs. 1700

>> Withdrawal successful. Please collect your cash.
>> Withdrawn Amount: Rs. 1700.00
>> Remaining Balance: Rs. 8300.00

Notes Dispensed:
  - Rs.  500 x 3 note(s)
  - Rs.  200 x 1 note(s)
--------------------------------------------------

------------------ ATM MAIN MENU -----------------
  1. Check Balance & Account Details
  2. Deposit Cash
  3. Withdraw Cash
  4. Change Security PIN
  5. View Transaction History & Metrics
  6. Exit ATM
--------------------------------------------------
Enter your choice (1-6): 5

--------------- TRANSACTION HISTORY --------------
S.No  Type            Amount (Rs.)    Balance (Rs.)  
--------------------------------------------------
1     Withdrawal      1700.00         8300.00        

------------- SESSION METRICS (ARRAY) ------------
Total Monetary Volume   : Rs. 1700.00
Number of Transactions  : 1
Average Transaction Size: Rs. 1700.00
--------------------------------------------------
```

---

## 11. Limitations

1. **In-Memory Volatility**: Data is retained during the active session only. Because file I/O and databases are intentionally excluded per course guidelines, restarting the program resets balance and transactions.
2. **Single User Session**: The application models one active customer session at a time.
3. **No External Network**: Does not connect to live banking networks, clearing houses, or card magnetic strip readers.

---

## 12. Future Scope & Improvements

- **Persistent Storage**: Incorporate file handling (text/CSV) or relational databases (SQLite) to store customer accounts across sessions.
- **Multi-Account Support**: Allow multiple card numbers with account switching.
- **Cryptographic Hashing**: Store PINs as SHA-256 hashes instead of plaintext strings.
- **Graphical Interface**: Implement a graphical interface using Tkinter or web technologies once advanced course modules are completed.
