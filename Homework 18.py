#Task 1. Write a test for the Bank class that we wrote in 14 lesson. 
# You should write a test for the open_account method. Ensure that the account is opened and has balance.

import unittest
from unittest.mock import patch
from your_bank_module import Bank, SavingsAccount, CurrentAccount

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):
        initial_balance = 1000
        account_number = "SA001"
        interest_rate = 0.05

        # Opening a savings account
        savings_account = SavingsAccount(initial_balance, account_number, interest_rate)
        self.bank.open_account(savings_account)

        # Checking if the account is in the bank's list of accounts
        self.assertIn(savings_account, self.bank._accounts)

        # Checking if the balance of the opened account is correct
        opened_account = self.bank._accounts[0]
        self.assertEqual(opened_account.get_balance(), initial_balance)

    def test_update_method(self):
        # Creation a savings account and add it to the bank
        initial_balance = 1000
        account_number = "SA001"
        interest_rate = 0.05
        savings_account = SavingsAccount(initial_balance, account_number, interest_rate)
        self.bank.open_account(savings_account)

# Task 2
# Test update method. It should check that code added interest and sent a message (print function was called).
        # Creation a mock for the print function
        with patch('builtins.print') as mock_print:
            # Call the update method
            self.bank.update()

            # Checking if the add_interest method was called for the savings account
            savings_account.add_interest.assert_called_once()

            # Checking if the print function was called for the savings account
            mock_print.assert_called_with(f"Letter sent to account {account_number}: Account in overdraft.")

if __name__ == '__main__':
    unittest.main()
