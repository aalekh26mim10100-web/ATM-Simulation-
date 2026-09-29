"""
ATM Simulation System - Core Banking Module
Course: Python Essentials (First-Year B.Tech CSE)

This module defines the ATM class and essential constants for the simulation.
Concepts used:
- Fundamentals, Variables, Comments
- Data Structures: Dictionaries, Lists, Tuples, Sets, Frozen Sets, Array
- Operators: Arithmetic, Assignment, Relational, Logical, Membership, Identity, Bitwise
- Object-Oriented Programming (Class with standard attributes and methods)
"""

import array

# ==============================================================================
# CONSTANTS & CONFIGURATION
# ==============================================================================

# Bitwise flags for ATM service availability (using bitwise operators)
SERVICE_WITHDRAW = 1      # Binary: 001
SERVICE_DEPOSIT = 2       # Binary: 010
SERVICE_PIN_CHANGE = 4    # Binary: 100
SERVICE_ALL = SERVICE_WITHDRAW | SERVICE_DEPOSIT | SERVICE_PIN_CHANGE  # Binary: 111 (7)

# Frozen set for allowed transaction categories (immutable set)
VALID_TRANSACTION_TYPES = frozenset(["Deposit", "Withdrawal", "PIN Change"])

# Tuple for supported cash note denominations (fixed collection)
ACCEPTED_DENOMINATIONS = (2000, 500, 200, 100)


# ==============================================================================
# ATM CLASS DEFINITION
# ==============================================================================

class ATM:
    """
    Represents an ATM account and operations.
    Encapsulates account information, credentials, balance, and transaction history.
    """

    def __init__(self, holder_name="Avika Sharma", account_number="10010203", pin="1234", initial_balance=10000.0):
        # Dictionary for storing structured account details
        self.account_info = {
            "holder_name": holder_name,
            "account_number": account_number,
            "account_type": "Savings",
            "branch": "Campus Main Branch"
        }

        # Account credentials and monetary balance
        self.pin = str(pin)
        self.balance = float(initial_balance)

        # Dynamic list storing transaction history records as tuples
        self.transaction_history = []

        # Array data structure storing purely numeric transaction amounts for numerical calculations
        # Type code 'd' represents double-precision floating point numbers
        self.transaction_amounts = array.array('d', [])

        # Active service permissions bitmask (Bitwise concepts)
        self.service_flags = SERVICE_ALL

        # Daily withdrawal limit rules
        self.daily_limit = 20000.0
        self.total_withdrawn_today = 0.0

    def verify_pin(self, entered_pin):
        """
        Verifies if the entered PIN matches the account PIN.
        Uses relational equality operator (==).
        """
        return str(entered_pin) == self.pin

    def check_balance(self):
        """
        Returns the current available balance.
        """
        return self.balance

    def deposit(self, amount):
        """
        Deposits money into the account.
        Validates amount, updates balance, and logs the transaction.
        """
        # Bitwise operator check: verify if deposit service flag is active
        if (self.service_flags & SERVICE_DEPOSIT) == 0:
            return False, "Deposit service is currently unavailable."

        # Relational and Logical checks
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."

        # Arithmetic operator (% modulo) check: notes must be multiples of 100
        if amount % 100 != 0:
            return False, "Deposit amount must be a multiple of 100 (e.g., 500, 1000, 2500)."

        # Assignment operator (+=) to update account balance
        self.balance += amount

        # Membership operator check on frozen set
        tx_type = "Deposit"
        if tx_type in VALID_TRANSACTION_TYPES:
            # Tuple storing immutable transaction record: (type, amount, balance_after)
            record = (tx_type, float(amount), self.balance)
            self.transaction_history.append(record)

            # Record raw amount into numerical array
            self.transaction_amounts.append(float(amount))

        return True, "Deposit successful."

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        Checks for service availability, positive amount, multiple of 100,
        sufficient balance, and daily limit precedence.
        """
        # Bitwise operator check: verify if withdrawal service is active
        if (self.service_flags & SERVICE_WITHDRAW) == 0:
            return False, "Withdrawal service is currently unavailable."

        # Logical and Relational checks
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."

        if amount % 100 != 0:
            return False, "Amount must be in multiples of 100 (Available notes: Rs. 100, 200, 500, 2000)."

        # Check for sufficient account balance
        if amount > self.balance:
            return False, "Insufficient balance in your account."

        # Operator Precedence and Associativity demonstration in daily limit calculation:
        # Parentheses force (self.total_withdrawn_today + amount) to evaluate first before subtraction
        remaining_limit = self.daily_limit - (self.total_withdrawn_today + amount)
        if remaining_limit < 0:
            return False, "Transaction exceeds daily withdrawal limit of Rs. 20000.0."

        # Assignment operator (-= and +=)
        self.balance -= amount
        self.total_withdrawn_today += amount

        # Log transaction as a tuple in history list
        tx_type = "Withdrawal"
        if tx_type in VALID_TRANSACTION_TYPES:
            record = (tx_type, float(amount), self.balance)
            self.transaction_history.append(record)

            # Record raw amount into numerical array
            self.transaction_amounts.append(float(amount))

        return True, "Withdrawal successful. Please collect your cash."

    def change_pin(self, old_pin, new_pin):
        """
        Changes the account PIN after verifying the current PIN.
        """
        # Bitwise check
        if (self.service_flags & SERVICE_PIN_CHANGE) == 0:
            return False, "PIN change service is currently unavailable."

        # Comparison check for old PIN
        if str(old_pin) != self.pin:
            return False, "Current PIN is incorrect."

        new_pin_str = str(new_pin)

        # Validation: 4 digits, numeric, and not identical to old PIN
        if len(new_pin_str) != 4 or not new_pin_str.isdigit():
            return False, "New PIN must be exactly 4 numeric digits."

        if new_pin_str == self.pin:
            return False, "New PIN cannot be the same as your current PIN."

        # Update PIN
        self.pin = new_pin_str

        # Log PIN change event
        record = ("PIN Change", 0.0, self.balance)
        self.transaction_history.append(record)

        return True, "PIN changed successfully."

    def get_last_transaction(self):
        """
        Returns the most recent transaction tuple, or None if history is empty.
        Used to demonstrate identity operators (is None / is not None).
        """
        if len(self.transaction_history) == 0:
            return None
        return self.transaction_history[-1]

    def calculate_denomination_breakdown(self, amount):
        """
        Calculates currency note distribution for a withdrawal amount.
        Demonstrates tuple iteration, integer floor division (//), and modulo (%).
        """
        notes_count = {}
        remaining = int(amount)

        for denom in ACCEPTED_DENOMINATIONS:
            if remaining >= denom:
                count = remaining // denom
                remaining = remaining % denom
                notes_count[denom] = count

        return notes_count

    def get_transaction_metrics(self):
        """
        Calculates summary metrics using the numerical array.
        Demonstrates division with mixed data types (float / int = float).
        """
        count = len(self.transaction_amounts)

        if count == 0:
            return 0.0, 0, 0.0

        # Sum values stored in the array
        total_volume = 0.0
        for val in self.transaction_amounts:
            total_volume += val

        # Division with mixed data types:
        # total_volume is float, count is int -> result is float
        average_transaction = total_volume / count

        return total_volume, count, average_transaction
