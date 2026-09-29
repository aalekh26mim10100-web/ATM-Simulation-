"""
ATM Simulation System - Main Application Entry Point
Course: Python Essentials (First-Year B.Tech CSE)

This program provides an interactive, terminal-based ATM simulation.
It supports PIN authentication, balance inquiry, cash deposits, cash withdrawals,
PIN updates, transaction logging, and summary analytics.

NOTE: Implemented strictly without try/except or external libraries.
"""

from atm import ATM, ACCEPTED_DENOMINATIONS

# Set of valid menu choices for membership validation
VALID_MENU_CHOICES = {"1", "2", "3", "4", "5", "6"}


# ==============================================================================
# HELPER FUNCTIONS (INPUT VALIDATION WITHOUT TRY/EXCEPT)
# ==============================================================================

def display_banner():
    """Prints the application header."""
    print("==================================================")
    print("               WELCOME TO APEX BANK               ")
    print("             AUTOMATED TELLER MACHINE             ")
    print("==================================================")


def display_menu():
    """Displays the main user menu."""
    print("\n------------------ ATM MAIN MENU -----------------")
    print("  1. Check Balance & Account Details")
    print("  2. Deposit Cash")
    print("  3. Withdraw Cash")
    print("  4. Change Security PIN")
    print("  5. View Transaction History & Metrics")
    print("  6. Exit ATM")
    print("--------------------------------------------------")


def is_valid_numeric_string(text):
    """
    Validates whether an input string represents a valid positive number.
    Implements validation using basic string checking and control flow
    without relying on try/except blocks.
    """
    cleaned = text.strip()
    if len(cleaned) == 0:
        return False

    decimal_count = 0
    for char in cleaned:
        if char == '.':
            decimal_count += 1
            # A valid number cannot have more than one decimal point
            if decimal_count > 1:
                return False
        elif char not in "0123456789":
            # Any character other than a digit or decimal point is invalid
            return False

    # The string must not be just a lonely decimal point "."
    if cleaned == ".":
        return False

    return True


def get_positive_amount(prompt_message):
    """
    Prompts the user for a monetary amount and validates it.
    Returns the parsed float value, or None if the input was invalid.
    """
    raw_input = input(prompt_message).strip()

    # Logical NOT and membership check
    if not is_valid_numeric_string(raw_input):
        print("Error: Invalid numeric input. Please enter a valid positive number.")
        return None

    # Type conversion from str to float
    amount = float(raw_input)
    if amount <= 0:
        print("Error: Amount must be greater than zero.")
        return None

    return amount


# ==============================================================================
# MAIN APPLICATION LOGIC
# ==============================================================================

def main():
    """Main execution loop for the ATM simulation."""
    display_banner()

    # Initialize the ATM instance with sample demo account
    atm = ATM(
        holder_name="Avika Sharma",
        account_number="1001020304",
        pin="1234",
        initial_balance=10000.0
    )

    # --------------------------------------------------------------------------
    # PIN AUTHENTICATION (Maximum 3 attempts)
    # --------------------------------------------------------------------------
    print("\nPlease insert your ATM card (Simulated).")
    print("Default demo PIN is: 1234\n")

    max_attempts = 3
    attempt_count = 0
    authenticated = False

    while attempt_count < max_attempts:
        entered_pin = input("Enter your 4-digit PIN: ").strip()

        # Validate entered PIN
        if atm.verify_pin(entered_pin):
            authenticated = True
            print("\n>> PIN accepted. Login successful!")
            break
        else:
            # Assignment operator
            attempt_count += 1
            remaining = max_attempts - attempt_count
            if remaining > 0:
                print(f"Incorrect PIN. You have {remaining} attempt(s) remaining.\n")
            else:
                print("Maximum PIN attempts exceeded. Card locked for security.")

    # Control flow: terminate session if authentication fails
    if not authenticated:
        print("\nSession terminated. Please contact your branch. Goodbye!")
        return

    # --------------------------------------------------------------------------
    # MAIN MENU INTERACTIVE LOOP
    # --------------------------------------------------------------------------
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        # Membership operator check: verifying user choice against set
        if choice not in VALID_MENU_CHOICES:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        # Option 1: Check Balance & Account Details
        if choice == "1":
            print("\n---------------- ACCOUNT DETAILS -----------------")
            print(f"Account Holder   : {atm.account_info['holder_name']}")
            print(f"Account Number   : {atm.account_info['account_number']}")
            print(f"Account Type     : {atm.account_info['account_type']}")
            print(f"Branch           : {atm.account_info['branch']}")
            print(f"Available Balance: Rs. {atm.check_balance():.2f}")
            print("--------------------------------------------------")

            # Demonstration of the type() function for Python Essentials syllabus
            print(f"Metadata Info    : Balance type is {type(atm.balance).__name__}")
            print("--------------------------------------------------")

        # Option 2: Deposit Cash
        elif choice == "2":
            print("\n---------------- CASH DEPOSIT --------------------")
            print("Note: ATM accepts cash in multiples of Rs. 100 only.")
            amount = get_positive_amount("Enter amount to deposit: Rs. ")

            if amount is not None:
                success, message = atm.deposit(amount)
                if success:
                    print(f"\n>> {message}")
                    print(f">> Deposited Amount: Rs. {amount:.2f}")
                    print(f">> Updated Balance : Rs. {atm.check_balance():.2f}")
                else:
                    print(f"\n>> Transaction Failed: {message}")
            print("--------------------------------------------------")

        # Option 3: Withdraw Cash
        elif choice == "3":
            print("\n---------------- CASH WITHDRAWAL -----------------")
            print(f"Accepted denominations: {ACCEPTED_DENOMINATIONS}")
            print(f"Daily withdrawal limit: Rs. {atm.daily_limit:.2f}")
            print(f"Available Balance     : Rs. {atm.check_balance():.2f}")

            amount = get_positive_amount("Enter amount to withdraw: Rs. ")

            if amount is not None:
                success, message = atm.withdraw(amount)
                if success:
                    print(f"\n>> {message}")
                    print(f">> Withdrawn Amount: Rs. {amount:.2f}")
                    print(f">> Remaining Balance: Rs. {atm.check_balance():.2f}")

                    # Display denomination breakdown calculated with // and %
                    notes = atm.calculate_denomination_breakdown(amount)
                    print("\nNotes Dispensed:")
                    for denom in ACCEPTED_DENOMINATIONS:
                        count = notes.get(denom, 0)
                        if count > 0:
                            print(f"  - Rs. {denom:>4} x {count} note(s)")
                else:
                    print(f"\n>> Transaction Failed: {message}")
            print("--------------------------------------------------")

        # Option 4: Change Security PIN
        elif choice == "4":
            print("\n---------------- CHANGE SECURITY PIN --------------")
            current_pin = input("Enter your current PIN: ").strip()
            new_pin = input("Enter new 4-digit PIN: ").strip()
            confirm_pin = input("Re-enter new 4-digit PIN to confirm: ").strip()

            # Relational check
            if new_pin != confirm_pin:
                print("\n>> Error: New PIN and Confirmation PIN do not match.")
            else:
                success, message = atm.change_pin(current_pin, new_pin)
                if success:
                    print(f"\n>> {message}")
                    print(">> Please remember your new PIN for future transactions.")
                else:
                    print(f"\n>> Failed: {message}")
            print("--------------------------------------------------")

        # Option 5: View Transaction History & Metrics
        elif choice == "5":
            print("\n--------------- TRANSACTION HISTORY --------------")
            last_tx = atm.get_last_transaction()

            # Identity operator (is None / is not None) demonstration
            if last_tx is None:
                print("No transactions performed yet during this session.")
            else:
                print(f"{'S.No':<5} {'Type':<15} {'Amount (Rs.)':<15} {'Balance (Rs.)':<15}")
                print("-" * 50)
                index = 1
                # For loop iterating through transaction history list of tuples
                for record in atm.transaction_history:
                    t_type, t_amount, t_balance = record
                    print(f"{index:<5} {t_type:<15} {t_amount:<15.2f} {t_balance:<15.2f}")
                    index += 1

                # Display summary metrics calculated using Python array data structure
                total_vol, tx_count, avg_amount = atm.get_transaction_metrics()
                print("\n------------- SESSION METRICS (ARRAY) ------------")
                print(f"Total Monetary Volume   : Rs. {total_vol:.2f}")
                print(f"Number of Transactions  : {tx_count}")
                # Mixed type division result
                print(f"Average Transaction Size: Rs. {avg_amount:.2f}")

            print("--------------------------------------------------")

        # Option 6: Exit ATM
        elif choice == "6":
            print("\n==================================================")
            print("   Thank you for banking with Apex Bank!          ")
            print("   Please take your card and receipt. Have a day! ")
            print("==================================================")
            break


if __name__ == "__main__":
    main()
